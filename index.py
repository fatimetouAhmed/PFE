from fastapi import FastAPI
from routes.user import user_router
from routes.salle import salle_router
from routes.departement import departement_router
from routes.notification import notification_router
from routes.filiere import filiere_router
from routes.semestre import semestre_router
from routes.etudiant import etudiant_router
from routes.matiere import matiere_router
from routes.etudiermat import etudiermat_router
from routes.semestre_etudiant import semestre_etudiant_router
from routes.examun import examun_router

app=FastAPI()
# Définir les routes pour l'ensemble d'itinéraires utilisateur
app.include_router(user_router, prefix="/users", tags=["Utilisateurs"])

# Définir les routes pour l'ensemble d'itinéraires etudiant
app.include_router(etudiant_router, prefix="/etudiants", tags=["Etudiants"])

# Définir les routes pour l'ensemble d'itinéraires matiere
app.include_router(matiere_router, prefix="/matieres", tags=["Matieres"])

# Définir les routes pour l'ensemble d'itinéraires salle
app.include_router(semestre_etudiant_router, prefix="/semestre_etudiants", tags=["Semestre_etudiants"])

# Définir les routes pour l'ensemble d'itinéraires salle
app.include_router(salle_router, prefix="/salles", tags=["Salles"])

# Définir les routes pour l'ensemble d'itinéraires salle
app.include_router(etudiermat_router, prefix="/etudiermatiere", tags=["etudiermatiere"])

# Définir les routes pour l'ensemble d'itinéraires departement
app.include_router(departement_router, prefix="/departements", tags=["Departemens"])

# Définir les routes pour l'ensemble d'itinéraires notification
app.include_router(notification_router, prefix="/notifications", tags=["Notifications"])

# Définir les routes pour l'ensemble d'itinéraires filiere
app.include_router(filiere_router, prefix="/filieres", tags=["Filieres"])

# Définir les routes pour l'ensemble d'itinéraires semestre
app.include_router(semestre_router, prefix="/semestres", tags=["Semestres"])

# Définir les routes pour l'ensemble d'itinéraires examun
app.include_router(examun_router, prefix="/examuns", tags=["Examuns"])

@app.get("/")
async def home():
    return {"message": "Bienvenue sur l'API de gestion des utilisateurs et des salles."}
