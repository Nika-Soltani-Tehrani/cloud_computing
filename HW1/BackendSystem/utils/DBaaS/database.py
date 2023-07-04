import mysql.connector
import BackendSystem.utils.DBaaS.config as config


class Database:

    def __init__(self):
        self.cursor = None
        self.db = self.connect()
        self.create_table()

    @staticmethod
    def connect():
        return mysql.connector.connect(
            host=config.HOST,
            port=config.PORT,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DATABASE
        )

    def create_table(self):
        self.cursor = self.db.cursor()
        stmt = "SHOW TABLES LIKE 'posts'"
        self.cursor.execute(stmt)
        result = self.cursor.fetchone()
        if result:
            return
        else:
            self.cursor.execute("CREATE TABLE posts "
                           "(id int primary key , "
                           "description VARCHAR(255), "
                           "email VARCHAR(255),"
                           "state VARCHAR(255),"
                           "category VARCHAR(32))")
            self.cursor = self.db.cursor()
            self.cursor.execute("SHOW TABLES")
        print(self.cursor)

    def insert_data(self, id, description, email, state, category):
        self.cursor.execute(f"SELECT * FROM posts WHERE {id} = id")
        result = self.cursor.fetchall()
        if result:
            # print("row data is duplicate")
            return
        else:
            sql = "INSERT INTO posts (id, description, email, state, category) VALUES (%s, %s, %s, %s, %s)"
            val = (id, description, email, state, category)
            self.cursor.execute(sql, val)
            self.db.commit()
            print(self.cursor.rowcount, "record inserted.")

    def get_data(self, post_id):
        print(post_id)
        self.cursor.execute(f"SELECT * FROM posts WHERE id ={post_id}")

        result = self.cursor.fetchall()

        for x in result:
            print(x)
        return x

    def update_state(self, post_id, new_state):
        self.cursor.execute(f"UPDATE posts SET state = '{str(new_state)}' WHERE id = {post_id}")
        # sql = "UPDATE posts (id, description, email, state, category) VALUES (%s, %s, %s, %s, %s)"
        # val = (id, description, email, state, category)
        # self.cursor.execute(sql, val)

    def update_category(self, post_id, new_category):
        self.cursor.execute(f"UPDATE posts SET category = '{new_category}' WHERE id = {post_id}")


# db = Database()
# # db.insert_data(123, 'heelo', 'world', 'processing', 'not processed')
# db.update_state(123, 'processing')
# # db.get_data(123)
