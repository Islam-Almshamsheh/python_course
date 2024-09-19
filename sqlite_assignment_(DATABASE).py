"""ASSIGNMENTS (DATABASE)"""
import sqlite3
db=sqlite3.connect("elzero.db")
cr=db.cursor()
cr.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    birth_date DATE UNIQUE,
    email TEXT UNIQUE
)
""")
# Defining a constant for a frequently used SQL query to improves code quality and reduces redundancy
INSERT_USER_QUERY = "INSERT INTO users VALUES (?,?,?,?)"
try:
    cr.execute(INSERT_USER_QUERY, (1, "Ahmad", '1980-10-20', "a@elzero.org"))
    cr.execute(INSERT_USER_QUERY, (2, "Sayed", '1990-10-20', "s@elzero.org"))
    cr.execute(INSERT_USER_QUERY, (3, "Gamal", '1991-10-05', "g@elzero.org"))
    cr.execute(INSERT_USER_QUERY, (4, "Mahmoud", '1987-10-09', "m@elzero.org"))
    cr.execute(INSERT_USER_QUERY, (5, "Sameh", '2000-11-08', "ss@elzero.org"))
except sqlite3.Error as sr:
    print("There is a PROBLEM which is : ", sr)

# cr.execute("select * from users")
# result=cr.fetchall()
# for row in result:
#     print(row[0] , row[1], row[2], row[3],sep=" <=> ")

#ASSIGNMENT FOUR
# """
# The following represnts a syntax error
# cr.execute("SELECT * FROM USERS OFFSET 2")
# solve: OFFSET is typically paired with a LIMIT to specify how many rows you want after skipping
# """
cr.execute("SELECT * FROM USERS LIMIT 1 OFFSET 4")
result=cr.fetchall()
for row in result:
    print(row[0] , row[1], row[2], row[3],sep=" <=> ")

# ASSIGNMENT NO FIVE
def delete_users():
    """ 
        1. Takes input from users and turns it into an integer as the ID data type is an integer.
        2. Checks if the input ID exists in the database and performs actions based on the result.
        3. Shows remaining members after deletion.
    """
    user_selection = int(input("Enter the ID to delete that member: => ").strip())
    
    cr.execute("SELECT ID FROM USERS")
    matches = cr.fetchall()
    
    # Flatten the list of tuples into a list of IDs
    matches = [row[0] for row in matches]

    if user_selection in matches:
        
        #this code would give a sqlite3.ProgrammingError: parameters are of unsupported type
        """even for a single parameter, it should be passed as a tuple to avoid errors and ensure compatibility
           with how SQL queries are expected to work. 
           This pattern applies to most SQL tools and libraries."""
        # cr.execute("DELETE FROM USERS WHERE id= (?)", user_selection)
        # the corrected format:
        cr.execute("DELETE FROM USERS WHERE ID=(?)",(user_selection,))
        print(f"The member with the {user_selection} id is deleted successfully")
       
       # Show remaining members after deletion
        print("These are the remaining members after deletion:")

        cr.execute("select * from users")
        result = cr.fetchall()
        for row in result:
            print(f"ID => {row[0]}, NAME => {row[1]}, BIRTH_DATE => {row[2]}, EMAIL => {row[3]}")

    else:
        print("YOUR ENTERED ID IS NOT EXISTED IN THE DATABASE")    

delete_users()
db.commit()
db.close()    
