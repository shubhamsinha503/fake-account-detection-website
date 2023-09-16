from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database (replace with a real database)
users = {'shubham': '123456', 'user2@example.com': 'password2'}


@app.route("/")
def home():
  return render_template('home.html')


@app.route("/login", methods=['POST'])
def login():
  name = request.form['txtN']

  
  if name == "xyz":
    return render_template('logoutpage.html')
  else:
    return render_template('loginpage.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
