from sqlalchemy import create_engine,MetaData
engine=create_engine("mysql+pymysql://root@localhost:3306/db_devmobile")
meta=MetaData()
con=engine.connect()