from storage.database import (
    Database
)


db = Database()

cursor = db.connection.cursor()

cursor.execute(
    "DELETE FROM sessions"
)

db.connection.commit()

print(
    "History cleared"
)