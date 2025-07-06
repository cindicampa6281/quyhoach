import os
import json
from Database.Database import Base
from Database.Database import *
from Models.Districts import Districts
from Models.XaPhuong import XaPhuong
from Models.Provinces import Provinces
import geojson
from shapely.wkt import loads as wkt_loads
from shapely.wkb import loads as load_wkb, dumps as dump_wkb
from shapely.wkb import loads

def bToPolygon(dat):
    polygon = loads(dat.data)
    geojson_polygon = geojson.Feature(geometry=polygon)
    return geojson_polygon["geometry"]["coordinates"]

def load_json_phanloai( input_file ):
    with open(input_file) as json_file:
        json_data = json.load(json_file)
        print(json_data)
        listongcong = []
        sapxep = 1
        toanbodotbien = 0

        for item_district in json_data:
            idpro = item_district["id"] 
            print("____idpro____" + str(idpro))
            district_find =  session.query(Districts).filter(Districts.DistrictID ==  int(idpro) ).first() 
            province_find =  session.query(Provinces).filter(Provinces.ProvinceID ==  district_find.ProvinceID ).first() 
            list_data = []
            polygon_item = ""
            if district_find.multipolygon != None:
                coords = bToPolygon(district_find.multipolygon)
                encrypted_data = coords
                polygon_item = encrypted_data
            list_data_rutgon = []
            list_rut_gon = []
            count = 0
            for item_sukien in item_district["matched_projects"] :
                data_sukien_json = {
                "bidName" : item_sukien["bidName"] ,
                "chudautu": item_sukien["chudautu"] ,
                "createdBy": item_sukien["createdBy"] ,
                "publicDate": item_sukien["publicDate"] ,
                "projectName": item_sukien["projectName"] ,
                "bidCloseDate": item_sukien["bidCloseDate"] ,
                "id_muasamcong": item_sukien["id_muasamcong"] ,
                "tongmuc_dautu": item_sukien["tongmuc_dautu"] ,
                "bidNamePlanNew": item_sukien["bidNamePlanNew"] ,
                "dotbien_hatang": item_sukien["dotbien_hatang"] ,
                "link_muasamcong": item_sukien["link_muasamcong"] ,
                }
                data_rutgon_json = {
                    "bidName" : item_sukien["bidName"] 
                }
                list_data_rutgon.append(data_rutgon_json)
                list_data.append(data_sukien_json)
                count = count + 1
            toanbodotbien = toanbodotbien + count
            data_json = {
                "id_district" : item_district["id"] ,
                "id_province" : province_find.ProvinceID , 
                "name_province" : province_find.ProvinceName , 
                "name_district" : district_find.DistrictName ,
                "list_sukien" : list_data ,
                "so_dot_bien" : count , 
                "thu_tu_sap_xep" : sapxep ,
                "polygon" : polygon_item
            }
            data_json2 = {
                "id_district" : item_district["id"] ,
                "id_province" : province_find.ProvinceID , 
                "name_province" : province_find.ProvinceName , 
                "name_district" : district_find.DistrictName ,
                "list_sukien" : list_data_rutgon ,
                "so_dot_bien" : count ,
                "thu_tu_sap_xep" : sapxep ,
                "ti_le_phan_tram" : float( (count / 49172) * 100 )
            }
            listongcong.append( data_json2 )
            sapxep = sapxep + 1
            with open( str(item_district["id"] ) + ".json" , 'w', encoding='utf-8') as f:
                json.dump( data_json , f, ensure_ascii=False, indent=4)
    with open("sap_xep_theo_huyen.json" , 'w', encoding='utf-8') as f:
                json.dump( { "tongcong" : listongcong , "tongso_dotbien" : toanbodotbien } , f, ensure_ascii=False, indent=4)


def load_json_sap_xep_theo_tinh( input_file ):
    with open(input_file) as json_file:
        json_data = json.load(json_file)
        print(json_data)
        listongcong = []
        
        province_all =  session.query(Provinces).all()
        for item_provin in province_all:
            tongdot_bien_tinh = 0
            list_dotbien_cac_huyen = []
            polygon_item = ""
            if item_provin.multipolygon != None:
                    coords = bToPolygon(item_provin.multipolygon)
                    encrypted_data = coords
                    polygon_item = encrypted_data
            for item_district_json in json_data["tongcong"]:
                id_province = item_district_json["id_province"] 
                if item_provin.ProvinceID == int(id_province) :
                    tongdot_bien_tinh = int( item_district_json["so_dot_bien"] ) + tongdot_bien_tinh
                    list_dotbien_cac_huyen.append( item_district_json )
                
            data_json = { "dot_bien_tinh" : list_dotbien_cac_huyen , 
                             "tongdot_bien_tinh" : tongdot_bien_tinh ,
                              "name_tinh" : item_provin.ProvinceName ,
                               "id_tinh" : item_provin.ProvinceID ,
                               "polygon" : polygon_item }
            with open( "tinh_" + str(item_provin.ProvinceID ) + ".json" , 'w', encoding='utf-8') as f:
                json.dump( data_json , f, ensure_ascii=False, indent=4)
            listongcong.append( data_json )
        with open("sap_xep_theo_tinh.json" , 'w', encoding='utf-8') as f:
                json.dump( { "tongcong" : listongcong  } , f, ensure_ascii=False, indent=4)

