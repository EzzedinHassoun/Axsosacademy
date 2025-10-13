from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = []
            errors["first_name"].append("First Name should be at least 2 characters")
        if postData['first_name'].isalpha() == False:
            if "first_name" not in errors:
                errors["first_name"] = []
            errors["first_name"].append("First Name cannot contain numbers or special characters")
        
        if len(postData['last_name']) < 2:
            errors["last_name"] = []
            errors["last_name"].append("last Name should be at least 2 characters")
        if postData['last_name'].isalpha() == False:
            if "last_name" not in errors:
                errors["last_name"] = []
            errors["last_name"].append("Last Name cannot contain numbers or special characters")
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = []
            errors["email"].append("Invalid email address!")
        if is_exists(postData['email']):
            if "email" not in errors:
                errors["email"] = []
            errors["email"].append("The email address you provided is already associated with an existing account")
        
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters long"

        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Confirm password should be the same as password"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 


def register(request_data):
    first_name = request_data['first_name']     
    last_name = request_data['last_name']
    email = request_data['email']
    password = request_data['password']   
    user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    return user

def get_user(email):
    try:
        user = User.objects.get(email=email)
        print("TYPE of user object", type(user))
        return user
    except User.DoesNotExist:
        print("User with email {} does not exist".format(email))
        return None  

    
def is_exists(email):
    return User.objects.filter(email=email).exists()