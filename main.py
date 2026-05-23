from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="Templates")

@app.get("/login", response_class=HTMLResponse)
async def mostrar_login(request: Request):

    return templates.TemplateResponse(
        request=request, 
        name="login.html", 
        context={"error": None, "exito": None}
    )

@app.post("/login", response_class=HTMLResponse)
async def procesar_login(
    request: Request, 
    usuario: str = Form(...), 
    contrasena: str = Form(...)
):

    if usuario == "admin" and contrasena == "12345":
        mensaje_exito = f"¡Bienvenido de nuevo, {usuario}!"
        return templates.TemplateResponse(
            request=request, 
            name="login.html", 
            context={"exito": mensaje_exito, "error": None}
        )
    else:
        mensaje_error = "Usuario o contraseña incorrectos. Inténtalo de nuevo."
        return templates.TemplateResponse(
            request=request, 
            name="login.html", 
            context={"error": mensaje_error, "exito": None}
        )