from fasthtml.common import *
from utils import *

app, rt = fast_app(live=True)

@app.get("/")
def home():
    return P("HEGawaefaefA")

# @app.get("/kuy")
@rt("/kuy")
def get():
    return hello()

serve()