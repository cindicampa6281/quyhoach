from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

class bando_nhiet_district_month(Base):
    __tablename__ = 'bando_nhiet_district_month'
    id = Column(Integer, primary_key=True, nullable=False)
    DistrictID = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    chung_cu = Column(LONGTEXT, nullable=True)
    biet_thu = Column(LONGTEXT, nullable=True)
    tho_cu = Column(LONGTEXT, nullable=True)
    shophouse = Column(LONGTEXT, nullable=True)
    name_district  = Column(Text, nullable=True)
    name_provinces = Column(Text, nullable=True) 



