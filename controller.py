import sqlite3
from sqlite3 import Error




def create_connection(db_file):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

def create_curser(query):
    conn=sqlite3.connect('/home/alimobinifar/Documents/Resturant/my_database.db')
    curser=conn.cursor()
    curser.execute(query)
    conn.commit()




create_connection('/home/alimobinifar/Documents/Resturant/my_database.db')




class DataBase:



    def create_table_food():
        query='CREATE TABLE IF NOT EXISTS Food(id INTEGER ,name VARCHAR(255),material VARCHAR(255),price INT ,reservation VARCHAR(20))'
        create_curser(query)

    def create_table_user():
        query='CREATE TABLE IF NOT EXISTS user(id PRIMARYKEY AUTOINCREAMENT  ,name TEXT, family TEXT, phone TEXT,Address TEXT)'
        create_curser(query)


    def create_table_orders():
        query='CREATE TABLE IF NOT EXISTS orders(order_id INTEGER ,costumer_id , name TEXT,food TEXT)'
        create_curser(query)

    def create_table_admin():
        query='CREATE TABLE IF NOT EXISTS admin(admin_id INTEGER ,username TEXT , password TEXT)'
        create_curser(query)
    






    if __name__ == '__main__':
        create_table_food()
        create_table_user()
        create_table_orders()



class food_data(DataBase):

    def insert_food(self,food_id,food_name,food_material,food_price,food_reservasion):
        DataBase.create_table_food()
        insert_query=f"INSERT INTO Food (id,name,material,price,reservation) VALUES('{food_id}','{food_name}','{food_material}','{food_price}','{food_reservasion}')"
        # insert_query='''insert into food values('khye bagher', 'er +ghorme +rice', '43534','yes')'''
        
        conn=sqlite3.connect('/home/alimobinifar/Documents/Resturant/my_database.db')
        curser=conn.cursor()
        curser.execute(insert_query)
        conn.commit()

    def show_menu():
                conn=sqlite3.connect('/home/alimobinifar/Documents/Resturant/my_database.db')
                cur = conn.cursor()
                cur.execute("SELECT * FROM Food")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    def remove_food(food_id):
        create_curser(f"delete from Food where id ='{food_id}'")
    

class Admin_query:

        def define_admin(admin_id,UserName,PassWord):
            DataBase.create_table_admin()
            insert_query=f"INSERT INTO admin (admin_id,username,password) VALUES('{admin_id}','{UserName}','{PassWord}')"
            create_curser(insert_query)
        
        def admin_check(username,password):
            conn=sqlite3.connect('/home/alimobinifar/Documents/Resturant/my_database.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM admin")
            rows = cur.fetchall()
            for row in rows:
                if row[1]==username and row[2]==password:
                    print(row)
                    return True
                    break
                else:
                    return False

        
        
        def admin_updater(self,id,user_name,pass_word):
                conn=sqlite3.connect('/home/alimobinifar/Documents/Resturant/my_database.db')
                cur = conn.cursor()
                cur.execute(f"UPDATE admin SET username ='{user_name}', password ='{pass_word}' WHERE admin_id ='{id}'")
                conn.commit()
       
        def define_user(id,name,family,phone,Address):
            DataBase.create_table_admin()
            insert_query=f"INSERT INTO user (id,name,family,phone,Address) VALUES('{id}','{name}','{family}','{phone}','{Address}')"
            create_curser(insert_query)
    

class user():

    def show_user():
            conn=sqlite3.connect('/home/alimobinifar/Documents/Resturant/my_database.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM user")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    
                
Admin_query_runner=Admin_query()





    




