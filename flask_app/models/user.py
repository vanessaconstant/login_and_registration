from unittest import result
from wsgiref import validate
from flask_app.config.mysqlconnection import connectToMySQL, MySQLConnection
from flask_app import app
from flask import session, flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CREATE

    @classmethod
    def createUser(cls, data):

        if not cls.validate_reg(data):
            return False
        data = cls.parsed_data(data)

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        user_id = connectToMySQL('logreg_schema').query_db(query, data)
        return user_id

        # READ
    @classmethod
    def get_user_by_email(cls, email):

        data = {
            'email': email
        }

        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL('logreg_schema').query_db(query, data)

        if result:

            result = cls(result[0])

        return result

    @classmethod
    def login(cls, data):

        data = {
            'email': data['email'],
            'password': data['password']
        }

        if not User.get_user_by_email(data['email']):
            flash("You have entered a wrong email or password", 'login')
            return False

        result = User.get_user_by_email(data['email'])
        print(result.password)
        if not bcrypt.check_password_hash(result.password, data['password']):
            flash("You have entered a wrong email or password", 'login')
            return False

        else:
            user_id = result.id
            session['user_id'] = user_id
            return result

    @classmethod
    def get_user_by_id(cls, id):
        data = {
            'id': id
        }

        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL('logreg_schema').query_db(query, data)
        if result:
            result = cls(result[0])
        print(result)
        return result
    # UPDATE

    # DELETE

    @ staticmethod
    def validate_reg(data):
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            flash("This is not a valid email! Please try again", "register")
            is_valid = False
        if User.check_if_user_exist(data['email']):
            flash("Already have an account. Please login.", "register")
            is_valid = False
        if (len(data['first_name']) < 2):
            flash("First name requires at least 2 characters", "register")
            is_valid = False
        if(len(data['last_name']) < 2):
            flash("Last name requires at least 2 characters", "register")
            is_valid = False
        if(len(data['password']) < 8):
            flash("Password requires at least 8 characters", "register")
            is_valid = False
        if(data['password'] != data['conf_password']):
            flash("Confirmation password does not match", "register")
            is_valid = False
        return is_valid

    @ staticmethod
    def parsed_data(data):

        user_info = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': bcrypt.generate_password_hash(data['password'])
        }
        return user_info

    @ staticmethod
    def validate_login(data):
        pass
