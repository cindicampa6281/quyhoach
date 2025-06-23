from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
from sqlalchemy.dialects.mysql import LONGTEXT
from shapely.geometry import MultiPolygon
from geoalchemy2 import Geometry

class DiaChinh(Base):
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    __tablename__ = 'DiaChinh'
    id = Column(String(255), primary_key=True, nullable=False)
    
    soqd = Column(String(255), nullable=True)
    doan = Column(String(255), nullable=True)
    shthua = Column(String(255), nullable=True)
    shbando = Column(String(255), nullable=True)
    
    tinhtp = Column(String(255), nullable=True)
    xaphuong = Column(String(255), nullable=True)
    quanhuyen = Column(String(255), nullable=True)
    
    
    type = Column(String(255), nullable=True)
    geometry_name = Column(String(255), nullable=True)
    objectid = Column(String(255), nullable=True)
    madoituong = Column(String(255), nullable=True)
    loaidat = Column(String(255), nullable=True)
    danso = Column(String(255), nullable=True)
    matdoxaydu = Column(String(255), nullable=True)
    tangcao = Column(String(255), nullable=True)
    ghichu = Column(String(255), nullable=True)
    kyhieukhuq = Column(String(255), nullable=True)
    kyhieuoqh = Column(String(255), nullable=True)
    trangthaiq = Column(String(255), nullable=True)
    kyhieuphan = Column(String(255), nullable=True)
    cancuphapl = Column(String(255), nullable=True)
    dientich = Column(Float, nullable=True)
    shape_leng = Column(Float, nullable=True)
    shape_area = Column(Float, nullable=True)
    matdoxaydu = Column(String(255), nullable=True)
    
    shape_le_1 = Column(Float, nullable=True)
    
    # DistrictID = Column(Integer, ForeignKey('Districts.DistrictID'))
    # ProvinceID = Column(Integer, ForeignKey('Provinces.ProvinceID'))
    
    
    multipolygon = Column(LONGTEXT, nullable=True)
    polygonType = Column(Text, nullable=True)
    geometry = Column(Geometry, nullable=True)
    # bbox = Column(Text, nullable=True)