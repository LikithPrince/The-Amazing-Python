
from fastapi import APIRouter , Depends
from .. import schemas, models
from fastapi import Depends, HTTPException , status
from requests import Session
from  .. import schemas, models
from typing import List
from ..database import get_db



router= APIRouter(tags=['Blogs'], prefix="/blog")

@router.post('/', status_code=status.HTTP_201_CREATED )
def create(request : schemas.Blog, db :Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def modify(id, request : schemas.Blog, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not found')
    blog.update(request.dict())
    db.commit()
    return 'Updated Successfully'


@router.get('/', status_code=200, response_model=List[schemas.ShowBlog])
def all(db :Session = Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs


@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)
def show(id, db: Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not found')
    return blog



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not found')
    db.delete(blog)
    db.commit()
    return {f'Successfully deleted id no. {id} from the database.'}