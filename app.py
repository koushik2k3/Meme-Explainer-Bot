from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from lib import *
from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    raise ValueError("OpenAI API key not found in environment variables")

# Now you can use the API key
print("Your OpenAI API Key is:", openai_api_key)


app = Flask(__name__)

CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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
    app.run()


