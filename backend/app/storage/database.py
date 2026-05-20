import sqlite3
import threading
from pathlib import Path

from config.settings import (
    DATABASE_PATH
)



class Database:

    def __init__(self):

        DATABASE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.lock = threading.Lock()

        self.connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )


        self.initialize()

    def initialize(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions(

                id INTEGER PRIMARY KEY,

                started_at TEXT,

                ended_at TEXT,

                duration REAL,

                language TEXT,

                raw_text TEXT,

                cleaned_text TEXT,

                latency REAL,

                provider TEXT,

                tags TEXT
            )
            """
        )

        self.connection.commit()