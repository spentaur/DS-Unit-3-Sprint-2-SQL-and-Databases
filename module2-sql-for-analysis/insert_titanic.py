import os
import pandas as pd
from sqlalchemy import create_engine, Enum
from sqlalchemy.types import Float, Integer, VARCHAR, Boolean
from dotenv import load_dotenv

load_dotenv()

print("Connecting to database...")
db_string = os.getenv("DB_STRING")
engine = create_engine(db_string)
pg_conn = engine.connect()
print("Connected!")
print("\n")

print("Reading CSV...")
df = pd.read_csv('titanic.csv')
print("CSV Read!")
print("\n")

print("Formatting...")
df['Survived'] = df['Survived'].astype(bool)
print("Formatted!")
print("\n")

print("Assigning Enum...")
sexes = ('male', 'female')
sexes_enum = Enum(*sexes, name="sex")
print("Assigned!")
print("\n")

print("Saving to PostgreSQL...")
dtype = {'Survived':                Boolean(),
         'Pclass':                  Integer(),
         'Name':                    VARCHAR(100),
         'Sex':                     sexes_enum,
         'Age':                     Float(),
         'Siblings/Spouses Aboard': Integer(),
         'Parents/Children Aboard': Integer(),
         'Fare':                    Float()}
df.to_sql('titanic', pg_conn, dtype=dtype)
print("Saved!")
print("\n")

print("Closing Connection...")
pg_conn.close()
print("Closed!")
