from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def func():
    return render_template("form.html") 

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        marks=int(request.form['marks'])        
        return redirect(url_for("result",marks=marks))
    
    
@app.route("/result/<int:marks>")
def result(marks):
    return render_template("result1.html", marks = marks)

if __name__=="__main__":
    app.run(debug=True)