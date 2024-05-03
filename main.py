from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")



@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        return redirect(url_for("home"))
    elif request.method == "GET":
        return render_template("edit.html")




@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        return redirect(url_for("home"))
    elif request.method == "GET":
        return render_template("add.html")








if __name__ == "__main__":
    app.run(debug=True)




