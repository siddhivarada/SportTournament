from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Sports Tournament</h1><ul><li>Cricket</li><li>Football</li><li>Basketball</li></ul>"
print("Server is running on http://localhost:5000")