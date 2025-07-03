from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class du_an_bds(Base):
    __tablename__ = 'du_an_bds'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenDuAn = Column(String(255), unique=True, nullable=True)
    matDoXayDung = Column(String(255), unique=True, nullable=True)
    dienTich = Column(String(255), unique=True, nullable=True)
    khoiCong = Column(String(255), unique=True, nullable=True)
    loaiHinh = Column(String(255), unique=True, nullable=True)
    banGiaoDuKien = Column(String(255), unique=True, nullable=True)
    chuDauTu = Column(String(255), unique=True, nullable=True)
    trangThai = Column(String(255), unique=True, nullable=True)
    viTri = Column(String(2550), unique=True, nullable=True)
    congTyThietKe = Column(String(1000), unique=True, nullable=True)
    viTriDesc = Column(String(2000), unique=True, nullable=True)
    tienIch = Column(String(2000), unique=True, nullable=True)
    tinh = Column(Integer, nullable=True)
    quanHuyen = Column(Integer, ForeignKey('Districts.DistrictID'))
    xaPhuong = Column(Integer, ForeignKey('xa_phuong.WandID'))    
    images = Column(String(2000), unique=True, nullable=True)
    link_detail  = Column(String(255), unique=True, nullable=True)
    toaDo = Column(String(255), unique=True, nullable=True)
    
    donViThiCong = Column(String(255), unique=True, nullable=True)
    dienTichXayDung = Column(String(255), unique=True, nullable=True)
    dienTichSanXayDung = Column(String(255), unique=True, nullable=True)
    dienTichMin = Column(String(255), unique=True, nullable=True)
    dienTichMax = Column(String(255), unique=True, nullable=True)
    congTrinhCongCong = Column(String(255), unique=True, nullable=True)
    tongVonDauTu = Column(String(255), unique=True, nullable=True)
    chiTiet = Column(String(255), unique=True, nullable=True)
    gioiThieu = Column(String(255), unique=True, nullable=True)
    giaMinPerM2 = Column(String(255), unique=True, nullable=True)
    giaMin = Column(String(255), unique=True, nullable=True)
    soTangCao = Column(String(255), unique=True, nullable=True)
    soTangHam = Column(String(255), unique=True, nullable=True)
    soLuongCanHo = Column(String(255), unique=True, nullable=True)
    soLuongDatNen = Column(String(255), unique=True, nullable=True)
    soLuongBietThu = Column(String(255), unique=True, nullable=True)
    soLuongNhaMatDat = Column(String(255), unique=True, nullable=True)
    link = Column(String(255), unique=True, nullable=True)
    test = Column(String(255), unique=True, nullable=True)
    polygon = Column(String(1000), unique=True, nullable=True)
    giaDuAnCungKhuVuc = Column(String(1000), unique=True, nullable=True)

    