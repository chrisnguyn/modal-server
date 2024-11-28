from modal import App, Image, Secret, Volume, wsgi_app

from src.create_flask_app import create_flask_app

image = Image.debian_slim().pip_install_from_requirements("requirements.txt")
app = App("modal-server", image=image)
secrets = Secret.from_name("modal-server-secrets")
volume = {"/app": Volume.from_name("modal-server-volume")}


@app.function(secrets=[secrets], image=image)
@wsgi_app()
def entrypoint():
    return create_flask_app()
