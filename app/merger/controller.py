from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import secure_filename
from app import merger
from flask import Blueprint, request, current_app, redirect
import os
import time

merger_blueprint = Blueprint('merger', __name__, url_prefix="/merger",
                             static_folder="../static", template_folder="../templates/merger")


@merger_blueprint.route('/')
def index():
    return render_template('index.html.j2')


@merger_blueprint.route('<folderid>/arrange/')
def arrange(folderid):
    print('here')
    return render_template('arrange.html.j2', id=folderid)


@merger_blueprint.route('<folderid>/upload', methods=['GET', 'POST'])
def upload(folderid):
    folder = current_app.config['UPLOAD_FOLDER'] + folderid
    if request.method == 'POST':
        if not os.path.exists(folder):
            os.makedirs(folder)

        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(folder, f.filename))
                print("Uploaded...", f.filename)
        return render_template('arrange.html.j2', id=folderid)
    else:
        return render_template('upload.html.j2', id=folderid)
