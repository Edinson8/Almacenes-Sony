import os
from urllib.parse import quote_plus

DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "tu_pass")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "almacenes_sony")

# SQLALCHEMY_DATABASE_URI para MySQL (ejemplo usando mysqlclient)
SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{quote_plus(DB_PASS)}@{DB_HOST}/{DB_NAME}"
SECRET_KEY = os.getenv("SECRET_KEY", "cambia_esto_en_produccion")
