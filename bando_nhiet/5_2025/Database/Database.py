from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, MetaData
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


#  user='phpmyadmin',
#             password='Sonhehe89!',
#             database='landinvest',

# Tạo kết nối đến cơ sở dữ liệu MySQL
engine = create_engine('mysql+pymysql://phpmyadmin:Sonhehe89!@localhost/landinvest?charset=utf8mb4')

# Tạo một session để thao tác với cơ sở dữ liệu
Session = sessionmaker(bind=engine)
session = Session()

# Định nghĩa một Base cho các lớp ánh xạ đối tượng
Base = declarative_base()

# Chạy hàm này để tạo các bảng nếu chưa tồn tại
# Base.metadata.create_all(engine)
metadata = MetaData()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
