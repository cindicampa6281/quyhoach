
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text

# from sqlalchemy.orm import relationship

from Database.Database import Base

from geoalchemy2 import Geometry

from shapely.geometry import MultiPolygon


class Provinces(Base):
    __tablename__ = 'Provinces'
    ProvinceID = Column(Integer, primary_key=True)
    ProvinceName = Column(String(50), nullable=False)
    bounding_box = Column(String(1000), nullable=False)
    
    multipolygon = Column(Geometry('MULTIPOLYGON'), nullable=False)
    bbox = Column(Text, nullable=False)

