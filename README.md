
# login_and_registration

Login and Registration page with validation using:
- Python: Flask
- MySQL

<img width="832" alt="Screen Shot 2022-04-16 at 12 36 47 AM" src="https://user-images.githubusercontent.com/31575741/163662263-baceebf5-a1f2-4c30-b9bb-2f1788fa4f8a.png">

Users have to follow certain criteria in order to be able to register and create an account:

First Name - letters only, at least 2 characters and that it was submitted
Last Name - letters only, at least 2 characters and that it was submitted
Email - valid Email format, does not already exist in the database, and that it was submitted
Password - at least 8 characters, and that it was submitted
Password Confirmation - matches password

if those criterias are not met, the user will get an error message.

Users have to register first before they can login and access their account. They will get an error message if the email is not in the database or the password does not match. 
