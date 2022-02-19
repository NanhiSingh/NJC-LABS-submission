import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE MOVIES
                (LEAD_ACTOR TEXT,
                 LEAD_ACTRESS TEXT,
                 YEAR_OF_RELEASE, 
                 DIRECTOR_NAME TEXT NOT NULL);''')

print("Table created successfully")

conn.execute("INSERT INTO MOVIES VALUES ('Akshay Kumar', 'Kriti Sanon', 2022, 'Farhad Samji')")
conn.execute("INSERT INTO MOVIES VALUES ('Allu Arjun', 'Amrapali', 2022, 'K. Krishnamurthy')")
conn.execute("INSERT INTO MOVIES VALUES ('Yashpal Singh', 'Aradhya', 2021, 'Nanhi Singh')")
conn.execute("INSERT INTO MOVIES VALUES ('Keanu Reeves', 'Senela', 2018, 'James Chad')")
conn.execute("INSERT INTO MOVIES VALUES ('Will Smith', 'Wanda', 2017, 'Selena Pearls')")

conn.commit()
print("Records created successfully")

cursor = conn.execute("SELECT LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR_NAME FROM MOVIES")

for row in cursor:
    print("LEAD ACTOR = ", row[0])
    print("LEAD ACTRESS = ", row[1])
    print("YEAR OF RELEASE = ", row[2])
    print("DIRECTOR = ", row[3])
    print('\n')

print("Operation done successfully")
conn.close()

