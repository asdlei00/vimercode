        
class Database(object):
    placeholder = '?'
    
    def connect(self, dbtype, *args, **kwargs):
#Add-Begin by dantezhu in 2011-12-16 01:56:34
        self.dbtype = dbtype
#Add-End
        if dbtype == 'sqlite3':
            import sqlite3
            self.connection = sqlite3.connect(*args)
        elif dbtype == 'mysql':
            import MySQLdb
            self.connection = MySQLdb.connect(**kwargs)
            self.placeholder = '%s'

class DBConn(object):
    def __init__(self):
        self.b_debug = False
        self.b_commit = True
        self.conn = None

autumn_db = DBConn()
autumn_db.conn = Database()
