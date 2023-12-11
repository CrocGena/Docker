users=[
    (0,'geno','kompiuterigen')
]

username_mapping={user[1]:user for user in users}
username_input=input('username:  ')
pasword_input=input("pasword: ")

_,username,password=username_mapping[username_input]

if pasword_input==password:
    print("correct")
else:
    print("incorect")

from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"
if __name__=="__main__":
    app.run()

