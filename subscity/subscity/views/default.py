from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from subscity.models import Cinema
import json

@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(Cinema)
        result = query.first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'result': result.name}


db_err_msg = "Pyramid is having a problem using your SQL database."
