from flask import Flask, request
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from flask_cors import CORS
load_dotenv()
app = Flask(__name__)
CORS(app)

supabase: Client = create_client(
  os.getenv("SUPABASE_URL"),
  os.getenv("SUPABASE_KEY")
)

@app.get("/")
def health():
  return {"status":"giggling"}

@app.get("/api/resources")
def get_all_resources():
  response = supabase.table("friendly_giggle_resources").select("*").execute()
  return {"resources": response.data,"count": len(response.data)}


@app.post("/api/resources")
def create_resource():
  data = request.get_json()
  new_resource = {
    "title": data.get("title"),
    "category": data.get("category","general topics"),
    "description": data.get("description")
       }
  response = supabase.table("friendly_giggle_resources").insert(new_resource).execute()
  return {"message": "item added","response": response.data}, 201


if __name__ == "__main__":
  app.run(debug=True)

