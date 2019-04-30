import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    count = 0
    f = open("books.csv")
    reader = csv.reader(f)
    for ISBN, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:ISBN, :title, :author, :year)",
                    {"ISBN": ISBN, "title": title, "author": author, "year": year})
        count += 1
        print(f"book number {count} added")
    db.commit()
    print(f"{count} books loaded")

if __name__ == "__main__":
    main()
