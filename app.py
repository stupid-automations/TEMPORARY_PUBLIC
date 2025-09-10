from flask import Flask, render_template
import os

# Get the directory where app.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Set the template folder dynamically
template_path = os.path.join(base_dir, "templates")

app = Flask(__name__, template_folder=template_path)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
