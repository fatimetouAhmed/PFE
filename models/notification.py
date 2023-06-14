from datetime import datetime
from sqlalchemy import Table,Column,String,Integer,DATETIME,Boolean
from config.db import meta

notifications=Table(
    'notifications',meta,
    Column('id',Integer,primary_key=True),
    Column('content',String(250)),
    Column('date',DATETIME,default=datetime.now),
    Column('is_read',Boolean,default=False),
)