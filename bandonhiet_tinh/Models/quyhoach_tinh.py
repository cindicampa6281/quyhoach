from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Date, Time, SmallInteger, Boolean, LargeBinary
from Database.Database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text

class quyhoach_tinh(Base):
    __tablename__ = 'quyhoach_tinh'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idProvince = Column(Integer, nullable=False)
    description = Column(Text, default=False)
    location = Column(Text, default=False)
    boundingbox = Column(Text, default=False)
    coordation = Column(Text, default=False)
    createAt = Column(DateTime, default=func.current_timestamp())
    tinh_image = Column(Text, default=False)
    so_lan_view = Column(Integer, nullable=False)
    zoom = Column(Integer, nullable=False)
    min_zoom = Column(Integer, nullable=False)
    link_server = Column(Text, default=False)
    type_load_anh = Column(Text, default=False)
    type_link = Column(Text, default=False)

