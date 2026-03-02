from flask import Flask,render_template,request
import requests
app = Flask(__name__)



def translate_text(text):
    url = "http://localhost:5001/translate"

    data = {
        "q":text,
        "source":"en",
        "target":"hi",
        "format":"text"
    }

    response = requests.post(url,data=data)
    result = response.json()

    return result["translatedText"]

@app.route("/",methods=["GET","POST"])
def home():
    translated_text=""

    if request.method == "POST":
        user_text = request.form["text"]
        translated_text = translate_text(user_text)
    return render_template("index.html",translated_text=translated_text)

if __name__=="__main__":
    app.run(debug=True)
