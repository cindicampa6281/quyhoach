from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Date, Time, SmallInteger, Boolean, LargeBinary
from Database.Database import Base

class quyhoach_quan_huyen(Base):
    __tablename__ = 'quyhoach_quan_huyen'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idDistrict = Column(Integer, nullable=False)
    idProvince = Column(Integer , nullable=False)
    description = Column(String(255) , default=False)
    image = Column(String(255) , default=False)
    imageHttp = Column(String(255) , default=False)
    location = Column(String(255) , default=False)
    boundingbox = Column(String(255) ,  default=False)
    coordation = Column(String(255) , default=False)
    huyen_image = Column(String(255) , default=False)
    so_lan_view = Column(Integer , nullable=False)
    is_du_an = Column(Integer , nullable=False)
    zoom = Column(Integer, nullable=False)
    nam_het_han = Column(Integer , nullable=False)
    min_zoom = Column(Integer , nullable=False)
    map_type  = Column(Integer , nullable=False)
    link_server = Column(String(255) , default=False)

