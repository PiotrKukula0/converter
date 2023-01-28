import io
from PIL import Image
from flask import Flask, request, Response
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/jpgtopng", methods=["GET"])
def jpgtopng():
    return render_template("jpgtopng.html")


@app.route("/pngtojpg", methods=["GET"])
def pngtojpg():
    return render_template("pngtojpg.html")


@app.route("/webptopng", methods=["GET"])
def webtopng():
    return render_template("webptopng.html")


@app.route("/bmptopng", methods=["GET"])
def bmptopng():
    return render_template("bmptopng.html")


@app.route("/pngtopdf", methods=["GET"])
def pngtopdf():
    return render_template("pngtopdf.html")


@app.route('/api/jpgtopng', methods=['POST'])
def jpg_to_png():
    # Get image file from request parameters
    image = request.files.get('image')

    # Open image and convert to PNG
    img = Image.open(image)
    img.save('converted.png', 'png')

    # Create response object with converted image as attachment
    with open('converted.png', 'rb') as f:
        response = Response(f.read(), content_type='image/png')
        response.headers.set('Content-Disposition',
                             'attachment', filename='converted.png')
    return response


@app.route("/api/pngtojpg", methods=["POST"])
def convert_png_to_jpg():
    # Get the PNG image from the request
    png_image = request.files.get("image")

    # Open the PNG image using PIL
    image = Image.open(png_image)

    # Convert the image to JPG format
    image = image.convert("RGB")

    # Create a response object with the JPG image
    response = Response(content_type="image/jpeg")
    response.headers["Content-Disposition"] = "attachment; filename=image.jpg"
    image.save(response.stream, "JPEG")

    return response




@app.route("/api/webptopng", methods=["POST"])
def convert_webp_to_png():
    # Get the WEBP image from the request
    webp_image = request.files.get("image")

    # Open the WEBP image using PIL
    image = Image.open(webp_image)

    # Convert the image to PNG format
    image.save("converted.png", "PNG")

    # Create a response object with the PNG image
    response = Response(content_type="image/png")
    response.headers["Content-Disposition"] = "attachment; filename=image.png"
    with open("converted.png", "rb") as f:
        response.data = f.read()
    return response


@app.route("/api/bmptopng", methods=["POST"])
def convert_bmp_to_png():
    # Get the BMP image from the request
    bmp_image = request.files.get("image")

    # Open the BMP image using PIL
    image = Image.open(bmp_image)

    # Convert the image to PNG format
    image.save("converted.png", "PNG")

    # Create a response object with the PNG image
    response = Response(content_type="image/png")
    response.headers["Content-Disposition"] = "attachment; filename=image.png"
    with open("converted.png", "rb") as f:
        response.data = f.read()
    return response


@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    image = request.files["image"]
    img = Image.open(image)
    byte_io = io.BytesIO()
    img.save(byte_io, 'PDF')
    byte_io.seek(0)
    response = Response(byte_io, content_type='application/pdf')
    response.headers.set("Content-Disposition", "attachment", filename="converted_file.pdf")
    return response


if __name__ == "__main__":
    app.run(debug=True)
