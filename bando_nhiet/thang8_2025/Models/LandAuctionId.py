from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import *


class LandAuctionId(Base):
    __tablename__ = 'LandAuctionId'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, nullable=False)