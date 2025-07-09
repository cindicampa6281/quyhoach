from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
from sqlalchemy.dialects.mysql import LONGTEXT
from shapely.geometry import MultiPolygon
from geoalchemy2 import Geometry
class Districts(Base):
    __tablename__ = 'Districts'
    DistrictID = Column(Integer, primary_key=True, autoincrement=True)
    ProvinceID = Column(Integer, ForeignKey('Provinces.ProvinceID'))
    DistrictName = Column(String(50), unique=True, nullable=False)

    multipolygon = Column(Geometry('MULTIPOLYGON'), nullable=False)
    bbox = Column(Text, nullable=False)