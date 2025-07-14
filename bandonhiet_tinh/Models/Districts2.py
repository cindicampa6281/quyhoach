from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base


class Districts2(Base):
    __tablename__ = 'Districts2'
    DistrictID = Column(Integer, primary_key=True, autoincrement=True)
    
    DistrictName = Column(String(50), unique=True, nullable=False)
    
    DistrictType = Column(Text, nullable=False)
    
    DistrictNameEnglish = Column(String(50), unique=True, nullable=False)
    
    ProvinceID = Column(Integer, ForeignKey('Provinces2.ProvinceID'))
    coordinates = Column(Text, nullable=False)
    bounding_box = Column(Text, nullable=False)
    

    