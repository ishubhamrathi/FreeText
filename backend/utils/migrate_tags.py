from path_setup import add_app_to_path

add_app_to_path()

from storage.database import Database

db = Database()

cursor = db.connection.cursor()

try:
    cursor.execute(
        """
        ALTER TABLE sessions
        ADD COLUMN tags TEXT
        """
    )

    db.connection.commit()

    print(
        "Tags added"
    )

except Exception as ex:
    print(
        ex
    )