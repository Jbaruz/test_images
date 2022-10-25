from distutils.log import error
import os

from flask import redirect, render_template, request, flash, session, send_from_directory, url_for
from flask_base import app
from datetime import datetime
from flask_base.models.images import Image
from flask_base.models.newsletter import News

from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/process_news', methods=['GET','POST'])
def process_news():
    if request.method == 'POST':
        print(request.form)
        if not News.validar(request.form):
            return redirect('/')
        print('in post of file')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename =f"{int(datetime.utcnow().timestamp())}{secure_filename(file.filename)}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    new_noticia={
        'title':request.form['title'],
        'resume':request.form['resume'],
        'category':request.form['category'],
        'content':request.form['content'],
    }
    noticia=News.save(new_noticia)
    print("VER AQUIII 33333--->", noticia)
    
    new_image={
        'name': filename,
        'new_id':noticia,
    }
    print("VER IMAGE 44444--->",new_image)
    image = Image.save(new_image)
    if noticia == False:
        flash('algo errado paso con la creacion de la noticia', 'error')
        return redirect ('/contact')
    flash('Exito al crear nueva noticia', 'success')
    return redirect('/')

