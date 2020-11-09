import os
import numpy as np
from PIL import Image
from pathlib import Path
from datetime import datetime
from werkzeug.utils import secure_filename
from feature_extractor import FeatureExtractor
from flask import Flask, render_template, request, redirect

import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'





fe = FeatureExtractor()

app = Flask(__name__)


UPLOAD_FOLDER = './static/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



app.config['UPLOAD_FOLDER']	= UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 12 * 1024 * 1024



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS







@app.route('/')
def login():
	return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def uploader():


	cred = []
	for key, value in request.form.items():
		cred.append(value)
	uname = cred[0]
	upass = cred[1]
	if request.method == 'POST' and uname == 'a' and upass == 'b':

		return render_template("uploader.html")
	else:
		return render_template("login.html")






@app.route('/uploader', methods=['POST'])
def upload_file():


    if request.method == 'POST':

        if 'files[]' not in request.files:
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #for img_path in sorted(Path("./static/img").glob("*.jpg")):
        #	feature = fe.extract(img=Image.open(img_path))
        #	feature_path = Path("./static/feature") / (img_path.stem + ".npy")
        #	np.save(feature_path, feature)

        return render_template("similar_image.html")







@app.route('/similar_image', methods=['GET', 'POST'])
def index():


	if request.method == 'POST':
		features = []
		img_paths = []
		for feature_path in Path("./static/feature").glob("*.npy"):
			features.append(np.load(feature_path))
			img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
		features = np.array(features)
		file = request.files['query_img']
		img = Image.open(file.stream)
		uploaded_img_path = "./static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
		img.save(uploaded_img_path)
		query = fe.extract(img)
		dists = np.linalg.norm(features-query, axis=1)
		ids = np.argsort(dists)[1:10]
		scores = [(dists[id], img_paths[id]) for id in ids]
		return render_template('similar_image.html',
                               query_path=uploaded_img_path,
                               scores=scores)
	else:
		return render_template('similar_image.html')






if __name__ == '__main__':
	app.run(debug = True)

