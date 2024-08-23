from .auth import auth_bp
from .user import user_bp
from .collection_point import collection_point_bp

# Adicione os blueprints no pacote routes
__all__ = ['auth_bp', 'user_bp', 'collection_point_bp']
