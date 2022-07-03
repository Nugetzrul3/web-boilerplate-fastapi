from sqlmodel import create_engine

sqlite_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url, echo=True)

