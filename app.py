from flask import Flask, render_template, request
app = Flask(__name__) ## this turns it into the main file I guess?? No, it connects to the naming convention we use to create files and folders
@app.route("/", methods=["GET", "POST"])
def index():
    return (render_template("index.html"))

if __name__ == "__main__":
    app.run()

