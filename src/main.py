from modal import Image, Stub, Secret, Volume

from src.create_flask_app import create_flask_app

image = Image.debian_slim().pip_install_from_requirements("requirements.txt")
stub = Stub("modal-server", image=image)
secrets = Secret.from_name("modal-server-secrets")
volume = {"/app": Volume.new()}


@stub.function(secrets=[secrets], image=image)
def entrypoint():
    return create_flask_app()
