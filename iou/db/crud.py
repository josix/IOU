from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, display_name: str):
    return (
        db.query(models.User).filter(models.User.display_name == display_name).first()
    )


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(line_id=user.line_id, display_name=user.display_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.User(line_id=group.line_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def create_user_group(db: Session, user_group_map: schemas.UserGroupCreate):
    db_user_group = models.UserGroup(**user_group_map.dict())
    db.add(db_user_group)
    db.commit()
    db.refresh(db_user_group)
    return db_user_group
