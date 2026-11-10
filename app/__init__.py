"""Factoría de la aplicación web Flask para Inventario DSL."""

from flask import Flask


def create_app() -> Flask:
    """Crea la aplicación y registra sus rutas."""
    app = Flask(__name__)

    from app.routes import web

    app.register_blueprint(web)
    return app
