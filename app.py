from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        user_text = request.form["text"]
        return f"user typed:{user_text}"
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
