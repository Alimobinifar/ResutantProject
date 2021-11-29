from model import Admin ,food
from controller import food_data,user
from model import root_admin
class View:
     
    def __init__(self,type_):

        self.type_=type_
       
        if self.type_=='admin':
            login.admin()

        if self.type_=='user':
            login.user()


class login():

    def admin():
            
            print('hello admin')

            user_name=input('please enter your user name :')

            pass_word=input('please enter your user password :')
            
            admin_runner=Admin(user_name, pass_word)
            
            if admin_runner.Admin_checker()==True:
                print(' ')
                print('Hello you loggined as an amdin\n')
                print('')
                print('for define an admin (just by root admin): add amin ')

                print('For see menu enter (Menu) \n')
                
                print('For see menu enter add food \n')

                print('For remove food enter rm food \n')
                
                print('for see users enter : users \n')

                print('for edit menu enter : Menu Edit\n')

                print('for change password enter (chpass)\n')

                print('for define users : add user \n')
                print('\n')
                request=input('what do you want to do ?\n ')

                if request=='menu' or request=='Menu':
                       show_data.show_menu_()

                elif request=='users' or request=='Users':
                    show_data.show_users()

                elif request=='add user' or request=='Add User' or request=='Add user':
                    user_.define_user()

                elif request=='add food' or request=='Add Food' or request=='Add food':
                    admin.add_food_by_admin()
                
                elif request=='rm food' :
                    admin.remove_food_by_admin()
                
                elif request=='add admin':
                    try:
                        if user_name=='Admin' and pass_word=='Root':
                            admin_id=input('please enter amin id : ')
                            UserName=input('please enter user name : ')
                            PassWord=input('please enter password')
                            root_admin.define_admin(admin_id, UserName, PassWord)
                            print('successflly registered . ')
                        else:
                            print('just root admin is able to manage other admins .... ')
                    except Error as e :
                            print(e)


                 

                             
                

             

    

class show_data(food_data,user):
     
    def __init__(self):
        pass  

    def show_menu_():
        print('this is food menu : ')
        food_data.show_menu()
    
    def show_users():
        print('this is list of users :')
        user.show_user()

class user_():
    
    def define_user():
        id=input('please enter user id :')
        name=input('please enter name of user :')
        family=input('please enter users family :')
        phone=input('please enter users phone :')
        address=input('please enter users address :')
        try:
            Admin.define_user(id, name, family, phone, address)    
        except:
            'Error in Internal Services ... '
class admin(food):

    def change_password():

        admin=input('please enter your new password :')   
    
    def add_food_by_admin():

        food_id=int(input('please enter food id :'))
        name=input('please enter food name :')
        material=input('whats the material of this food ? ')
        price=int(input('please enter price : '))
        food_reservasion=input('is it possible to reserve or no ?')

        # try:
        food.add_food_data(food_id, name, material, price, food_reservasion)

        # except :
        #     raise Exception('some problems in adding data... check functions ...')
    
    def remove_food_by_admin():

        food_id=input('please enter food id : ')
        food_data.remove_food(food_id)
    




User_type=input('please enter who are you admin or user ?  : ')

run_view=View(User_type)

run_login=login()