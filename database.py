from sqlalchemy import create_engine

# Update with your actual database credentials
DATABASE_URL = "postgresql://username:password@localhost:5432/sales_db"

engine = create_engine(DATABASE_URL)

def get_db_connection():
    return engine.connect()
