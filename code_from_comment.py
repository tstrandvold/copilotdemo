#a function for connecting to a database and returning a cursor object
def get_cursor():  
    #connect to the database
    conn = psycopg2.connect("dbname=postgres user=postgres")
    #open a cursor to perform database operations
    cur = conn.cursor()
    #return the cursor
    return cur