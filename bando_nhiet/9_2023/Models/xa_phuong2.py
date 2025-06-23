from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime
class xa_phuong2(Base):
    __tablename__ = "xa_phuong2"
    WandID = Column(Integer, primary_key=True)    
    WandName = Column(Text)
    WandType = Column(Text)
    WandNameEnglish = Column(Text)
    DistrictID = Column(Integer, ForeignKey('Districts.DistrictID'))
    ProvinceID = Column(Integer, ForeignKey('Provinces.ProvinceID'))
    bbox 	= Column(Text)
    center 	= Column(Text)
    wikidata 	= Column(Text, nullable=False )
