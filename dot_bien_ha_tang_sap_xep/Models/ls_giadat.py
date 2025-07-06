from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime
class ls_giadat(Base):
    __tablename__ = 'lich_su_gia_dat'
    id = Column(Integer, primary_key=True, nullable=False)
    DistrictID = Column(Integer, nullable=False)
    ProvinceID = Column(Integer, nullable=False)
    url = Column(String(600), nullable=True)
    poster = Column(String(255), nullable=True)
    price = Column(String(255), nullable=True)
    area = Column(String(255), nullable=True)
    
    description = Column(String(255), nullable=True)
    image_links = Column(String(255), nullable=True)
    location_text = Column(String(255), nullable=True)
    
    province = Column(String(255), nullable=True)
    district = Column(String(255), nullable=True)
    ward = Column(String(255), nullable=True)
    WandID = Column(Integer, nullable=True)
    HistoryID = Column(Integer, nullable=True)
    type = Column(String(255), nullable=True)
    time_create = Column(DateTime, nullable=True)