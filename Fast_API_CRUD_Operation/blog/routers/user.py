
from fastapi import Depends, HTTPException , status
from requests import Session
from  .. import schemas, models
from ..database import  get_db
from ..hashing import Hash
from fastapi import APIRouter , Depends
from .. import schemas, models



router= APIRouter(tags=['Users'], prefix="/user")



@router.post('/', response_model=schemas.UserBlog )
def create_user(request: schemas.User, db :Session = Depends(get_db)):
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.UserBlog)
def get_user(id, db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} is not found')
    return user