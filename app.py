from flask import Flask, render_template, request
import harversine_distance
app = Flask(__name__)
@app.route("/", methods = ["POST", "GET"])
def calculatedisctance():
    if request.method == "POST":
        coordA = request.form.get("coordA")
        coordB = request.form.get("coordB")
        coordA1 = coordA.replace(" ","")
        coordB1 = coordB.replace(" ","")
        lat1 = float(coordA1.split(",")[0])
        lon1 = float(coordA1.split(",")[1])
        lat2 = float(coordB1.split(",")[0])
        lon2 = float(coordB1.split(",")[1])

        result = harversine_distance.haversine_distance(lat1,lon1,lat2,lon2)

        return render_template("form.html", answer = result)
    else:
        return render_template("form.html")


if __name__ == "__main__":
    app.run(debug = True)    