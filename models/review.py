#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = "reviews"
    text = Column(String(1023), nullable=false)
    place_id = Column(String(60), ForeignKey('places.if')nullable=false)
    user_id = Column(String(60), ForeignKey('users.if')nullable=false)
