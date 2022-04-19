from typing import List
from database import get_db
from sqlalchemy.sql import text


def update_ids_of(tables_name: List[str]):
    for table_name in tables_name:
        sequence_name = f"{table_name}_id_seq"
        db_gen = get_db()
        db = next(db_gen)
        db.execute(text(f"SELECT setval('{sequence_name}', (SELECT max(id) FROM {table_name}));"))
