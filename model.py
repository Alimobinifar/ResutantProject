from controller import Admin_query

from controller import food_data
class Admin(Admin_query):

    def __init__(self,username,password):

        self.username=username
        self.password=password

    def Admin_checker(self):
        try:
            
            if self.username=='Admin' and self.password=='Root':
                return True

        except :

            return False
    
    def define_admin(id,UserName,PassWord):
        Admin_query.define_admin(id, UserName, PassWord)
    

        



class food(food_data):
    
    def add_food_data(food_id,food_name_,food_material_,food_price_,food_reservasion_):
        food_data_runner=food_data()
        food_data_runner.insert_food(food_id,food_name_, food_material_, food_price_, food_reservasion_)

    

    





