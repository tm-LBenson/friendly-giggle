from flask import Flask, request
from flask_cors import CORS
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Base, Resource

app = Flask(__name__)

CORS(app)

engine = create_engine("sqlite:///resources.db")
Base.metadata.create_all(engine)

@app.get("/")
def health():
  return {"message": "online"}

@app.get("/api/resources")
def get_resources():
  with Session(engine) as session:
    resources = session.scalars(select(Resource)).all()
    return  [
       {
      "id": resource.id,
      "title": resource.title,
      "description": resource.description,
      "category": resource.category
       } for resource in resources
      ]



myList = [1,2,3]
#List comprehension
[{"number": item} for item in myList]


@app.post("/api/resources")
def create_resource():
  data = request.get_json()

  resource = Resource(title=data.get("title"),
                      description=data.get("description"),
                      category=data.get("category")
              )

  with Session(engine) as session:
    session.add(resource)
    session.commit()
    session.refresh(resource)

  return {
    "resource": {
      "id": resource.id,
      "title": resource.title,
      "description": resource.description,
      "category": resource.category
    }
  }