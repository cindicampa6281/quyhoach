from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class du_an_dautu_phattrien(Base):
    __tablename__ = 'du_an_dautu_phattrien'
    id = Column( String(255) , primary_key=True)
    name_du_an = Column( String(255) , unique=True, nullable=True)
    chu_dau_tu = Column( String(255) , unique=True, nullable=True)
    tong_dautu = Column( String(255) , unique=True, nullable=True)
    nguoi_tham_quyen = Column( String(255) , unique=True, nullable=True)
    thoi_gian_thuchien = Column( String(255) , unique=True, nullable=True)
    nhom_du_an = Column( String(255) , unique=True, nullable=True)
    so_quyet_dinh = Column( String(255) , unique=True, nullable=True)
    ngay_phe_duyet = Column( DateTime, unique=True, nullable=True)
    link_muasamcong = Column( String(2550) , unique=True, nullable=True)
    id_district = Column( Integer , unique=True, nullable=True)
    id_provinces = Column( Integer , unique=True, nullable=True)
    id_xaphuong = Column( Integer , unique=True, nullable=True)
    time_public = Column( DateTime , unique=True, nullable=True)
    name_tinh = Column( String(255) , unique=True, nullable=True)
    id_muasamcong = Column( String(255) , unique=True, nullable=True)
    ngay_dangtai =  Column( String(255) , unique=True, nullable=True)
    ngaypheduyet =  Column( String(255) , unique=True, nullable=True)
    link_bidwinner =  Column( String(255) , unique=True, nullable=True)