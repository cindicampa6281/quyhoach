import mysql.connector
import unicodedata
import re
import json

connection = mysql.connector.connect(
                    host="localhost",
                    user = 'phpmyadmin',
                    password= 'Sonhehe89!',
                    database= 'landinvest' ,
                    port=3306,
                )
def bang_gia_dat_province(DistrictId , page):
    limit = 500
    if limit == None  or limit == "" :
        limit = 50
    else:
        limit = int(limit)
    offset = (int(page) - 1) * limit
    dulieutrave = []
    try:
                
                cursor = connection.cursor()
                query = "SELECT * FROM `GiaDatTVPL` WHERE DistrictId = %s"
                param = (DistrictId,)
                cursor.execute(query, param)
                tong_so_page = cursor.fetchall()
                tong_phantu = len(tong_so_page)
                total_page = tong_phantu / limit
                offset = (int(page) - 1) * limit
                print("__________total_page___"+str(total_page))
                
                cursor = connection.cursor()
                stringExe = "SELECT * FROM `GiaDatTVPL` WHERE DistrictId = %s " + " ORDER BY VT1 DESC LIMIT "  + str(limit) +  " OFFSET " + str(offset)
                cursor.execute(stringExe , ( DistrictId , ))
                bang_giadat_all = cursor.fetchall()
                # cursor.close()
                # connection.close()
                print("___DistrictId__"+str(DistrictId))
                for item in bang_giadat_all:
                        item_json = {
                            "id": item[0],
                            "DistrictName": item[9] ,
                            "WardName": item[7] ,
                            # "WardId": item.WardId,
                            "vi_tri": [ { "VT1" : item[1] }, 
                                        { "VT2": item[2] },
                                        { "VT3": item[3]  },
                                        { "VT4": item[4]  },
                                        { "VT5": item[5]  } ] , 
                            "Type": item[6] ,
                            "RoadName": item[7]  ,
                            "FromTo": item[8]  ,
                            "DistrictId": item[9]  ,
                            "ProvinceId": item[10]  ,
                            "CreateAt": str( item[11] )  ,
                            "xa_phuong_id":item[12]   ,
                        }                    
                        dulieutrave.append(item_json)
                data_save = { "giatri" : dulieutrave ,
                             "so_trang" : total_page }
                name = str(DistrictId) + "_page_" + str(page) + ".json"
                with open( name , 'w', encoding='utf-8') as f:
                    json.dump( data_save , f, ensure_ascii=False, indent=4)
                total_page = int( total_page + 1 )
                return  total_page
    except Exception as e:
        print(e)
        return 0

if __name__ == "__main__":
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM `Districts`"
        param = ()
        cursor.execute(query, param)
        tong_district = cursor.fetchall()
        
        for item_district in tong_district:  
            all_page_1_district = 1
            item_page = 1
            while ( True ):
                if item_page > all_page_1_district :
                     break
                print(str( item_page) + "___" + str( all_page_1_district ) + "___item_district__" + str( item_district[ 0 ] ))
                all_page_1_district = bang_gia_dat_province( item_district[ 0 ] , item_page )
                item_page = item_page + 1
                
    finally:
        print("___hoan thanh___")