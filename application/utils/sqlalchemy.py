from database import get_db


def find(model, all_objs=False, **kwargs):
    try:
        db_gen = get_db()
        db = next(db_gen)
        instance = db.query(model).filter_by(**kwargs)
        if all_objs:
            return instance.all()
        else:
            return instance.first()
    except Exception as e:
        print(f"==> Finding error, detail info -> {e}")


def create(model, **kwargs):
    try:
        db_gen = get_db()
        db = next(db_gen)
        instance = model(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    except Exception as e:
        print(f"==> Creation error, detail info -> {e}")


def find_or_create(model, **kwargs):
    instance = find(model, **kwargs)
    if instance:
        return instance
    else:
        instance = create(model, **kwargs)
        return instance