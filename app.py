#This imports the Flask class from the flask package. 
#Flask is a micro web framework used to build web applications with Python.

from flask import Flask 

#This creates an instance of the Flask application.
#__name__ tells Flask where to look for resources (like templates or static files).

app = Flask(__name__)

#This defines a route:
#When someone accesses / (your homepage), Flask runs the home() function.
#It returns "Hello, CI/CD!", which is displayed in the browser.

@app.route('/')
def home():
    return "Hello, CI/CD!"

#This runs the Flask app only if this script is run directly (not imported as a module).
#host='0.0.0.0': Makes the app accessible from outside (important for Docker).
#port=5000: The app will listen on port 5000.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
