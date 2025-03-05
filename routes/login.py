from app import *
from models import *
from fasthtml.common import *



@app.get("/login")
def login_view():
    return Div(
        Strong("Holy smokes!", cls='font-bold'),
        Span("Something seriously bad happened.", cls='block sm:inline'),
        role='alert',
        cls='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative'
    )

@app.post("/order")
def login():
    pass