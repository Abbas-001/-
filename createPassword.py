#insta: @sahla_dot
# create password by Python 
from random import choice
def create_pass(len):
        passworrd = ""
        data = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        for i in range(len):
            passworrd += choice(data)
        return passworrd

passLenth = 8
finalPass = create_pass(passLenth)
print(f"the password is \" {finalPass} \"")
