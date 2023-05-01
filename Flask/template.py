
from flask import Flask, render_template

app=Flask(__name__)

# @app.route('/home')
def home():
    return render_template('home.html')


# @app.route('/liki')
def liki():
    return render_template('index.html')


app.add_url_rule('/home',"home",home)
app.add_url_rule('/liki',"liki",liki)

if __name__=="__main__":
    app.run(debug=True)