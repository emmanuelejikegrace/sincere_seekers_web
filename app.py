from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the Home Page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)