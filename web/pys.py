# users=[
#     (0,'geno','komp')
# ]

# username_mapping={user[1]:user for user in users}
# username_input=input("username: ")
# pasword_input=input("pasword: ")

# _,username,password=username_mapping[username_input]

# if pasword_input==password:
#     print("correct")
# else:
#     print("incorect")

from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  

    return 'Data received and processed successfully'

@app.route('/')
def hello_world():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
