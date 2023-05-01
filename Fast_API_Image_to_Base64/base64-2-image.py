

import base64
from fastapi import FastAPI, HTTPException , status
import uuid


app = FastAPI()


@app.post("/image/" , tags=['Create'])

async def get_json(file : dict ):
    # global payload
    if not file:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="No Image text sent")
    Unique_ID=uuid.uuid1()
    image_64_decode = base64.b64decode(file["imagedata"])
    image_result = open('images/image_'+str(Unique_ID)[:5]+'.jpg', 'wb')
    image_result.write(image_64_decode)
    image_result.close()

    return {"Message":"The Json-data is converted to image successfully."}

