from fasthtml.common import *
from starlette.responses import RedirectResponse


myHeaders = [
    Meta(charset='UTF-8'),
    Meta(name='viewport', content='width=device-width, initial-scale=1'),
    Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css'),
    Link(rel="stylesheet", href="/static/styles.css"),  # Load external CSS
    picolink,  # PicoCSS (Optional)
    Style(':root { --pico-font-size: 100%; }'),  # Default styles
]


def before(req, sess):
    print(sess)
    if "auth" not in sess:
        return RedirectResponse("/login")  # Redirect to login page

bware = Beforeware(before, skip=["/login", "/static/.*"])  # Allow login & static files

# Creating FastAPI App
app = FastHTML(hdrs=myHeaders, live=True, before=bware)

# Mounting the static folder for accessing the menu.css
app.mount("/static", StaticFiles(directory="static"), name="static")