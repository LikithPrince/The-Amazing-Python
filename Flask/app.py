
from flask import Flask, url_for

app=Flask(__name__)

def hello():
    name="Likith"
    return name

def blogs():
    value="I am creating blogs!"
    return value

@app.route('/')
def index():
    return "This is home page"
@app.route('/myhome/')
@app.route('/myhome/<un>')
def home(un="Guest"):
    return "Welcome to the home page of <b>"+un.title()+"</b>"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('home',un='likith p'))
    print(url_for('home',un='likith',pw='123'))


app.add_url_rule('/hellow',"hello",hello)
app.add_url_rule('/get_blogs',"blogs",blogs)
# app.add_url_rule('/','index',index)
app.add_url_rule('/myhome/','home',home)
app.add_url_rule('/myhome/<un>','home',home)





if __name__=="__main__":
    app.run(debug=True)