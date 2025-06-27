from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime

class gia_dat_xa_phuong(Base):
    __tablename__ = 'gia_dat_xa_phuong'
    id = Column(Integer, primary_key=True, nullable=False)
    DistrictID = Column(Integer, nullable=False)
    ProvinceID = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    WandID = Column(Integer, nullable=True)

    url = Column(String(600), nullable=True)
    price = Column(String(255), nullable=True)
    area = Column(String(255), nullable=True)
    
    description = Column(String(255), nullable=True)
    image_links = Column(String(255), nullable=True)
    location_text = Column(String(255), nullable=True)
    
    list_historyID = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    
    min_price = Column(Float, nullable=True)
    max_price = Column(Float, nullable=True)
    avg_price = Column(Float, nullable=True)
    startDate = Column(DateTime , nullable=True)
    endDate = Column(DateTime , nullable=True)

