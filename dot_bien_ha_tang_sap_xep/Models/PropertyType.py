from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Text
from PolygonCrawl.Database.Database import *


# from Models.Districts import *
# from Models.Provinces import *
import requests
import json


class PropertyType(Base):
    __tablename__ = "PropertyType"
    PropertyTypeID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(250), unique=True, nullable=False)
    Description = Column(String(250), unique=True, nullable=True)
    

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    res2 = requests.get("https://dgts.moj.gov.vn/common/getListPropertyType")
    html = res2.text
    if res2.status_code == 200:
        try:
            json_data = json.loads(html)
            for data in json_data:
                # print("meo m be")
                dataToAdd = PropertyType(
                    Name = data["name"],
                    Description = data["des"]
                )
                session.add(dataToAdd)
                session.commit()
        except Exception as e:
            print(e)
            pass
            