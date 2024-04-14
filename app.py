from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from libv2 import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class UploadForm(FlaskForm):
    image = FileField('Image')
    submit = SubmitField('Upload')

@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/project', methods=['GET', 'POST'])
def project():
    form = UploadForm()
    caption = None
    image = None
    if form.validate_on_submit():
        image_file = request.files['image']
        image_file.save('static/images/' + image_file.filename)
        image_path = 'static/images/' + image_file.filename
        # caption = get_description(image_path)
        template=detect(image_path)
        text = extract_text(image_path)
        caption=generate_meme_explanation(template, text)
        image = 'saved_image.jpg'
    return render_template('index.html', form=form, caption=caption, image=image)

@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    return render_template('aboutUs.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contactUs.html')

if __name__ == '__main__':
    app.run(port=2000)


