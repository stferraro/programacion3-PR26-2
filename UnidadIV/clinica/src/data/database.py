import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

DB_NAME = os.getenv("DB_NAME", "clinica_veterinaria.db")
DB_DIR = os.getenv("DB_DIR", "resources")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / DB_DIR / DB_NAME


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conexion = sqlite3.connect(DB_PATH)
    conexion.execute("PRAGMA foreign_keys = ON")
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tablas() -> None:
    with get_connection() as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS servicios (
                cod_servicio INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL CHECK (tipo IN ('consulta', 'hospedaje')),
                fecha TEXT NOT NULL,
                nombre_mascota TEXT NOT NULL,
                nombre_cliente TEXT NOT NULL,
                costo_base REAL NOT NULL,
                nombre_veterinario TEXT,
                especialidad INTEGER,
                dias_estadia INTEGER,
                tipo_habitacion INTEGER
            )
            """
        )
