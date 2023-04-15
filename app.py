from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from lib import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class UploadForm(FlaskForm):
    image = FileField('Image')
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadForm()
    caption = None
    image = None
    if form.validate_on_submit():
        image_file = request.files['image']
        image_file.save('static/images/' + image_file.filename)
        image = image_file.filename
        image_path = 'static/images/' + image_file.filename
        caption = get_description(image_path)
    return render_template('index.html', form=form, caption=caption, image=image)

if __name__ == '__main__':
    app.run()


