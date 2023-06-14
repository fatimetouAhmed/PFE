from fastapi import APIRouter
from config.db import con
from models.semestre import Semestre
from schemas.semestre import SemestreBase
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from models.semestre_etudiant import Semestres
semestre_router=APIRouter()
@semestre_router.get("/semestre_filiere")
async def semestre_filiere_data():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    semestres = session.query(Semestre).join(Semestre.filieres).all()

    # Parcourir les filières et récupérer leurs départements associés
    results = []
    for semestre in semestres:
        result = {
            "nom": semestre.nom,
            "filieres": {
                "nom": semestre.filieres.nom,
                "description": semestre.filieres.description
            }
        }
        results.append(result)

    return results
@semestre_router.get("/")
async def read_data():
    query = Semestre.__table__.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"nom": row.nom,
                  "id_fil": row.id_fil}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(semestres.select().fetchall())
@semestre_router.get("/etudiants_semestres")
async def semestres_etudiants_data():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les étudiants avec leurs matières
    semestres = session.query(Semestres).options(joinedload(Semestres.semestres_etudiants)).all()

    # Parcourir les étudiants et récupérer leurs matières associées
    results = []
    for semestre in semestres:
        result = {
            "nom": semestre.nom,
            "id_fil": semestre.id_fil,
            "semestres_etudiants": []
        }

        for etudiant in  semestre.semestres_etudiants:
            result["semestres_etudiants"].append({
            "nom": etudiant.nom,
            "prenom": etudiant.prenom,
            "photo": etudiant.photo,
            "genre": etudiant.genre,
            "date_N": etudiant.date_N,
            "lieu_n": etudiant.lieu_n,
            "email": etudiant.email,
            "telephone": etudiant.telephone,
            "nationalité": etudiant.nationalité,
            "date_inscription": etudiant.date_insecription,
            })
        results.append(result)

    return results
@semestre_router.get("/{id}")
async def read_data_by_id(id:int):
    query = Semestre.__table__.select().where(Semestre.__table__.c.id==id)
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"nom": row.nom,
                  "id_fil": row.id_fil}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
    # return con.execute(semestres.select().where(semestres.c.id==id)).fetchall()

@semestre_router.post("/")
async def write_data(semestre:SemestreBase):
    print("nom",semestre.nom)
    con.execute(Semestre.__table__.insert().values(
        nom=semestre.nom,
        id_fil=semestre.id_fil
        ))
    return await read_data()

@semestre_router.put("/{id}")
async def update_data(id:int,semestre:SemestreBase):
    con.execute(Semestre.__table__.update().values(
        nom=semestre.nom,
        id_fil=semestre.id_fil
    ).where(Semestre.__table__.c.id==id))
    return await read_data()

@semestre_router.delete("/{id}")
async def delete_data(id:int):
    con.execute(Semestre.__table__.delete().where(Semestre.__table__.c.id==id))
    return await read_data()
