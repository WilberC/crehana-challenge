from database import Base

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    body = Column(Text)
    post_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship("Post", back_populates="comments")
