import pymysql
import HashingDB

# Database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="", database="software security app")
cursor = connection.cursor()

# Define the function to register a user
def registerUser(email, username, password, role):
    try:
        # SQL query to insert a new user into the 'registeruser' table
        sql = """INSERT INTO registeruser (Email, UserName, Password, Role) 
                 VALUES (%s, %s, %s, %s)"""
        
        # Execute the SQL query with user data
        cursor.execute(sql, (email, username, password, role))

        # Commit the changes to the database
        connection.commit()
        
        print("User registered successfully!")
    except Exception as e:
        # If an error occurs, rollback the transaction
        connection.rollback()
        print("Error registering user:", str(e))
    # finally:
    #     # Close the database connection
    #     connection.close()
        
def loginUser(Email, password,role):
    try:
        # SQL query to check if the provided username and password match
        hashPww=HashingDB.hash_password(password)
        sql = """SELECT * FROM registeruser WHERE Email = %s AND Password = %s AND Role = %s"""
        
        # Execute the SQL query with the provided username and password
        cursor.execute(sql, (Email, hashPww,role))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            # If a matching user is found, return True to indicate successful login
            return True
        else:
            # If no matching user is found, return False to indicate failed login
            return False
    except Exception as e:
        # Handle any errors that might occur during the database operation
        print("Error during login:", str(e))
        return False
    #finally:
        # Close the database connection
        #connection.close()

