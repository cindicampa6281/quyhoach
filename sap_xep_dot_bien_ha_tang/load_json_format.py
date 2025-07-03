import os
import json
from Database.Database import Base
from Database.Database import *
from Models.Districts import Districts
from Models.XaPhuong import XaPhuong
from Models.Provinces import Provinces

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
                "list_sukien" : list_data ,
                "so_dot_bien" : count
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
    with open("tongket.json" , 'w', encoding='utf-8') as f:
                json.dump( { "tongcong" : listongcong , "tongso_dotbien" : toanbodotbien } , f, ensure_ascii=False, indent=4)

# Thực hiện xử lý và ghi file
load_json_phanloai( "/home/landinvest/Desktop/dobien_hatang/output_construction_projects.json" )