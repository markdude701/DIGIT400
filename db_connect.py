import MySQLdb 

def connection():
    conn = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd="cookies",
        db = "demo")
    c = conn.cursor()
    
    return c, conn