# from app import *
# import routes

# serve()

from fasthtml.common import *

app, rt = fast_app(
    hdrs=(
        Script("https://unpkg.com/@tailwindcss/browser@4"),  # Load Tailwind CDN
    )
)

@rt("/")
def get():
    return Div("Hello, Tailwind!", cls="text-2xl font-bold text-blue-500")

serve()
