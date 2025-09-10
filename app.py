from flask import Flask, render_template, request
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, "templates")
app = Flask(__name__, template_folder=template_path)

# 3️⃣ Route to display form
@app.route("/")
def home():
    return render_template("index.html")

# 4️⃣ Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")  # Get user input
    if username:
        # Save name to text file
        with open("user_names.txt", "a") as f:
            f.write(username + "\n")
        return f"Hello, {username}! Your name has been saved."
    return "No name received!"

# 5️⃣ Run the app
if __name__ == "__main__":
    app.run(debug=True)

