from fastapi import FastAPI
import uvicorn



app=FastAPI()

@app.get('/')
def index():
   return {"message": "Hello World"}

dict_data={}

@app.post('/update')
def update(name:str):
   dict_data[name]=name
   return dict_data
