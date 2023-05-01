from multiprocessing import connection
from turtle import pd
from fastapi import FastAPI, File, UploadFile
from io import BytesIO
import pandas as pd
import psycopg2
import json

connection = psycopg2.connect(
    user='postgres', password='Liki@1996', host='localhost', port='8100', database='FastAPI')

cursor = connection.cursor()

list = []

app = FastAPI()


@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    file_name = file.filename
    contents = await file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer)
    buffer.close()
    list = df.to_dict(orient='records')
    print(list)

    sql_query = """INSERT INTO public.namma_mane(name, created_date, date)
        VALUES ('{0}', now(), '{1}')""".format(file_name, json.dumps(list))

    print(sql_query)
    cursor.execute(sql_query)
    connection.commit()

    print(sql_query)
