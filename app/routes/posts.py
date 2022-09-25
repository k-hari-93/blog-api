from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from .. import models, schemas, database, oauth2

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(database.get_db), skip: int = 0, limit: int = 10,
              search: Optional[str] = ""):
    
    results = db.query(models.Post, func.count(models.Vote.user_id).label("votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True
        ).group_by(models.Post.id).order_by(models.Post.id).filter(or_(
        models.Post.title.ilike(f"%{search}%"),
        models.Post.content.ilike(f"%{search}%"))
        ).order_by(models.Post.id).offset(skip).limit(limit).all()
    
    return results

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db),
                current_user: models.User = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post
    
@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(database.get_db)):
    post = db.query(models.Post, func.count(models.Vote.user_id).label("votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True
        ).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} was not found")
        
    return post


@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(database.get_db),
                current_user: models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} was not found")
        
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Not authorized to perform requested action")
        
    post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(database.get_db),
                current_user: models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} was not found")
    
    if updated_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Not authorized to perform requested action")
    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    
    return updated_post