def load_json_sap_xep_tyle_huyen_trongtinh( input_file ):
    with open(input_file) as json_file:
            json_data = json.load(json_file)
            # print(json_data)
            listongcong = []
            for item_tinh  in  json_data["tongcong"] :
                tongdot_bien_tinh = item_tinh["tongdot_bien_tinh"]
                list_dotbien = []
                list_dotbien_xoa = []
                for item_huyen in item_tinh["dot_bien_tinh"] :
                    so_dot_bien_huyen = item_huyen["so_dot_bien"]   
                    phantram = (so_dot_bien_huyen / tongdot_bien_tinh)  * 100 
                    item_huyen["ti_le_phan_tram"] =  phantram  
                    item_huyen_xoa = item_huyen 
                    item_huyen_xoa["list_sukien"] = []
                    district_find =  session.query(Districts).filter(Districts.DistrictID ==  int(item_huyen[ "id_district"] ) ).first() 
                    polygon_item = ""
                    if district_find.multipolygon != None:
                        coords = bToPolygon(district_find.multipolygon)
                        encrypted_data = coords
                        polygon_item = encrypted_data
                    item_huyen["polygon_huyen"] = polygon_item
                    list_dotbien.append( item_huyen ) 
                    list_dotbien_xoa.append ( item_huyen_xoa )
                    
                lines_tong = sorted( list_dotbien , key=lambda k: k.get("so_dot_bien", 0), reverse=True)
                offset_tile = 255 / ( len( list_dotbien ) + 2 )
                phantu = 0
                for item_phantu in lines_tong:
                    color = {"red" : 255 - phantu * offset_tile , 
                     "green" : 0 + phantu * offset_tile ,
                     "blue" : 0 + phantu * 2 }
                    item_phantu["color"] = color
                    phantu = phantu + 1  
                #_______________________________________
                lines_pro_tong = sorted( list_dotbien_xoa , key=lambda k: k.get("so_dot_bien", 0), reverse=True)
                offset_tile = 255 / ( len( list_dotbien_xoa ) + 2 )
                phantu = 0
                for item_phantu in lines_pro_tong:
                    color = {"red" : 255 - phantu * offset_tile , 
                     "green" : 0 + phantu * offset_tile ,
                     "blue" : 0 + phantu * 2 }
                    item_phantu["color"] = color
                    phantu = phantu + 1  
                item_tinh_xoa = item_tinh
                item_tinh_xoa["dot_bien_tinh"] = list_dotbien_xoa
                listongcong.append ( item_tinh_xoa )
                with open( "tinh_" + str( item_tinh["id_tinh"] ) + ".json" , 'w', encoding='utf-8') as f:
                    json.dump( item_tinh , f, ensure_ascii=False, indent=4)
            tong_sapxep = sorted( listongcong , key=lambda k: k.get("tongdot_bien_tinh", 0), reverse=True)
            offset_tile = 255 / ( len( listongcong ) + 2 )
            phantu = 0
            for item_phantu in tong_sapxep:
                    color = {"red" : 255 - phantu * offset_tile , 
                     "green" : 0 + phantu * offset_tile ,
                     "blue" : 0 + phantu * 2 }
                    item_phantu["color"] = color
                    phantu = phantu + 1  
            with open( "sap_xep_tinh.json" , 'w', encoding='utf-8') as f:
                json.dump( { "cac_tinh" : tong_sapxep  } , f , ensure_ascii = False, indent = 4 )
            with open( "sapxep_chitiet.json" , 'w', encoding='utf-8') as f:
                json.dump( { "tongcong" : listongcong  } , f , ensure_ascii = False, indent = 4 )

# Thực hiện xử lý và ghi file
# load_json_phanloai( "/home/landinvest/Desktop/sap_xep_dot_bien_ha_tang/output_construction_projects.json" )
# load_json_sap_xep_theo_tinh( "/home/landinvest/Desktop/sap_xep_dot_bien_ha_tang/sap_xep_theo_huyen.json" )

load_json_sap_xep_tyle_huyen_trongtinh("/home/landinvest/Desktop/sap_xep_dot_bien_ha_tang/theo_tinh/sap_xep_theo_tinh.json")