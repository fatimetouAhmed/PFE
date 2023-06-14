from fastapi import APIRouter
from config.db import con
from models.notification import notifications 
from schemas.notification import Notification

notification_router=APIRouter()
@notification_router.get("/")
async def read_data():
    query = notifications.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"content": row.content,"date": row.date,"is_read": row.is_read}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(notifications.select().fetchall())

@notification_router.get("/{id}")
async def read_data_by_id(id:int):
    query = notifications.select().where(notifications.c.id==id)
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"content": row.content,"date": row.date,"is_read": row.is_read}   # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(notifications.select().where(notifications.c.id==id)).fetchall()


@notification_router.post("/")
async def write_data(notification:Notification):

    con.execute(notifications.insert().values(
        content=notification.content,
        date=notification.date,
        is_read=notification.is_read
        ))
    return await read_data()



@notification_router.put("/{id}")
async def update_data(id:int,notification:Notification):
    con.execute(notifications.update().values(
        content=notification.content,
        date=notification.date,
        is_read=notification.is_read
    ).where(notifications.c.id==id))
    return await read_data()

@notification_router.delete("/{id}")
async def delete_data(id:int):
    con.execute(notifications.delete().where(notifications.c.id==id))
    return await read_data()
