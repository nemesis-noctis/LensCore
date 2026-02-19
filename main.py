import os
import random
import threading
import time
import uuid

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import HiddenField, SubmitField
from wtforms.validators import DataRequired

from lens_core import LensCore

load_dotenv("./.env")

AZURE_VISION_API_KEY = os.getenv("VISION_KEY")

class ImgFileForm(FlaskForm):
    img_file = FileField("Image File", validators=[FileRequired()])
    lang = HiddenField(validators=[DataRequired()])
    submit = SubmitField("Submit")

def search_song(img_file_path, lang, attempts):
    '''
    Searches for songs in the selected language using LensCore and returns a Song object.
    Performs a number of attempts and, if an error occurs or no songs are found for the image, returns None.
    
    :param img_file_path: Path to the folder where the image is located.
    
    :param lang:  Language for searching tags.
    
    :param attempts: Attempts to find the song before returning None.
    '''
    while attempts > 0:
        lens_core = LensCore(AZURE_VISION_API_KEY)

        tags_list = lens_core.get_tags_from_img(img_file_path=img_file_path, lang=lang)
        if tags_list is None:
            attempts = 0
            break
        
        tags_to_search = lens_core.select_tags_to_search(tags_list)
    
        search_response = lens_core.search_songs(tags_to_search)
        if search_response is None:
            attempts -= 1  
            
        else:
            return random.choice(search_response)
        
    if attempts == 0:
        return None


def delete_img(img_path, delay):
    '''
    Deletes the image uploaded by the user after a delay in seconds.
    
    :param img_path: Path of the image to be deleted.
    :param delay: Time until the image is deleted.
    '''
    time.sleep(delay)
    os.remove(img_path)


app = Flask(__name__)
app.config['SECRET_KEY'] = uuid.uuid4().hex


@app.route("/" )
def home():  
    form = ImgFileForm(lang="pt")
    return render_template("./index.html", form = form)


@app.route("/en")
def home_en():
    form = ImgFileForm(lang="en")
    return render_template("./index_en.html", form = form)


@app.route("/song-recommendation", methods=["POST"])
def song_recommendation():
    form = ImgFileForm()
    
    if form.validate_on_submit():
        images_path = "./static/temp_img/"
        lang = form.lang.data
        accepted_langs = ["en", "pt"]
        if lang not in accepted_langs:
            return redirect(url_for("home")) 
        
        original_filename = secure_filename(form.img_file.data.filename)
        filename = f"{uuid.uuid4().hex}-{original_filename}"
        
        img_file_path = images_path + filename
        form.img_file.data.save(img_file_path)
        
        searched_song = search_song(img_file_path, lang=lang, attempts=20)
        thread = threading.Thread(target=delete_img, args=(img_file_path, 20))
        thread.start()
        
        if searched_song is None:
            errors_per_lang = {"en": "An Error occured or no song found, please try to upload another Image or change language.", 
                               "pt": "Ocorreu um erro ou nenhuma música foi encontrada. Por favor, tente enviar outra imagem ou mude o idioma."}
            
            error = errors_per_lang[lang]
            
            if lang == "en":
                flash(error)
                return redirect(url_for("home_en"))
            
            flash(error)
            return redirect(url_for("home"))
        
        else:
            if lang == "en":
                return render_template("./song_en.html", song=searched_song, original_img = img_file_path)
            
            return render_template("./song.html", song=searched_song, original_img = img_file_path)
    
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
