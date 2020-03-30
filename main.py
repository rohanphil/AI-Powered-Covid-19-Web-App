from flask import Flask, render_template, request
from io import BytesIO
import tensorflow as tf
from keras.preprocessing import image
from keras.preprocessing.image import array_to_img, img_to_array
from keras.models import load_model
import os
from PIL import Image
import numpy as np
from base64 import b64encode

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import cv2

# code which helps initialize our server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'

bootstrap = Bootstrap(app)

saved_model = tf.keras.models.load_model("model/covid19.h5")
saved_model._make_predict_function()

class UploadForm(FlaskForm):
    photo = FileField('Upload an image',validators=[FileAllowed(['jpg', 'png', 'jpeg'], u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Predict')

def preprocess(img):
    width, height = img.shape[0], img.shape[1]
    img = image.array_to_img(img, scale=False)

    desired_width, desired_height = 100, 100

    if width < desired_width:
     desired_width = width
    start_x = np.maximum(0, int((width-desired_width)/2))

    img = img.crop((start_x, np.maximum(0, height-desired_height), start_x+desired_width, height))
    img = img.resize((100, 100))

    img = image.img_to_array(img)
    return img / 255.

@app.route('/', methods=['GET','POST'])
def predict():
    form = UploadForm()
    if form.validate_on_submit():
     print(form.photo.data)
     image_stream = form.photo.data.stream
     original_img = Image.open(image_stream)
     print(type(original_img))
     #image = cv2.imread(image_stream)
     image = np.array(original_img)
     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     image = cv2.resize(image, (224,224))
     image = image/255
     image = np.expand_dims(image, axis = 0)
     prediction = saved_model.predict(image)

     print(prediction)

     if (prediction[0][0]>prediction[0][1]):
       result = "Possibility of Covid-19 infection"
     else:
       result = "Unlikely to be infected by Covid-19"

     byteIO = BytesIO()
     original_img.save(byteIO, format=original_img.format)
     byteArr = byteIO.getvalue()
     encoded = b64encode(byteArr)

     return render_template('result.html', result=result, encoded_photo=encoded.decode('ascii'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)