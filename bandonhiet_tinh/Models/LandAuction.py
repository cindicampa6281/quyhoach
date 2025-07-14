from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from Database.Database import Base


from Models.Districts import *
from Models.Provinces import *

class LandAuction(Base):
    def update(self, **kwargs):
        for key, value in kwargs.items():
            try:
                setattr(self, key, value)
            except Exception as e:
                print(e)
                
    __tablename__ = 'LandAuction'
    auPropertyInfoId = Column(Integer, primary_key=True, autoincrement=True)
    
    propertyAmount = Column(Text, nullable=True)
    detail = Column(Text, nullable=True)
    propertyQuality = Column(Text, nullable=True)
    depositUnit = Column(Integer, nullable=True)
    propertyTypeId = Column(Integer, nullable=True)
    propertyTypeName = Column(Text, nullable=True)
    
    
    fileCost = Column(Float, nullable=True)
    strPropertyStartPrice = Column(Text, nullable=True)
    strDeposit = Column(Text, nullable=True)
    strFileCost = Column(Text, nullable=True)
    
    auctionInfoId = Column(Integer, ForeignKey("LandAuctionId.id"), nullable=True)
    
    Title = Column(Text, nullable=True)
    OpenPrice = Column(Float, nullable=True) #OpenPrice propertyStartPrice
    DepositPrice = Column(Float, nullable=True) # deposit

    # DistrictName = Column(Text, nullable=True)
    # ProvinceName = Column(Text, nullable=True)
    DistrictID = Column(Integer, ForeignKey(Districts.DistrictID))
    ProvinceID = Column(Integer, ForeignKey(Provinces.ProvinceID))
    
    
    NameProperty = Column(Text, nullable=True) #NameProperty propertyName
    AddressProperty = Column(Text, nullable=True) #AddressProperty propertyPlace
    AuctionUrl = Column(Text, nullable=True)
    NamePropertyOwner = Column(Text, nullable=True)
    AddressPropertyOwner = Column(Text, nullable=True)
    NameAuctionHouse = Column(Text, nullable=True)
    AddressAuctionHouse = Column(Text, nullable=True)
    PhoneNumberAuctionHouse = Column(Text, nullable=True)
    AuctionAddress = Column(Text, nullable=True)
    EventSchedule = Column(DateTime, nullable=True)  # Store as datetime
    RegistrationStartTime = Column(DateTime, nullable=True)
    RegistrationEndTime = Column(DateTime, nullable=True)
    DepositPaymentStartTime = Column(DateTime, nullable=True)
    DepositPaymentEndTime = Column(DateTime, nullable=True)
    Description = Column(Text, nullable=True)
    
    longitude = Column(Text, nullable=True)
    latitude = Column(Text, nullable=True)