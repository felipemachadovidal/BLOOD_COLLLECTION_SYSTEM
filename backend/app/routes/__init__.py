from flask import Blueprint

# Importação dos outros blueprints
from .auth import auth_bp
from .user import user_bp
from .collection_point import collection_point_bp

# Criação de um blueprint para a rota raiz
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return "Backend is running!"

# Adicione os blueprints no pacote routes
__all__ = ['auth_bp', 'user_bp', 'collection_point_bp', 'main_bp']
