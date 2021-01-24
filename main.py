import os
from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/receive",methods = ["POST"])
def rec():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(filename))
    return "saved"

if __name__ == "__main__":
    app.run(host = "localhost" , port = "9000")


