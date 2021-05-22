from fastapi import FastAPI, File, UploadFile
import numpy as np
from turbojpeg import TurboJPEG
import tensorflow as tf
import cv2

import os
os.chdir('..')

# Initialize necessary components
app = FastAPI()
turbojpeg = TurboJPEG()
model = tf.saved_model.load('weights/mobilenet_hd/')
preproc_model = tf.saved_model.load('weights/preproc/')

infer = model.signatures['serving_default']
preproc = preproc_model.signatures['serving_default']

labels = {
    0: 'not hot dog',
    1: 'hot dog'
}

@app.post('/image')
async def get_index(file: UploadFile = File(...)):
    contents = await file.read()
    # img_buffer = np.frombuffer(contents, dtype=np.uint8)
    # img = turbojpeg.decode(img_buffer)
    # img = cv2.imdecode(img_buffer, cv2.IMREAD_COLOR)
    
    img = tf.io.decode_jpeg(contents)
    img_pre = tf.expand_dims(img, axis=0)
    img_pre = preproc(img_pre)['output_0']
    preds = tf.squeeze(infer(img_pre)['outputs'], axis=0)
    
    return {
        'prediction': labels[preds.numpy().argmax()],
        'score': round(float(preds.numpy().max()) * 100, 2)
    }