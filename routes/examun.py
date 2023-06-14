from sqlalchemy import select, join, alias
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from fastapi import APIRouter
from config.db import con
from models.examun import examuns
# from models.examun import Salle
# from models.examun import Matieres
# from models.etudiant import Etudiant
# from models.matiere import Matiere
from schemas.examun import Examun

examun_router=APIRouter()
@examun_router.get("/")
async def read_data():
    query =examuns.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                 "type": row.type,
                  "heure_deb": row.heure_deb,
                  "heure_fin": row.heure_fin,
                  "id_sal": row.id_sal,
                  "id_mat": row.id_mat,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(examuns.select().fetchall())

@examun_router.get("/{id}")
async def read_data_by_id(id:int):
    query =examuns.select().where(examuns.c.id==id)
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {
                  "type": row.type,
                  "heure_deb": row.heure_deb,
                  "heure_fin": row.heure_fin,
                  "id_sal": row.id_sal,
                  "id_mat": row.id_mat,}   # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(examuns.select().where(examuns.c.id==id)).fetchall()


@examun_router.post("/")
async def write_data(examun:Examun):

    con.execute(examuns.insert().values(
        type=examun.type,
        heure_deb=examun.heure_deb,
        heure_fin=examun.heure_fin,
        id_sal=examun.id_sal,
        id_mat=examun.id_mat,
        ))
    return await read_data()



@examun_router.put("/{id}")
async def update_data(id:int,examun:Examun):
    con.execute(examuns.update().values(
        type=examun.type,
        heure_deb=examun.heure_deb,
        heure_fin=examun.heure_fin,
        id_sal=examun.id_sal,
        id_mat=examun.id_mat,
    ).where(examuns.c.id==id))
    return await read_data()

@examun_router.delete("/{id}")
async def delete_data(id:int):
    con.execute(examuns.delete().where(examuns.c.id==id))
    return await read_data()
