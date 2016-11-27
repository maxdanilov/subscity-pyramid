from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from subscity.models.meta import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config.scan()
    return config.make_wsgi_app()
