from flask import Flask, render_template,request
import requests

app = Flask(__name__)

API_KEY = "key"

@app.route("/", methods=["GET","POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        print(response)
        data = response.json()

        if data["cod"] == 200:
            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
