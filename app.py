import io
from io import BytesIO
from flask import request, jsonify, send_file
from flask import Flask
import base64
import os
from PIL import Image
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Fastest Image Processing in Python !'

@app.route('/v1/image/resizeB64', methods=['POST'])
def resizeB64():
    imageStr = request.json['image']
    size = (128, 128)
    imgdata = base64.b64decode(str(imageStr))
    image = Image.open(io.BytesIO(imgdata))
    output = BytesIO()
    image.thumbnail(size)
    image.save(output, "JPEG")
    encoded_image = base64.b64encode(output.getvalue())
    print(encoded_image)
    return jsonify({'image': encoded_image.decode()})


@app.route('/v1/image/resize', methods=['POST'])
def resize():

    file = request.files['file']
    height = int(request.args.get('height'))
    width = int(request.args.get('width'))
    if height is None:
            return jsonify({"error" : "height attribut is mendator"}),400
    if width is None:
            return jsonify({"error" : "width attribut is mendator"}),400
    if file is None:
            return jsonify({"error" : "file is mendator"}),400        
    size = (width, height)
    image = Image.open(file)
    output = BytesIO()
    image.thumbnail(size)
    image.save(output, "JPEG")
    output.seek(0)
    return send_file(
        output,
        attachment_filename='thumbnail.jpeg',
        mimetype='image/jpeg',
        as_attachment=True
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run()
