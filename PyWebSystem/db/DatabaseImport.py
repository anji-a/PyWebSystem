

def get_database(DBENGINE):
    if DBENGINE == "django.db.backends.postgresql":
        import psycopg2 as Database
        return Database
