
from typing import Optional
import base64, json
from fastapi import FastAPI, File, HTTPException , status
import uuid

app = FastAPI()


@app.post("/image-data/" , tags=['Create'])

async def create_upload_file(file : Optional[str] = File(None)):
    global payload
    if not file:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="No upload file sent")
    with open(file, "rb") as image2string:
        unique_ID=uuid.uuid1()
        converted_string = base64.b64encode(image2string.read()).decode('ascii')
        imagedata = "data1:image/jpg;base64,"+converted_string
        payload = json.dumps({"imagedata": converted_string})
        file = open('Base64_files/image_2_Base64_'+str(unique_ID)[:5]+'.txt', 'w')
        file.write(payload)
        file.close()
    return "ok"

