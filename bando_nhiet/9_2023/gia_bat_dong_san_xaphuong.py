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

import ast

# import Models.Provinces
from Models import XaPhuong

from Database.Database import *
from Models import Districts2, Provinces2, Districts, Provinces, ls_giadat
from sqlalchemy import func

from shapely.wkb import loads as load_wkb, dumps as dump_wkb
from shapely.ops import unary_union
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import shape
from shapely.geometry import Point
from shapely.geometry import Polygon, MultiPolygon

from shapely.wkt import loads as wkt_loads

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


list_data = []
def bToPolygon(dat):
    polygon = loads(dat.data)
    geojson_polygon = geojson.Feature(geometry=polygon)
    return geojson_polygon["geometry"]["coordinates"]

def get_lich_su_gia_dat_district(DistrictID,month,year , district_name):
    list_lich_sugia_chungcu = []
    list_lich_sugia_bietthu = []
    list_lich_sugia_thocu = []
    list_lich_sugia_shophouse = []
    try:
        date_time_moc = datetime(int(year), 1, int(month))
        # session.query(Districts).filter.all()
        xa_phuong_all =  session.query(XaPhuong).filter(XaPhuong.DistrictID == DistrictID ).all() 
        tong_so_phuong_co_gia_chungcu  = 0
        tong_so_phuong_co_gia_bietthu  = 0
        tong_so_phuong_co_gia_thocu  = 0
        tong_so_phuong_co_gia_shophouse = 0
        for item_xa_phuong in xa_phuong_all:
            if item_xa_phuong.WandID != None:
                bds_lich_su_xaphuong_chungcu =  session.query(ls_giadat).filter(  and_(item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            ls_giadat.type == "Chung cư" ,
                                                            ls_giadat.HistoryID != None ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%') )        )  ) ).all()
                if bds_lich_su_xaphuong_chungcu != None:
                    for item_lichsu in bds_lich_su_xaphuong_chungcu:
                        item_history =   session.query(historychartdangcap).filter( and_(historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc  ) ).first()
                        if item_history != None:
                            tong_so_phuong_co_gia_chungcu = tong_so_phuong_co_gia_chungcu + 1
                            data_hist = {
                                "xaphuong_id" : item_lichsu.WandID ,
                                "name_xaphuong" : item_lichsu.ward ,
                                "price" : item_lichsu.price ,
                                # "description": item_lichsu.description ,
                                "type" : item_lichsu.type ,
                                "max" : item_history.max ,
                                "avg" : int(item_history.avg) ,
                                "min": item_history.min ,
                            }
                            print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                            list_lich_sugia_chungcu.append(data_hist)
                            
                            break
                else:
                    for item_time in  range(1,12):
                        if month >= item_time:
                            date_time_moc = datetime(int(year), item_time, int(month))
                            bds_lich_su_xaphuong_chungcu =  session.query(ls_giadat).filter(  and_(item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            ls_giadat.type == "Chung cư" ,
                                                            ls_giadat.HistoryID != None  ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%'))  )         )).all()
                            if bds_lich_su_xaphuong_chungcu != None:
                                for item_lichsu in bds_lich_su_xaphuong_chungcu:
                                    item_history =   session.query(historychartdangcap).filter( and_( historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc ) ).first()
                                    if item_history != None:
                                        tong_so_phuong_co_gia_chungcu = tong_so_phuong_co_gia_chungcu + 1
                                        data_hist = {
                                            "xaphuong_id" : item_lichsu.WandID ,
                                            "name_xaphuong" : item_lichsu.ward ,
                                            "price" : item_lichsu.price ,
                                            # "description": item_lichsu.description ,
                                            "type" : item_lichsu.type ,
                                            "max" : item_history.max ,
                                            "avg" : int(item_history.avg) ,
                                            "min": item_history.min ,
                                        }
                                        print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                                        list_lich_sugia_chungcu.append(data_hist)
                            
                                        break
                                break
                #______________________________________________________________________________________________________________________
                bds_lich_su_xaphuong_bietthu =   session.query(ls_giadat).filter(  and_( item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            ls_giadat.type == "Biệt thự" ,
                                                            ls_giadat.HistoryID != None ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%'))  )  ) ).all()
                if bds_lich_su_xaphuong_bietthu != None:
                    for item_lichsu in bds_lich_su_xaphuong_bietthu:
                        item_history =   session.query(historychartdangcap).filter(and_( historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc ) ).first()
                        if item_history != None:
                            tong_so_phuong_co_gia_bietthu = tong_so_phuong_co_gia_bietthu + 1
                            data_hist = {
                                "xaphuong_id" : item_lichsu.WandID ,
                                "name_xaphuong" : item_lichsu.ward ,
                                "price" : item_lichsu.price ,
                                # "description": item_lichsu.description ,
                                "type" : item_lichsu.type ,
                                "max" : item_history.max ,
                                "avg" : int(item_history.avg) ,
                                "min": item_history.min ,
                            }
                            print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                            list_lich_sugia_bietthu.append(data_hist)
                            
                            break
                else:
                    for item_time in  range(1,12):
                        if month >= item_time:
                            date_time_moc = datetime(int(year), item_time, int(month))
                            bds_lich_su_xaphuong_bietthu =   session.query(ls_giadat).filter( and_( item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            ls_giadat.type == "Biệt thự" ,
                                                            ls_giadat.HistoryID != None ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%'))  )   ) ).all()
                            if bds_lich_su_xaphuong_bietthu != None:
                                for item_lichsu in bds_lich_su_xaphuong_bietthu:
                                    item_history =   session.query(historychartdangcap).filter( and_( historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc ) ).first()
                                    if item_history != None:
                                        tong_so_phuong_co_gia_bietthu = tong_so_phuong_co_gia_bietthu + 1
                                        data_hist = {
                                            "xaphuong_id" : item_lichsu.WandID ,
                                            "name_xaphuong" : item_lichsu.ward ,
                                            "price" : item_lichsu.price ,
                                            # "description": item_lichsu.description ,
                                            "type" : item_lichsu.type ,
                                            "max" : item_history.max ,
                                            "avg" : int(item_history.avg) ,
                                            "min": item_history.min ,
                                        }
                                        print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                                        list_lich_sugia_bietthu.append(data_hist)
                            
                                        break
                                break
                #______________________________________________________________________________________________________________________
                bds_lich_su_xaphuong_thocu =   session.query(ls_giadat).filter( and_( item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            or_(ls_giadat.type == "Đất đấu giá/Đất thổ cư" ,
                                                            ls_giadat.type == "Nhà riêng" ) ,
                                                            ls_giadat.HistoryID != None ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%'))  )   )).all()
                if bds_lich_su_xaphuong_thocu != None:
                    for item_lichsu in bds_lich_su_xaphuong_thocu:
                        item_history =   session.query(historychartdangcap).filter( and_( historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc ) ).first()
                        if item_history != None:
                            tong_so_phuong_co_gia_thocu = tong_so_phuong_co_gia_thocu + 1
                            data_hist = {
                                "xaphuong_id" : item_lichsu.WandID ,
                                "name_xaphuong" : item_lichsu.ward ,
                                "price" : item_lichsu.price ,
                                # "description": item_lichsu.description ,
                                "type" : item_lichsu.type ,
                                "max" : item_history.max ,
                                "avg" : int(item_history.avg) ,
                                "min": item_history.min ,
                            }
                            print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                            list_lich_sugia_thocu.append(data_hist)
                            
                            break
                else:
                    for item_time in  range(1,12):
                        if month >= item_time:
                            date_time_moc = datetime(int(year), item_time, int(month))
                            bds_lich_su_xaphuong_thocu =   session.query(ls_giadat).filter( and_(item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            or_(ls_giadat.type == "Đất đấu giá/Đất thổ cư" ,
                                                            ls_giadat.type == "Nhà riêng" ) ,
                                                            ls_giadat.HistoryID != None ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%'))  )     ) ).all()
                            if bds_lich_su_xaphuong_thocu != None:
                                for item_lichsu in bds_lich_su_xaphuong_thocu:
                                    item_history =   session.query(historychartdangcap).filter( and_( historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc  ) ).first()
                                    if item_history != None:
                                        tong_so_phuong_co_gia_thocu = tong_so_phuong_co_gia_thocu + 1
                                        data_hist = {
                                            "xaphuong_id" : item_lichsu.WandID ,
                                            "name_xaphuong" : item_lichsu.ward ,
                                            "price" : item_lichsu.price ,
                                            # "description": item_lichsu.description ,
                                            "type" : item_lichsu.type ,
                                            "max" : item_history.max ,
                                            "avg" : int(item_history.avg) ,
                                            "min": item_history.min ,
                                        }
                                        print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                                        list_lich_sugia_thocu.append(data_hist)
                            
                                        break
                                break
                #______________________________________________________________________________________________________________________
                bds_lich_su_xaphuong_shophouse =  session.query(ls_giadat).filter(  item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            or_(ls_giadat.type == "Shophouse" ,ls_giadat.type == "nha-mat-pho" ),
                                                            ls_giadat.HistoryID != None  ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%'))  )      ).all()
                if bds_lich_su_xaphuong_shophouse != None:
                    for item_lichsu in bds_lich_su_xaphuong_shophouse:
                        item_history =   session.query(historychartdangcap).filter( and_( historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc  ) ).first()
                        if item_history != None:
                            tong_so_phuong_co_gia_shophouse = tong_so_phuong_co_gia_shophouse + 1
                            data_hist = {
                                "xaphuong_id" : item_lichsu.WandID ,
                                "name_xaphuong" : item_lichsu.ward ,
                                "price" : item_lichsu.price ,
                                # "description": item_lichsu.description ,
                                "type" : item_lichsu.type ,
                                "max" : item_history.max ,
                                "avg" : int(item_history.avg) ,
                                "min": item_history.min ,
                            }
                            print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                            list_lich_sugia_shophouse.append(data_hist)
                            
                            break
                else:
                    for item_time in  range(1,12):
                        if month >= item_time:
                            date_time_moc = datetime(int(year), item_time, int(month))
                            bds_lich_su_xaphuong_shophouse =  session.query(ls_giadat).filter( and_( item_xa_phuong.WandID == ls_giadat.WandID ,
                                                            or_(ls_giadat.type == "Shophouse" ,ls_giadat.type == "nha-mat-pho" ),
                                                            ls_giadat.HistoryID != None ,    or_(ls_giadat.url.like(func.lower(f'%https://batdongsan.com.vn%') ) , 
                                                                                                 ls_giadat.url.like(func.lower(f'%https://www.nhatot.com%'))  )     ) ).all()
                            if bds_lich_su_xaphuong_shophouse != None:
                                for item_lichsu in bds_lich_su_xaphuong_shophouse:
                                    item_history =   session.query(historychartdangcap).filter( and_( historychartdangcap.HistoryID == item_lichsu.HistoryID ,
                                                                            historychartdangcap.startDate <= date_time_moc , 
                                                                            historychartdangcap.endDate >= date_time_moc  ) ).first()
                                    if item_history != None:
                                        tong_so_phuong_co_gia_shophouse = tong_so_phuong_co_gia_shophouse + 1
                                        data_hist = {
                                            "xaphuong_id" : item_lichsu.WandID ,
                                            "name_xaphuong" : item_lichsu.ward ,
                                            "price" : item_lichsu.price ,
                                            # "description": item_lichsu.description ,
                                            "type" : item_lichsu.type ,
                                            "max" : item_history.max ,
                                            "avg" : int(item_history.avg) ,
                                            "min": item_history.min ,
                                        }
                                        print("_______________________" + item_xa_phuong.WandName+ "______" + str(data_hist))
                                        list_lich_sugia_shophouse.append(data_hist)
                                        break
                                break
                 #______________________________________________________________________________________________________________________               
        #______________________________________________________________________________________________________________________
        lines_shophouse = sorted(list_lich_sugia_shophouse, key=lambda k: k.get('avg', 0), reverse=True)
        offset_shophouse = 255 / ( len(list_lich_sugia_shophouse) + 2 )
        phantu = 0
        for item_phantu in lines_shophouse:
            color = {"red" : 255 - phantu * offset_shophouse , 
                     "green" : 0 + phantu * offset_shophouse ,
                     "blue" : 0 + phantu * 2 }
            item_phantu["color"] = color
            phantu = phantu + 1     
        #____________________________________________________________________________
        # print("_______________________" + str(bando_nhiet_find.chung_cu))
        lines_chung_cu = sorted(list_lich_sugia_chungcu, key=lambda k: k.get('avg', 0), reverse=True)
        offset_chung_cu = 255 / ( len(list_lich_sugia_chungcu) + 2 )
        phantu = 0
        for item_phantu in lines_chung_cu:
            color = {"red" : 255 - phantu * offset_chung_cu , 
                     "green" : 0 + phantu * offset_chung_cu ,
                     "blue" : 0 + phantu * 2 }
            item_phantu["color"] = color
            phantu = phantu + 1   
        #____________________________________________________________________________
        lines_biet_thu = sorted(list_lich_sugia_bietthu, key=lambda k: k.get('avg', 0), reverse=True)
        offset_biet_thu = 255 / ( len( list_lich_sugia_bietthu ) + 2 )
        phantu = 0
        for item_phantu in lines_biet_thu:
            color = {"red" : 255 - phantu * offset_biet_thu , 
                     "green" : 0 + phantu * offset_biet_thu ,
                     "blue" : 0 + phantu * 2 }
            item_phantu["color"] = color
            phantu = phantu + 1  
    #____________________________________________________________________________
        lines_tho_cu = sorted(list_lich_sugia_thocu, key=lambda k: k.get('avg', 0), reverse=True)
        offset_tho_cu = 255 / ( len( list_lich_sugia_thocu ) + 2 )
        phantu = 0
        for item_phantu in lines_tho_cu:
            color = {"red" : 255 - phantu * offset_tho_cu , 
                     "green" : 0 + phantu * offset_tho_cu ,
                     "blue" : 0 + phantu * 2 }
            item_phantu["color"] = color
            phantu = phantu + 1 
        xaphuong_all =  session.query(XaPhuong).filter(XaPhuong.DistrictID == DistrictID  ).all() 
        list_polygon = []
        for item_xaphuong in xaphuong_all:
            polygon_item = {}
            if  item_xaphuong.polygon_diocthongthai != None:
                array_xoa1lan = []
            
                item_xaphuong.polygon_diocthongthai  = item_xaphuong.polygon_diocthongthai.replace("20.9971714019775]]]," , "20.9971714019775]]]]")
                print("__________item_xaphuong.____" + item_xaphuong.WandName + "__________" + item_xaphuong.polygon_diocthongthai)
                jsonData = json.loads( item_xaphuong.polygon_diocthongthai )
                for item_phantu in jsonData:
                        for item2 in item_phantu:
                            for item3 in item2:
                                if float (item3[0] ) < float (item3[1] ) :
                                    temp1 = item3[1]
                                    temp2 = item3[0]
                                    item3[0] = temp1
                                    item3[1] = temp2
                            array_xoa1lan.append(item2)
                polygon_item["polygon"] =        array_xoa1lan
                polygon_item["WandID"]  = item_xaphuong.WandID
                polygon_item["WandName"]  = item_xaphuong.WandName
                list_polygon.append(polygon_item)
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
                        coords = bToPolygon(item_xaphuong.multipolygon)
                        polygon_item = {}
                        encrypted_data = coords
                        polygon_item["polygon"] = encrypted_data
                    polygon_item["WandID"]  = item_xaphuong.WandID
                    polygon_item["WandName"]  = item_xaphuong.WandName
                    list_polygon.append(polygon_item)
                else: 
                    print("_________KHONGCO_POLYGON______"+ str(item_xaphuong.WandName))
        name_file = str(DistrictID) + "_" + str(month) + "_" + str(year) + ".json"
        # district_find =  session.query(Districts).filter(Districts.DistrictID == DistrictID  ).first() 
        jsonData = {"shophouse":lines_shophouse ,
                    "chungcu": lines_chung_cu , 
                    "bietthu" : lines_biet_thu ,
                    "thocu" : lines_tho_cu ,
                    "polygon" : list_polygon , 
                    "ten_huyen" : district_name
                    }
        
        list_data.append(jsonData)
        with open( name_file , 'w', encoding='utf-8') as f:
            json.dump( jsonData , f, ensure_ascii=False, indent=4)
        with open( "tong_toan_bo.json" , 'w', encoding='utf-8') as f:
            json.dump( list_data , f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error: {e}")
        error = "An error occurred " + str(e)
        return {"status": 500, "message": error}
    
if __name__ == "__main__":

    dulieutrave = []
    try:
        list_district = session.query(Districts).all()
        biendem = 0
        for item_district in list_district:
            # if biendem > 601:
                print("________________"+ item_district.DistrictName + "_____" + str(item_district.DistrictID))
                get_lich_su_gia_dat_district(item_district.DistrictID, 9 , 2023 , item_district.DistrictName)
            # biendem = biendem + 1
        
    except Exception as e:
        print(e)
    


