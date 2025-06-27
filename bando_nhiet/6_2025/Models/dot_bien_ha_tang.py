from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text, Boolean, JSON
from Database.Database import Base
import datetime

from Models.Districts import *
from Models.Provinces import *


class dot_bien_ha_tang(Base):
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    __tablename__ = 'dot_bien_ha_tang'
    json_data = Column(LONGTEXT, nullable=True)
    id = Column(String(255), primary_key=True)
    notifyNo = Column(Text, nullable=True)
    notifyVersion = Column(Text, nullable=True)
    bidNo = Column(Text, nullable=True)
    planNo = Column(Text, nullable=True)
    publicDate = Column(DateTime, nullable=True)
    procuringEntityCode = Column(Text, nullable=True)
    bidOpenDate = Column(DateTime, nullable=True)
    
    status = Column(Text, nullable=True)
    guaranteeValue = Column(Float, nullable=True)
    guaranteeForm = Column(Text, nullable=True)
    
    bidCloseDate = Column(DateTime, nullable=True)
    
    bidName = Column(LONGTEXT, nullable=True)
    capitalDetail = Column(Text, nullable=True)
    contractType = Column(Text, nullable=True)
    bidForm = Column(Text, nullable=True)
    bidMode = Column(Text, nullable=True)
    contractPeriodUnit = Column(Text, nullable=True)
    contractPeriod = Column(Integer, nullable=True)
    planName = Column(Text, nullable=True)
    investField = Column(Text, nullable=True)
    planType = Column(Text, nullable=True)
    
    projectName = Column(Text, nullable=True)
    procuringEntityName = Column(Text, nullable=True)
    investorCode = Column(Text, nullable=True)
    investorName = Column(Text, nullable=True)
    isDomestic = Column(Boolean, nullable=True)
    bidPrice = Column(Float, nullable=True)
    bidPriceUnit = Column(Text, nullable=True)
    bidEstimatePrice = Column(Float, nullable=True)
    
    bidOpenLocation = Column(Text, nullable=True)
    bidValidityPeriod = Column(Integer, nullable=True)
    bidValidityPeriodUnit = Column(Text, nullable=True)
    
    issueLocation = Column(Text, nullable=True)
    receiveLocation = Column(Text, nullable=True)
    executionLocation = Column(Text, nullable=True)
    
    feeType = Column(Text, nullable=True)
    feeValue = Column(Float, nullable=True)
    isInternet = Column(Boolean, nullable=True)
    bidNoType = Column(Text, nullable=True)
    
    bidId = Column(String(255))
    processApply = Column(Text, nullable=True)
    
    isAgreeFrame = Column(Boolean, nullable=True)
    isPrequalification = Column(Boolean, nullable=True)
    shortListNo = Column(Text, nullable=True)
    planDecisionDate = Column(DateTime, nullable=True)
    
    lotDTOList = Column(JSON, nullable=True)
    
    delayDTOList = Column(JSON, nullable=True)
    
    getVersionDTOS = Column(JSON, nullable=True)
    
    createdBy = Column(Text, nullable=True)
    notifyType = Column(Text, nullable=True)
    
    incentives = Column(Text, nullable=True)
    language = Column(Text, nullable=True)
    reOfferNotifyNo = Column(Text, nullable=True)
    reOfferNotifyVersion = Column(Text, nullable=True)
    note = Column(Text, nullable=True)
    reOfferNotifyId = Column(Text, nullable=True)
    shoppingAgencyCode = Column(Text, nullable=True)
    additionalChoise = Column(Text, nullable=True)
    additionalPrice = Column(Float, nullable=True)
    underUnitCode = Column(Text, nullable=True)
    propertySample = Column(Text, nullable=True)
    cdtType = Column(Integer, nullable=True)
    preNotifyNo = Column(Text, nullable=True)
    preNotifyVersion = Column(Text, nullable=True)
    preNotifyId = Column(Text, nullable=True)
    
    isMedicine = Column(Boolean, nullable=True)
    isRented = Column(Boolean, nullable=True)
    
    mixBidField = Column(Text, nullable=True)
    isMultiLot = Column(Boolean, nullable=True)
    workType = Column(Text, nullable=True)
    
    medicalType = Column(Integer, nullable=True)
    
    receiveLocationEn = Column(Text, nullable=True)
    bidOpenLocationEn = Column(Text, nullable=True)
    bidGuaranteeFormEn = Column(Text, nullable=True)
    baseMedicine = Column(Text, nullable=True)
    isGoods = Column(Boolean, nullable=True)
    originalPublicDate = Column(DateTime, nullable=True)
    deliveryCapability = Column(Text, nullable=True)
    
    DistrictName = Column(Text, nullable=True)
    ProvinceName = Column(Text, nullable=True)
    DistrictID = Column(Integer, ForeignKey(Districts.DistrictID))
    ProvinceID = Column(Integer, ForeignKey(Provinces.ProvinceID))
    
