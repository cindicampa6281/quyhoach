from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime


from Database.Database import Base

from geoalchemy2 import Geometry

from shapely.geometry import MultiPolygon
from sqlalchemy.dialects.mysql import LONGTEXT


class XaPhuong(Base):
    __tablename__ = "xa_phuong"
    WandID = Column(Integer, primary_key=True)
    
    
    
    WandName = Column(Text)
    WandType = Column(Text)
    WandNameEnglish = Column(Text)
    
    DistrictID = Column(Integer, ForeignKey('Districts.DistrictID'))
    ProvinceID = Column(Integer, ForeignKey('Provinces.ProvinceID'))
    
    
    multipolygon = Column(Geometry, nullable=True)
    polygonType = Column(Text, nullable=True)
    bbox = Column(Text, nullable=True)
    bounding_box = Column(Text, nullable=True)
    
    center 	= Column(Text, nullable=True)
    wikidata 	= Column(Text, nullable=True)
    polygon2 	= Column(Text, nullable=True)
    
    polygon_diocthongthai = Column(LONGTEXT)
