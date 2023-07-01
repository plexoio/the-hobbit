import os
from flask import Flask  # first import Class from module

# instance of the class passing __name__ (provides current module or script)
app = Flask(__name__)


@app.route("/")  # help direct the files to Flask
def index():
    return "Hello, world!"


# This condition ensures that the subsequent
# code block is only executed when run.py is the main entry point.
if __name__ == "__main__":  # when executed directly
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),  # replace if not found
        port=int(os.environ.get('PORT', '5000')),  # replace if not found
        debug=True  # caution security flaw if True
    )