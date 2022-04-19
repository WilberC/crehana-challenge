from database import get_db, SessionLocal


# Todo We have to improve the close_session to work with normal requests and the sync
def find(model, all_objs=False, close_session=False, **kwargs):
    try:
        if close_session:
            db_gen = get_db()
            db = next(db_gen)
        else:
            db = SessionLocal()
        instance = db.query(model).filter_by(**kwargs)
        if all_objs:
            return instance.all()
        else:
            return instance.first()
    except Exception as e:
        print(f"==> Finding error, detail info -> {e}")


def create(model, close_session=False, **kwargs):
    try:
        if close_session:
            db_gen = get_db()
            db = next(db_gen)
        else:
            db = SessionLocal()
        instance = model(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    except Exception as e:
        print(f"==> Creation error, detail info -> {e}")


def find_or_create(model, close_session=False, **kwargs):
    instance = find(model, close_session=close_session, **kwargs)
    if instance:
        return instance
    else:
        instance = create(model, close_session=close_session, **kwargs)
        return instance


def delete(model, **kwargs):
    db = SessionLocal()
    db.query(model).filter_by(**kwargs).delete()
    db.commit()
    db.close()


def update(model, find_by, updated_values):
    db = SessionLocal()
    db.query(model).filter_by(**find_by).update(updated_values)
    db.commit()
    db.close()
