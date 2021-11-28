from model import Admin  
from controller import food_data
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
            
            if admin_runner.Admin_checker():

                print('Hello you loggined as an amdin')

                print('For see menu enter (Menu) \n for see users enter (users) \n for edit menu enter (Menu Edit)\n and for change password enter (chpass) ')

                request=input('\nwhat do you want to do ?\n ')
                if request=='menu' or request=='Menu':
                       show_data.show_menu_()
            else:
                print('you are not admin sir')
            

    

class show_data(food_data):
     
    def __init__(self):
        pass  

    def show_menu_():
        print('this is food menu : ')
        food_data.show_menu()
        

    
User_type=input('please enter who are you admin or user ?  : ')

run_view=View(User_type)

run_login=login()