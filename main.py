from flask import Flask
from flask import render_template

# Using our Flask class we get from import we store it in app.
app = Flask(__name__)


# Using app.route we define our routes, / is our homepage.
@app.route("/")  # 127.0.0.1:5000.
def index():
    my_list = [1, 2, 3, 4, 5]
    pup_list = ["Jess", "Sammy", "Sarah"]
    name = "Emma"
    letters = list(name)
    pup_dict = {"pup_name": "Sammy"}
    return render_template(
        "basic.html",
        my_variable=name,
        letter=letters,
        pup_dict=pup_dict,
        my_list=my_list,
        pup_list=pup_list,
    )


@app.route("/info")
def info():
    return "<h1>Puppies</h1>"


@app.route("/puppy/<name>")  # Dynamic route example.
def user(name):
    return f"<h1>This is a page for {name}</h1>"  # name in string will also appear in address.


@app.route("/puppy_latin/<name>")
def latin(name):
    if name[-1] != "y":
        return f"<h1>{name}y</h1>"
    elif name[-1] == "y":
        return f"<h1>{name}iful</h1>"
    else:
        return name


if __name__ == "__main__":
    app.run(debug=True)  # Do not have this set when you place app into production.
