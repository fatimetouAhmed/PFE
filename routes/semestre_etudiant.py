from sqlalchemy import select, join, alias
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from fastapi import APIRouter
from config.db import con
from models.semestre_etudiant import semestre_etudiants
from models.semestre_etudiant import Etudiants
from models.semestre_etudiant import Semestres
# from models.etudiant import Etudiant
# from models.matiere import Matiere
from schemas.semestre_etudiant import Semestre_etudiant

semestre_etudiant_router=APIRouter()
@semestre_etudiant_router.get("/")
async def read_data():
    query =semestre_etudiants.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                  "id_etu": row.id_etu,
                  "id_sem": row.id_sem,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(semestre_etudiants.select().fetchall())

@semestre_etudiant_router.get("/{id}")
async def read_data_by_id(id:int):
    query =semestre_etudiants.select().where(semestre_etudiants.c.id==id)
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                  "id_etu": row.id_etu,
                  "id_sem": row.id_sem,}   # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(semestre_etudiants.select().where(semestre_etudiants.c.id==id)).fetchall()


@semestre_etudiant_router.post("/")
async def write_data(semestre_etudiant:Semestre_etudiant):

    con.execute(semestre_etudiants.insert().values(

        id_etu=semestre_etudiant.id_etu,
        id_sem=semestre_etudiant.id_sem,
        ))
    return await read_data()



@semestre_etudiant_router.put("/{id}")
async def update_data(id:int,semestre_etudiant:Semestre_etudiant):
    con.execute(semestre_etudiants.update().values(
        id_etu=semestre_etudiant.id_etu,
        id_sem=semestre_etudiant.id_sem,
    ).where(semestre_etudiants.c.id==id))
    return await read_data()

@semestre_etudiant_router.delete("/{id}")
async def delete_data(id:int):
    con.execute(semestre_etudiants.delete().where(semestre_etudiants.c.id==id))
    return await read_data()
