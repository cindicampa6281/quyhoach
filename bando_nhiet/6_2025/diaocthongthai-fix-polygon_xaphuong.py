from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime, timedelta
import json
import os
import signal
import subprocess
import re
from bs4 import Tag
from shapely.geometry import shape
from shapely.geometry.polygon import Polygon
import ast

# import Models.Provinces

from Database.Database import *
from Models import Districts2, Provinces2, Districts, Provinces, ls_giadat
from sqlalchemy import func

from shapely.wkb import loads as load_wkb, dumps as dump_wkb
from shapely.ops import unary_union
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import shape
from shapely.geometry import Point
from shapely.geometry import Polygon, MultiPolygon
import shapely



from sqlalchemy import asc, desc, or_, and_, union, select, intersect
from sqlalchemy import func, and_, or_, not_

from Models.xa_phuong2 import xa_phuong2
from Models.ls_giadat import ls_giadat
from Models.historychartdangcap import historychartdangcap
from Models.gia_dat_xa_phuong import gia_dat_xa_phuong
from datetime import datetime
from Models.Districts import Districts
from Models.XaPhuong import XaPhuong
from Models.bando_nhiet_district_month import bando_nhiet_district_month
from Models.Provinces import Provinces
import geojson

from shapely.wkb import loads 
from shapely import wkb
from shapely.geometry import mapping
import json
from shapely.wkt import loads as wkt_loads

def bToPolygon(dat):
    # print("_____DU_LIEU_DATA________" + str(dat.data))
    polygon = loads(dat.data)
    geojson_polygon = geojson.Feature(geometry=polygon)
    return geojson_polygon["geometry"]["coordinates"]

def load_du_lieu():
        list_data = []
        xaphuong_all =  session.query(XaPhuong).all() 
        list_polygon = []
        for item_xaphuong in xaphuong_all:
            polygon_item = {}
            if  item_xaphuong.polygon_diocthongthai != None:
                array_xoa1lan = []
            
                item_xaphuong.polygon_diocthongthai  = item_xaphuong.polygon_diocthongthai.replace("20.9971714019775]]]," , "20.9971714019775]]]]")
                if item_xaphuong.polygon_diocthongthai[-1] == ",":
                    stringpro = item_xaphuong.polygon_diocthongthai
                    print("__SSSSS__" + str(len(item_xaphuong.polygon_diocthongthai) - 1 ) + "___" + stringpro)
                    stringpro = stringpro.replace("]]]," , "]]]]")
                    item_xaphuong.polygon_diocthongthai = stringpro
                    print("__________item_xaphuong.____" + item_xaphuong.WandName + "__________" + item_xaphuong.polygon_diocthongthai)
                    session.commit()
                # jsonData = json.loads( item_xaphuong.polygon_diocthongthai )
                # for item_phantu in jsonData:
                #         for item2 in item_phantu:
                #             for item3 in item2:
                #                 if float (item3[0] ) < float (item3[1] ) :
                #                     temp1 = item3[1]
                #                     temp2 = item3[0]
                #                     item3[0] = temp1
                #                     item3[1] = temp2
                #             array_xoa1lan.append(item2)
                # polygon_item["polygon"] =        array_xoa1lan
                # polygon_item["WandID"]  = item_xaphuong.WandID
                # polygon_item["WandName"]  = item_xaphuong.WandName
                # list_polygon.append(polygon_item)
            else:
                if item_xaphuong.multipolygon != None:
                    if item_xaphuong.polygon2 != None:
                    
                        array_xoa1lan = []
                        jsonData = json.loads(item_xaphuong.polygon2)
                        for item_phantu in jsonData:
                            for item2 in item_phantu:
                                for item3 in item2:
                                    if item3[0] < item3[1]:
                                        temp1 = item3[1]
                                        temp2 = item3[0]
                                        item3[0] = temp1
                                        item3[1] = temp2
                                array_xoa1lan.append(item2)
                        polygon_item["polygon"] =        array_xoa1lan
                    else:
                        print("________item_xaphuong___" + str(item_xaphuong.WandName ))
                        if item_xaphuong.multipolygon != None:
                            coords = bToPolygon(item_xaphuong.multipolygon)
                            polygon_item = {}
                            encrypted_data = coords
                            polygon_item["polygon"] = encrypted_data
                    polygon_item["WandID"]  = item_xaphuong.WandID
                    polygon_item["WandName"]  = item_xaphuong.WandName
                    list_polygon.append(polygon_item)
                else: 
                    print("_________KHONGCO_POLYGON______"+ str(item_xaphuong.WandName))

        list_data.append(jsonData)
        with open( "jsondata.json" , 'w', encoding='utf-8') as f:
            json.dump( jsonData , f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    load_du_lieu()