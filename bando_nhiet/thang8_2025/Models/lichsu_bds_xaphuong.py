from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

class lichsu_bds_xaphuong(Base):
    __tablename__ = 'lichsu_bds_xaphuong'
    id = Column(Integer, primary_key=True, nullable=False)
    district_id = Column(Integer, nullable=False)
    province_id = Column(Integer, nullable=False)
    ward_id = Column(Integer, nullable=True)

    biet_thu = Column(Text, nullable=True) 
    tho_cu = Column(Text, nullable=True) 
    shophouse = Column(Text, nullable=True) 
    chung_cu = Column(Text, nullable=True) 
    
    date_create = Column(DateTime, nullable=True)
    name_provinces = Column(Text, nullable=True) 
    name_district = Column(Text, nullable=True) 