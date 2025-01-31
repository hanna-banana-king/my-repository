# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)


# create a function named "multiply" which multiplies two numbers
def multiply(a,b):
    return a*b 


# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/') 
@app.route("/")
def index():
    return render_template("index.html")


# calculate prodcut of them using "multiply" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, multiplication is not been calculated" string returns to them with "result.html" file
@app.route("/calc", methods=["GET", "POST"])
def calc():

    if request.method == "POST":
        # this is a POST response
        # multiply num1 x num2
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        c = multiply(int(num1), int(num2))
        return render_template("result.html", a=num1, b=num2, result=str(c), developer_name="Hanna")


 # x = {"Number": "One"}
 # x["Number"] ====> "One"

    else:
        return render_template("result.html", developer_name="Hanna")


# Add a statement to run the Flask application which can be debugged.
if __name__ == "__main__":
    app.run(debug=True)
