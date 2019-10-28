import flask_rebar
from flask_rebar import errors

from app.app import v1_registry
from app.entities.author import Author
from app.services import author as author_service
from app.schemas.request.author import BookRequestSchema
from app.schemas.response.author import BookResponseSchema


@v1_registry.handles(
    rule="/author",
    method="POST",
    response_body_schema={201: BookResponseSchema()},
    request_body_schema=BookRequestSchema(),
)
def create_account():
    body = flask_rebar.get_validated_body()
    author = Author(**body)
    author = author_service.save(author)
    return author, 201


@v1_registry.handles(
    rule="/author/<int:author_id>",
    method="GET",
    response_body_schema=BookResponseSchema()
)
def get_account(author_id: int):
    author = author_service.get_by_id(author_id)
    if author is None:
        raise errors.NotFound()

    return author
