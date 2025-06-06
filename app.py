import datetime

import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, validators
import os
from modifier import Hitap
from pdfmaker import thedilekce

app = Flask(__name__)
SECRET_KEY = 61
app.config['SECRET_KEY'] = 61 # :-)


class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')


class ThePage(MethodView):

    def get(self):
        conditioner = 0
        form = InfoForm()
        return render_template("index.html", form=form, conditioner=conditioner)

    def post(self):
        isim = request.form.get("isim")
        soyisim = request.form.get("soyisim")
        adres = request.form.get("adres")
        ilce = request.form.get("ilce")
        il = request.form.get("il")
        telno = request.form.get("telno")
        eposta = request.form.get("eposta")

        teslimtarihi = request.form.get("teslimtarihi")
        teslimtarihi = datetime.datetime.strptime(teslimtarihi, '%Y-%m-%d')
        teslimtarihi = teslimtarihi.strftime("%d.%m.%Y")

        teslimmakami_str = request.form.get("teslimmakami")
        teslimmakami_obj = Hitap()
        # teslimmakami_son = teslimmakami_obj.teslimmakami(hitaben=teslimmakami_str)

        ek1 = request.form.get("ek1")
        ek2 = request.form.get("ek2")
        ek3 = request.form.get("ek3")
        ek4 = request.form.get("ek4")
        ek5 = request.form.get("ek5")

        dilekce = request.form.get("dilekcemetni")

        """radioVal kısmı"""
        radioVal = request.form['radio']

        pdfkodu = thedilekce(isim=isim, soyisim=soyisim, adres=adres, ilce=ilce, il=il,
                             telno=telno, eposta=eposta, teslimmakami=teslimmakami_str,
                             tarih=teslimtarihi, metin=dilekce, ek1=ek1, ek2=ek2, ek3=ek3, ek4=ek4,
                             ek5=ek5, radioVal=radioVal).pdfolustur()

        conditioner = 1
        self.adres = adres

        return render_template("index.html", pdfkodu=pdfkodu, conditioner=conditioner)


class AnaSayfa(MethodView):

    def get(self):
        return render_template("mainpage.html")


class OrnekDilekce(MethodView):

    def get(self):
        return render_template("theexamplepage.html")

class Visitor(MethodView):

    def get(self):
        conditioner2 = 0
        # print(db)
        return render_template("visitorpage.html", conditioner2=conditioner2)

    #
    def post(self):


        db = mysql.connector.connect(
            host='localhost',
            user='seribbag_seribbag',
            password='^*XuCr-#dtB6',
            database='seribbag_visitorschema'
        )

        # Retrieve form data from request
        email = request.form['email']
        comment = request.form['comment']

        # screenshot = request.files['screenshot']:
        # file saving
        file = request.files['screenshot']
        screenshot = file.filename
        # screenshot.decode('utf-8')

        radio = request.form['radio']
        iban = request.form['iban']
        fullname = request.form['fullname']

        # Save the file to a desired location
        # file.save('C:/Users/Aymam/Desktop/SWE Documentation/Docs/FLASK/seridilekce_RENEWAL/p2. mysqlconnection/static/screenshot.jpg')
        try:
        
            screenshot = screenshot.encode('ascii', 'ignore').decode('ascii')
            d = f"/home/seribbag/public_html/static/images/{screenshot}"
            file.save(d)

        except:
            print("passed")


        # Create a cursor to interact with the database
        cursor = db.cursor()

        # Construct the SQL query and execute
        query = "INSERT INTO comment_table (email, comment, screenshot, radio, iban, fullname) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (email, comment, screenshot, radio, iban, fullname)
        cursor.execute(query, values)
        

        # Commit the changes and close the cursor
        db.commit()
        cursor.close()

        # Redirect to a thank you page or any desired page
        conditioner2 = 1
        return render_template('visitorpage.html', conditioner2=conditioner2)


app.add_url_rule('/', view_func=AnaSayfa.as_view('Ana Sayfa'))
app.add_url_rule('/dilekceyaz', view_func=ThePage.as_view('Our Page'), methods=["GET", "POST"])
app.add_url_rule('/ornekdilekce', view_func=OrnekDilekce.as_view('Örnek Dilekçe'))
app.add_url_rule('/yorum', view_func=Visitor.as_view('Yorum'), methods=["GET", "POST"])

if __name__ == '__main__':
    app.run()

"""DEĞİŞİKLER"""
"""1. zorunlu değil eklendi"""
"""?? Galaxy fold için eklemelerin yapılması gerekli"""
