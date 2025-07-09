from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text

# from sqlalchemy.orm import relationship

from Database.Database import Base


class Provinces2(Base):
    __tablename__ = 'Provinces2'
    ProvinceID = Column(Integer, primary_key=True)
    ProvinceName = Column(String(50), nullable=False)
    ProvinceType = Column(String(50), nullable=False)
    ProvinceNameEnglish = Column(String(50), nullable=False)

