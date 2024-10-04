import sqlobject as SO;
import os;

db = os.path.abspath("bdd.db");
database = 'sqlite:/'+ db.replace('\\','/');

__connection__=SO.connectionForURI(database);

class Users(SO.SQLObject):
    """Crea tabla de usuarios""";
    user = SO.StringCol(length = 40);
    password = SO.StringCol(length = 40);
    active = SO.IntCol();
    
# Users.dropTable();
Users.createTable(ifNotExists = True)
# Users(user = 'f',password = 'f1',active = 1)
    
class BddMethods:
    def getUser(userName):
        get =   Users.select(SO.AND(Users.q.user == userName, Users.q.active == 1));
        get = get.getOne();
        
        return get