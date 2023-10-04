import os

from pathlib import Path
import sys
path_root = Path(__file__).parents[0]
sys.path.append(str(path_root))

from src import main
from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    return (main.run(), 200)


if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080
    app.run(host="127.0.0.1", port=PORT, debug=True)