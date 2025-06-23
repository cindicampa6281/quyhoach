from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text, Boolean, JSON
from Database.Database import Base
import datetime

from Models.Districts import *
from Models.Provinces import *
from Models.XaPhuong import *

class NhaDauTu(Base):
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    __tablename__ = 'NhaDauTu'

    orgCode = Column(String(255), primary_key=True, nullable = False)

    accountingType = Column(String(255), nullable = True)
    agencyName = Column(String(255), nullable = True)
    authenType = Column(Integer, nullable = True)
    banks = Column(JSON, nullable = True)
    budgetCode = Column(String(255), nullable = True)
    businessStatus = Column(String(255), nullable = True)
    businessType = Column(String(255), nullable = True)
    businesses = Column(JSON, nullable = True)
    caRegister = Column(Boolean, nullable = True)
    chapterCapital = Column(String(255), nullable = True)
    chapterCode = Column(String(255), nullable = True)
    consider = Column(Integer, nullable = True)
    decNo = Column(String(255), nullable = True)
    docNo = Column(String(255), nullable = True)
    eorgCode = Column(String(255), nullable = True)
    files = Column(JSON, nullable = True)
    
    id = Column(String(255), nullable = True)
    idTypes = Column(String(255), nullable = True)
    isAgencies = Column(Boolean, nullable = True)
    isForeignInvestor = Column(Boolean, nullable = True)
    isPlanInvest = Column(Boolean, nullable = True)
    language = Column(String(255), nullable = True)
    location = Column(String(255), nullable = True)
    officeAdd = Column(String(255), nullable = True)
    officeDisID = Column(Integer, ForeignKey('Districts.DistrictID'), nullable = True)
    
    
    officePhone = Column(String(255), nullable = True)
    
    
    officeProID = Column(Integer, ForeignKey('Provinces.ProvinceID'), nullable = True)
    officeWarID = Column(Integer, ForeignKey(XaPhuong.WandID), nullable = True)
    
    
    officeWeb = Column(String(255), nullable = True)
    officeZipcode = Column(String(255), nullable = True)
    
    orgEnName = Column(String(255), nullable = True)
    orgFullName = Column(String(255), nullable = True)
    proManagementUnit = Column(String(255), nullable = True)
    reason = Column(String(255), nullable = True)
    recAdd = Column(String(255), nullable = True)
    recByOffice = Column(String(255), nullable = True)
    
    
    recDisID = Column(Integer, ForeignKey('Districts.DistrictID'), nullable = True)
                    
                    
    recEmailElecInvo = Column(String(255), nullable = True)
    
    recIdDateTime = Column(DateTime, nullable = True)
    
    recIdNo = Column(String(255), nullable = True)
    recIdType = Column(String(255), nullable = True)
    recProID = Column(Integer, ForeignKey('Provinces.ProvinceID'), nullable = True)
    recWarID = Column(Integer, ForeignKey(XaPhuong.WandID), nullable = True)

    recZipcode = Column(String(255), nullable = True)
    receiverEmail = Column(String(255), nullable = True)
    receiverName = Column(String(255), nullable = True)
    receiverPhone = Column(String(255), nullable = True)
    repEmail = Column(String(255), nullable = True)
    
    
    repIdDateTime = Column(DateTime, nullable = True)
    
    
    repIdNation = Column(String(255), nullable = True)
    repIdNo = Column(String(255), nullable = True)
    repIdType = Column(String(255), nullable = True)
    repName = Column(String(255), nullable = True)
    repPhone = Column(String(255), nullable = True)
    repPosition = Column(String(255), nullable = True)
    statusOrg = Column(String(255), nullable = True)
    taxCode = Column(String(255), nullable = True)
    taxCodeStatus = Column(String(255), nullable = True)
    
    
    taxDateTime = Column(DateTime, nullable = True)
    
    
    taxNation = Column(String(255), nullable = True)

