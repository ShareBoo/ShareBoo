import graphene

from graphene_django.types import DjangoObjectType

from shareboo.models import User, Book


class UserType(DjangoObjectType):
    class Meta:
        model = User


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(object):
    all_users = graphene.List(UserType)
    all_twitter_users = graphene.List(UserType)
    all_books = graphene.List(BookType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_twitter_users(self, info, **kwargs):
        return User.objects.filter(photo_url="https://image.com/twitter.png")

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()
