from app import *
from models import *
from fasthtml.common import *
from starlette.exceptions import HTTPException

@app.get("/login")
def login_page():
    return Container(
        H1("Login"),
        Form(
            Input(name="username", placeholder="Username", required=True),
            Input(name="password", type="password", placeholder="Password", required=True),
            Button("Login", type="submit", hx_post="/login", hx_target="#error-message", hx_swap="innerHTML"),
            Div(id="error-message", style="color: red; margin-top: 10px;")  # Error message
        )
    )


@app.post("/login")
def login(username: str, password: str, sess):
    user = controller.get_user_by_username(username)
    if user and user.password == password:
        sess["auth"] = username  # Store user session
        return Response(headers={"HX-Redirect": "/home"}, media_type="text/html")  # Redirect after login
    return P("❌ Invalid username or password!", style="color: red;")



@app.get("/logout")
def logout(sess):
    del sess["auth"]  # Remove authentication session
    return RedirectResponse("/login")  # Redirect to login page