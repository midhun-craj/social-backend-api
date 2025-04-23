from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class FriendRequestStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    bio = Column(String, default="")

    sent_requests = relationship("FriendRequest", back_populates="sender", foreign_keys='FriendRequest.sender_id')
    received_requests = relationship("FriendRequest", back_populates="receiver", foreign_keys='FriendRequest.receiver_id')

class FriendRequest(Base):
    __tablename__ = "friend_requests"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum(FriendRequestStatus), default=FriendRequestStatus.pending)

    sender = relationship("User", back_populates="sent_requests", foreign_keys=[sender_id])
    receiver = relationship("User", back_populates="received_requests", foreign_keys=[receiver_id])