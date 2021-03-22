import os

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/my_love")
def my_love():
    global url_dic
    url_dic["love_1"] = url_for("static", filename="img/love_1.png")
    url_dic["love_2"] = url_for("static", filename="img/love_2.png")
    return render_template("second_page.html", **url_dic)


@app.route("/")
def love():
    global url_dic
    url_dic["photo1"] = url_for("static", filename="img/IMG_3205.JPG")
    url_dic["photo2"] = url_for("static", filename="img/IMG_3200.JPG")
    url_dic["photo3"] = url_for("static", filename="img/IMG_3202.JPG")
    url_dic["photo4"] = url_for("static", filename="img/1.JPG")
    url_dic["photo5"] = url_for("static", filename="img/2.JPG")
    url_dic["photo6"] = url_for("static", filename="img/3.JPG")
    url_dic["photo7"] = url_for("static", filename="img/4.JPG")
    url_dic["photo8"] = url_for("static", filename="img/5.JPG")
    url_dic["photo9"] = url_for("static", filename="img/6.JPG")
    url_dic["photo10"] = url_for("static", filename="img/7.JPG")
    url_dic["photo11"] = url_for("static", filename="img/8.JPG")
    url_dic["photo12"] = url_for("static", filename="img/9.JPG")
    url_dic["photo13"] = url_for("static", filename="img/10.JPG")
    url_dic["photo14"] = url_for("static", filename="img/11.JPG")
    url_dic["photo15"] = url_for("static", filename="img/12.JPG")
    url_dic["photo16"] = url_for("static", filename="img/13.JPG")
    url_dic["photo17"] = url_for("static", filename="img/14.JPG")
    url_dic["css_path"] = url_for("static", filename="css/style.css")
    url_dic["second_ref"] = url_for("my_love")

    return render_template('index.html', **url_dic)


if __name__ == '__main__':
    url_dic = {}
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
