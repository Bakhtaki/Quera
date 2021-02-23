import re
import hashlib

Accounts = []

class Site:
    def __init__(self,url,register_users,active_users):
        self.url  = url
        self.register_users = []
        self.active_users = []
    
    def show_user(user):
        pass
    
    def register(self,user):
        for members  in self.register_users:
            if members == user:
                raise  Exception("user allready registered")
        id = len(self.register_users)
        self.register_users.append(user)
        print("registration succesful!!!")
                
    def login(self,login_parameter,password):
        def email_check(string):
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,5}$'

            if (re.search(regex, string)):
                return True
            else:
                return False
        if email_check(login_parameter):
            current_password = ''
            current_user= ''
            for member in Accounts:
                if member[5] == login_parameter:
                    current_password =member[2]
                    current_user = member[1]
            if hashlib.sha256(password.encode('utf-8')).hexdigest() == current_password:
                if  not current_user in self.active_users:
                        self.active_users.append(current_user)
                        print('login succesful')
                else:
                    print('user already logged in ')
            else:
                print('bad password')
        else:
            current_password =''
            for member in Accounts:
                if member[1] == login_parameter:
                    current_password = member[2]
                    current_user = member[1]
            if hashlib.sha256(password.encode('utf-8')).hexdigest() == current_password:
                if not current_user in self.active_users:
                    self.active_users.append(current_user)
                    print('login succesful')
                else:
                    print('user already logged in ')
            else:
                print('bad password')
            
    def log_out(self,user):
        if user in self.active_users:
            self.active_users.pop(user)
            print('user logged out')
        else: 
            print('user not logged in')

        
    
    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)
    
    def __str__(self):
        return self.url
    


class Account: 
    def __init__(self,username,password,user_id,phone,email):
        self.username = username
        self.password = password
        self.userid = user_id
        self.phone = phone   
        self.email = email
    
    def __str__(self):
        return self.username
    
    def __repr__(self):
        return self.username +'\n'+self.email
    
    def set_new_password(self,password):
        
        if self.password_validation(password):
           return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def username_validation(self,username):
        if '_' in self.username:
            return self.username
        else: 
            raise Exception("user invalid")
            
    
    def password_validation(self,password):
        def all_present(password):
            regex = ("^(?=.*[a-z])(?=." +"*[A-Z])(?=.*\\d)") #+"(?=.*[-+_!@#$%^&*., ?]).+$")       
            p = re.compile(regex)
            
            if (password == None):
                return False
            
            if (re.search(p,password)):
                return True
            else: 
                return False
        
        if len(password) > 8 and all_present(password):
            return True
        else:
            raise  Exception('invalid password')
            
                      
             
    
    def id_validation (self,id):
        
        def check_id_logic(id):
            sum = 0
            counter = 10
            for position in range(len(id)-1):
                sum += int(id[position]) * counter
                counter -= 1
                mod = sum % 11
            
            if mod < 2:
                
                if mod == int(id[9]):
                    logic = True
                else:
                    logic = False
            if 11 - mod == int(id[9]):
                logic = True
            else:
                logic = False
            return logic
        
        if len(id) == 10 and check_id_logic(id):
            return id 
        else:
            raise Exception('Code Melli invalid')
    
    
    def phone_validation(self,phone):
        if phone.startswith('+98'):
            phone = phone.replace('+98','0')
            return phone
        if phone.startswith('09'):
            return phone
        else:
            raise  Exception("invalid phone number")
    
    def email_validation(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,5}$'
        
        if (re.search(regex,email)):
            return email
        else:
            raise Exception("invalid Email ")

    
    def register_Account(self):
        username = self.username_validation(self.username)
        password = self.set_new_password(self.password)
        user_id = self.id_validation(self.userid)
        phone = self.phone_validation(self.phone)
        email = self.email_validation(self.email)
        row = len(Accounts)+1
        user_data = [row,username,password,user_id,phone,email]
        Accounts.append(user_data)
    
def show_welcome(func):
    def inner(user):
        user = user.replace('_',' ')
        for word in user:
            user = user.title()
        
        if len(user)> 15:
            user =user[:12]+'...'
            return func(user)
    return inner


def verify_change_password(func):
    def inner(user,password,new_pass):
        current_password = ''
        for member in Accounts:
            if member[1] == person.username:
                current_password = member[2]
                if hashlib.sha256(password.encode('utf-8')).hexdigest() == current_password:
                    updated_password = person.set_new_password(new_pass)
        for member in Accounts:
            if member[1] == person.username :
                member[2] = updated_password
        return func              
    return inner
     
                        
@show_welcome
def welcome(user):
    return ("wellcome to our site ", user)

@verify_change_password
def change_password(user,old_pass,new_pass):
    return("your passwrod changed Succesfully!")


def register_account(username,password,user_id,phone,email):
    return Account(username,password,user_id,phone,email)


person = register_account('hamidrez_bakhtaki','FuckingFuck@85','0079558003',
                          '+989121598580','hamidreza.bakhtai@gmail.com')
person.register_Account()
print(welcome(person.username))
x = change_password(person.username, person.password,'Panda@888')
site_address = 'bakhtaki.com'
HRB = Site(site_address,'','')
HRB.register(person.username)
HRB.login('hamidreza.bakhtai@gmail.com', 'Panda@888')
HRB.login(person.username, 'Panda@888')
print(HRB.__repr__())
print(HRB.__str__())
