from app.db.client.client import MySQLConnection


class DbInteraction:
    def __init__(self,host,port,user,password,db_name,rebuild_db=False):
        self.mysql_connection = MySQLConnection(
            host=host,
            user=user,
            port=port,
            password=password,
            db_name=db_name,
            rebuild_db=rebuild_db)
        self.engine = self.mysql_connection.engine

        if rebuild_db:
            pass

def create_table_users(self):
    if not self.engone.dialect.has_table(self.engine, 'users'):
        Base.matada.tabels['users'].create(self.engine)
    else:
        self.mysql_connection.execute_query('DROP TABLE IF EXISTS users')
        Base.matada.tabels['users'].create(self.engine)

def create_table_musical_compositions(self):
    if not self.engone.dialect.has_table(self.engine, 'musical_compositions'):
        Base.matada.tabels['musical_compositions'].create(self.engine)
    else:
        self.mysql_connection.execute_query('DROP TABLE IF EXISTS musical_compositions')
        Base.matada.tabels['musical_compositions'].create(self.engine)

    def add_user_info(self, username, email, password):
        user = User(
            username=username,
            password=password,
            email=email
        )
        self.mysql_connection.session.add(user)
        return True

    def get_user_info(self, username):
        user = self.mysql_connection.session.query(User).filter_by(username=username).first()
        if user:
            self.mysql_connection.session.expire_all()
            return {'username':user.username, 'email':user.email, 'password':user.password}
        else:
            raise UserNotFoundException('User not found')

if __name__ == '__main__':
    db = DbInteraction(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='pass',
        db_name='some_db',
        rebuild_db=True
    )
