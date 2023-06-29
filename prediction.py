from PIL import Image
from io import BytesIO
import deepface
from deepface import DeepFace
from pydantic import BaseModel
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, Column, Integer, String ,Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dbconfig import get_etudiant

models = [
          "VGG-Face", 
          "Facenet", 
          "Facenet512", 
          "OpenFace", 
          "DeepFace", 
          "DeepID", 
          "ArcFace", 
          "Dlib", 
          "SFace",
            ]

def predict_face(image_path):
  #  try:     
    #result = DeepFace.verify(image_path, img2_path = "image.jpg")
        results = DeepFace.find(img_path =image_path, db_path = "C:/Users/pc/Desktop/PFE/curd_fastapi/image",model_name=models[1],enforce_detection=False)
        try:  #if  results
          print ("resultats",results)
          photo = list(map(lambda x: x['identity'],results))
          
          if not photo:
            raise Exception("Étudiant inexistant")
          # return {"etudiant n existe pas"}
          else:
            url=photo[0][0]
            print("url:",url)
            donne=get_etudiant(url)
            return donne
        except Exception as e:
           return {"personne n'est pas detecte"}
      

      #  except Exception as e:
      #   return {"etudiant n existe pas"}
       #else:
     #    return 'etudiant n existe pas' 
 
    
    # Convertir la série en objet JSON
    #data_json = data.to_json(orient='values')
    #res=data_json.replace(" \ ", "")
     # result1= result.to_json()
    #if data_json is None:
     #   return {"error": "No face detected in the image"}