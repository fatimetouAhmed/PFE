from sqlalchemy import select, join, alias
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from fastapi import APIRouter
from config.db import con
from models.surveillance import surveillances
from models.surveillance import Surveillants
from models.surveillance import Salles
# from models.etudiant import Etudiant
# from models.matiere import Matiere
from schemas.surveillance import Surveillance

surveillance_router=APIRouter()
@surveillance_router.get("/")
async def read_data():
    query =surveillances.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                  "date_debut": row.date_debut,
                  "date_fin": row.date_fin,
                  "surveillant_id ": row.surveillant_id ,
                  "salle_id": row.salle_id,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(surveillances.select().fetchall())

@surveillance_router.get("/{id}")
async def read_data_by_id(id:int):
    query =surveillances.select().where(surveillances.c.id==id)
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                   "date_debut": row.date_debut,
                  "date_fin": row.date_fin,
                  "surveillant_id": row.surveillant_id ,
                  "salle_id": row.salle_id,}   # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(surveillances.select().where(surveillances.c.id==id)).fetchall()


@surveillance_router.post("/")
async def write_data(surveillance:Surveillance):

    con.execute(surveillances.insert().values(

        date_debut=surveillance.date_debut,
        date_fin=surveillance.date_fin,     
        surveillant_id=surveillance.surveillant_id,
        salle_id=surveillance.salle_id,
        ))
    return await read_data()



@surveillance_router.put("/{id}")
async def update_data(id:int,surveillance:Surveillance):
    con.execute(surveillances.update().values(
        date_debut=surveillance.date_debut,
        date_fin=surveillance.date_fin,     
        surveillant_id=surveillance.surveillant_id,
        salle_id=surveillance.salle_id,
    ).where(surveillances.c.id==id))
    return await read_data()

@surveillance_router.delete("/{id}")
async def delete_data(id:int):
    con.execute(surveillances.delete().where(surveillances.c.id==id))
    return await read_data()
