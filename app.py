from fasthtml.common import *

myHeaders = [
    Meta(charset='UTF-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1'),
    Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css'),
    picolink,  # PicoCSS (Optional)
    Style(':root { --pico-font-size: 100%; }'),  # Default styles
]

# Creating FastAPI App
app = FastHTML(hdrs=myHeaders)

# Mounting the static folder for accessing the menu.css
app.mount("/static", StaticFiles(directory="Mani-Kukuraya/static"), name="static")