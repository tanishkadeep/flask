from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('index.html')

@app.route("/fail/<int:marks>")
def failed(marks):
    return "Failed : " + str(marks)

@app.route("/pass/<int:marks>")
def passed(marks):
    return "Passed : " + str(marks)

@app.route("/results/<int:marks>")
def results(marks):
    if marks > 30:
        result = "passed"
    else:
        result = "failed"
        
    return redirect(url_for(result, marks=marks))


if __name__ == "__main__":
    app.run(debug=True)