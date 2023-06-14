from sqlalchemy import Table,Column,String,Integer
from config.db import meta

users=Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('nom',String(250)),
)