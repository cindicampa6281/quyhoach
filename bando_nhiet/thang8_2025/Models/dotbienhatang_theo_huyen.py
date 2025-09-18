from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text, Boolean, JSON , Double
from Database.Database import Base
import datetime

from Models.Districts import *
from Models.Provinces import *
from Models.XaPhuong import *

class dotbienhatang_theo_huyen(Base):
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    __tablename__ = 'dotbienhatang_theo_huyen'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ProvinceID = Column(Text, nullable = True)
    DistrictID = Column(Text, nullable = True)
    id_xaphuong = Column(Text, nullable = True)
    dotbien_hatang = Column( LONGTEXT , nullable = True)
    tongmuc_dautu  = Column( Double , nullable = True)	
    chudautu = Column( Text , nullable = True)		
    link_muasamcong = Column( Text , nullable = True)	
    id_muasamcong = Column( Text , nullable = True)	
    publicDate = Column( DateTime , nullable = True)	
    projectName = Column( Text , nullable = True)	
    createdBy = Column( Text , nullable = True)	
    json_data = Column( LONGTEXT , nullable = True)
    bidCloseDate = Column( DateTime , nullable = True)	
    bidNamePlanNew =  Column( LONGTEXT , nullable = True)
    bidName =  Column( LONGTEXT , nullable = True)
