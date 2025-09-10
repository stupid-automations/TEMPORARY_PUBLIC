from flask import Flask, render_template, request
import os

# Create Flask app
app = Flask(__name__)

# Route to display form
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")  # Get user input
    if username:
        # Save name to a text file
        with open("user_names.txt", "a") as f:
            f.write(username + "\n")
        return f"Hello, {username}! Your name has been saved."
    return "No name received!"

if __name__ == "__main__":
    app.run(debug=True)

