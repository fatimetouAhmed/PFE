from sqlalchemy import select, join, alias
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from fastapi import APIRouter
from config.db import con
from models.etudiermat import etudiermats
from models.etudiermat import Etudiant
from models.etudiermat import Matiere
# from models.etudiant import Etudiant
# from models.matiere import Matiere
from schemas.etudiermat import Etudiermat

etudiermat_router=APIRouter()
@etudiermat_router.get("/")
async def read_data():
    query =etudiermats.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                  "id_etu": row.id_etu,
                  "id_mat": row.id_mat,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(etudiermats.select().fetchall())

@etudiermat_router.get("/{id}")
async def read_data_by_id(id:int):
    query =etudiermats.select().where(etudiermats.c.id==id)
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                  "id_etu": row.id_etu,
                  "id_mat": row.id_mat,}   # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(etudiermats.select().where(etudiermats.c.id==id)).fetchall()


@etudiermat_router.post("/")
async def write_data(etudiermat:Etudiermat):

    con.execute(etudiermats.insert().values(

        id_etu=etudiermat.id_etu,
        id_mat=etudiermat.id_mat,
        ))
    return await read_data()



@etudiermat_router.put("/{id}")
async def update_data(id:int,etudiermat:Etudiermat):
    con.execute(etudiermats.update().values(
        id_etu=etudiermat.id_etu,
        id_mat=etudiermat.id_mat,
    ).where(etudiermats.c.id==id))
    return await read_data()

@etudiermat_router.delete("/{id}")
async def delete_data(id:int):
    con.execute(etudiermats.delete().where(etudiermats.c.id==id))
    return await read_data()
