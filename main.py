import os

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/hugs")
def hugs():
    url_dic["css_path"] = url_for("static", filename="css/style.css")
    return render_template("hugs.html", **url_dic)


@app.route("/my_love")
def my_love():
    url_dic["love_1"] = url_for("static", filename="img/love_1.png")
    url_dic["love_2"] = url_for("static", filename="img/love_2.png")
    url_dic["css_path"] = url_for("static", filename="css/style.css")

    return render_template("second_page.html", **url_dic)


@app.route("/")
def love():
    url_dic["photo1"] = url_for("static", filename="img/IMG_3205.JPG")
    url_dic["photo2"] = url_for("static", filename="img/IMG_3200.JPG")
    url_dic["photo3"] = url_for("static", filename="img/IMG_3202.JPG")
    url_dic["photo4"] = url_for("static", filename="img/1.jpg")
    url_dic["photo5"] = url_for("static", filename="img/2.jpg")
    url_dic["photo6"] = url_for("static", filename="img/3.jpg")
    url_dic["photo7"] = url_for("static", filename="img/4.jpg")
    url_dic["photo8"] = url_for("static", filename="img/5.jpg")
    url_dic["photo9"] = url_for("static", filename="img/6.jpg")
    url_dic["photo10"] = url_for("static", filename="img/7.jpg")
    url_dic["photo11"] = url_for("static", filename="img/8.jpg")
    url_dic["photo12"] = url_for("static", filename="img/9.jpg")
    url_dic["photo13"] = url_for("static", filename="img/10.jpg")
    url_dic["photo14"] = url_for("static", filename="img/11.jpg")
    url_dic["photo15"] = url_for("static", filename="img/12.jpg")
    url_dic["photo16"] = url_for("static", filename="img/13.jpg")
    url_dic["photo17"] = url_for("static", filename="img/14.jpg")
    url_dic["css_path"] = url_for("static", filename="css/style.css")
    url_dic["second_ref"] = url_for("my_love")
    url_dic["third_ref"] = url_for("hugs")

    return render_template('index.html', **url_dic)


if __name__ == '__main__':
    url_dic = {}
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
