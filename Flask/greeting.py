
from datetime import datetime
from flask import Flask
from sqlalchemy import true

app=Flask(__name__)



@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Guest"):
    
    print(datetime.now())
    return  "Welcome to my page <b>"+name.title()+ "</b>"


if __name__=="__main__":
    app.run(debug=True)