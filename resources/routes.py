from resources.books import BookApi, BooksApi
from resources.authors import AuthorApi, AuthorsApi
from resources.auth import Login, Register

def initialize_routes(api):
    api.add_resource(BooksApi, '/api/books')
    api.add_resource(BookApi, '/api/books/<int:bookId>')
    api.add_resource(AuthorsApi, '/api/authors')
    api.add_resource(AuthorApi, '/api/authors/<int:authorId>')
    api.add_resource(Login, '/auth/login')
    api.add_resource(Register, '/auth/register')