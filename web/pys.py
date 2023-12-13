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

from flask import Flask, request,jsonify
from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert_one({
    'num_of_users': 0
})

class Visit(Resource):
    def get(self):
        pre_num = UserNum.find({})[0]["num_of_users"]
        new_num = 1 + pre_num
        UserNum.update_one({}, {"$set": {"num_of_users": new_num}})
        return "Hello user " + str(new_num)




@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  

    return 'Data received and processed successfully'

@app.route('/')
def hello_world():
    return "Hello, world!"


api.add_resource(Visit, "/hello")
if __name__ == '__main__':
    app.run(host='0.0.0.0')
