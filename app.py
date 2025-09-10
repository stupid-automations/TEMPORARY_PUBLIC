from flask import Flask, render_template, request
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, "templates")
app = Flask(__name__, template_folder=template_path)

# 3️⃣ Route to display form
@app.route("/")
def home():
    return render_template("index.html")

# 5️⃣ Run the app
if __name__ == "__main__":
    app.run(debug=True)


