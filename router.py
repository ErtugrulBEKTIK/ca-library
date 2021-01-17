from routes.auth import Login, Register
from routes.admin.books import AdminBook, AdminBooks
from routes.admin.authors import AdminAuthor, AdminAuthors
from routes.admin.users import AdminUser, AdminUsers, AdminList
from routes.admin.categories import AdminCategory, AdminCategories
from routes.admin.comments import AdminComment, AdminComments
from routes.public import PublicBooks, PublicCategories
from routes.profile.detail import ProfileDetail
from routes.profile.changePassword import ProfilePassword
from routes.profile.bookings import ProfileBookings
from routes.profile.wishes import ProfileWishes, ProfileNotifications
from routes.profile.comments import ProfileComments
from routes.public import PublicComments

def initialize_routes(api):
    api.add_resource(Login, '/auth/login')
    api.add_resource(Register, '/auth/register')
    api.add_resource(AdminBooks, '/admin/books')
    api.add_resource(AdminBook, '/admin/books/<int:bookId>')
    api.add_resource(AdminAuthors, '/admin/authors')
    api.add_resource(AdminAuthor, '/admin/authors/<int:authorId>')
    api.add_resource(AdminUsers, '/admin/users')
    api.add_resource(AdminList, '/admin/admin-list')
    api.add_resource(AdminUser, '/admin/users/<int:userId>')
    api.add_resource(AdminCategories, '/admin/categories')
    api.add_resource(AdminCategory, '/admin/categories/<int:categoryId>')
    api.add_resource(AdminComments, '/admin/comments')
    api.add_resource(AdminComment, '/admin/comments/<int:commentId>')
    api.add_resource(PublicBooks, '/public/books')
    api.add_resource(PublicCategories, '/public/categories')
    api.add_resource(ProfileDetail, '/profile/detail')
    api.add_resource(ProfilePassword, '/profile/changePassword')
    api.add_resource(ProfileBookings, '/profile/bookings')
    api.add_resource(ProfileWishes, '/profile/wishes')
    api.add_resource(ProfileNotifications, '/profile/notifications')
    api.add_resource(ProfileComments, '/profile/comments')
    api.add_resource(PublicComments, '/public/comments/<int:bookId>')
