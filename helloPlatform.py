from flask import Flask
import platform
app = Flask(__name__)


def renderArchitecture():
    pf = str(platform.platform())
    uname = str(platform.uname())
    xs = f"{pf}<p>{uname}"
    return(xs)

@app.route("/")
def hello_world():
    p_str = renderArchitecture()
    return "<h1><p>Hello, there!</p></h1><h2>Your platform:</h2> " + p_str