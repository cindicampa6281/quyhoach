from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime


class GiaDatTVPL(Base):
    __tablename__ = "GiaDatTVPL"
    
    id = Column(String(10), primary_key=True, nullable = False)
    # DistrictName = Column(Text, nullable=True)
    
    # WardName = Column(Text, nullable=True)
    # WardId = Column(Text, nullable=True)
    VT1 = Column(Text, nullable=True)
    VT2 = Column(Text, nullable=True)
    VT3 = Column(Text, nullable=True)
    VT4 = Column(Text, nullable=True)
    VT5 = Column(Text, nullable=True)
    Type  = Column(Text, nullable=True)
    RoadName = Column(Text, nullable=True)
    
    FromTo = Column(Text, nullable=True)
    
    DistrictId = Column(Integer, ForeignKey('Districts.DistrictID'))
    ProvinceId = Column(Integer, ForeignKey('Provinces.ProvinceID'))
    CreateAt = Column(DateTime, default=datetime.datetime.now())
