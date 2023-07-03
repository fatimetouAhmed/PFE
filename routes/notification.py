from fastapi import APIRouter,Depends
from auth.authConfig import create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
from models.notification import notifications 
from schemas.notification import Notification

notification_router=APIRouter()
@notification_router.get("/")
async def read_data(user: User = Depends(check_Adminpermissions)):
    query = notifications.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"content": row.content,"date": row.date,"is_read": row.is_read}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(notifications.select().fetchall())

@notification_router.get("/{id}")
async def read_data_by_id(id:int,user: User = Depends(check_Adminpermissions)):
    query = notifications.select().where(notifications.c.id==id)
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"content": row.content,"date": row.date,"is_read": row.is_read}   # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(notifications.select().where(notifications.c.id==id)).fetchall()


@notification_router.post("/")
async def write_data(notification:Notification,user: User = Depends(check_Adminpermissions)):

    con.execute(notifications.insert().values(
        content=notification.content,
        date=notification.date,
        is_read=notification.is_read
        ))
    return await read_data()



@notification_router.put("/{id}")
async def update_data(id:int,notification:Notification,user: User = Depends(check_Adminpermissions)):
    con.execute(notifications.update().values(
        content=notification.content,
        date=notification.date,
        is_read=notification.is_read
    ).where(notifications.c.id==id))
    return await read_data()

@notification_router.delete("/{id}")
async def delete_data(id:int,user: User = Depends(check_Adminpermissions)):
    con.execute(notifications.delete().where(notifications.c.id==id))
    return await read_data()
