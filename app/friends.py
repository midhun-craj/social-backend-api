from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, auth
from app.models import FriendRequestStatus

router = APIRouter()

@router.post("/friends/request")
def send_friend_request(
    request: schemas.FriendRequestCreate,
    db: Session = Depends(auth.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if request.receiver_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot send request to yourself")
    exists = db.query(models.FriendRequest).filter_by(sender_id=current_user.id, receiver_id=request.receiver_id).first()
    if exists:
        raise HTTPException(status_code=400, detail="Request already sent")
    fr = models.FriendRequest(sender_id=current_user.id, receiver_id=request.receiver_id)
    db.add(fr)
    db.commit()
    return {"message": "Request sent"}

@router.post("/friends/action")
def action_on_request(
    action: schemas.FriendRequestAction,
    db: Session = Depends(auth.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    fr = db.query(models.FriendRequest).filter_by(id=action.request_id, receiver_id=current_user.id).first()
    if not fr:
        raise HTTPException(status_code=404, detail="Request not found")
    if action.action not in ["accept", "reject"]:
        raise HTTPException(status_code=400, detail="Invalid action")
    if action.action == "accept":
        fr.status = FriendRequestStatus.accepted
    elif action.action == "reject":
        fr.status = FriendRequestStatus.rejected
    db.commit()
    return {"message": f"Request {action.action}ed"}

@router.get("/friends", response_model=list[schemas.UserOut])
def list_friends(
    db: Session = Depends(auth.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    friends = db.query(models.User).join(models.FriendRequest,
        ((models.FriendRequest.sender_id == current_user.id) & (models.FriendRequest.receiver_id == models.User.id)) |
        ((models.FriendRequest.receiver_id == current_user.id) & (models.FriendRequest.sender_id == models.User.id))
    ).filter(models.FriendRequest.status == "accepted").all()
    return friends