from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base
import datetime
class historychartdangcap(Base):
    __tablename__ = 'historychartdangcap'
    id_his = Column(Integer, primary_key=True, nullable=False)
    HistoryID = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    quarter = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    max = Column(Float, nullable=True)
    avg = Column(Float, nullable=True)
    min = Column(Float, nullable=True)
    startDate = Column(DateTime, nullable=True)
    endDate = Column(DateTime, nullable=True)
    #____________________________________________________________________________________

