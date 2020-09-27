import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from book.models import Category, Publisher, Author, Book


# Create a GraphQL type for the category model
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


# Create a GraphQL type for the publisher model
class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher


# Create a GraphQL type for the author model
class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


# Create a GraphQL type for the book model
class BookType(DjangoObjectType):
    class Meta:
        model = Book


# Create a query type
class Query(ObjectType):

    category = graphene.Field(CategoryType, id=graphene.Int())
    publisher = graphene.Field(PublisherType, id=graphene.Int())
    author = graphene.Field(AuthorType, id=graphene.Int())
    book = graphene.Field(BookType, id=graphene.Int())

    category_list = graphene.List(CategoryType)
    publisher_list = graphene.List(PublisherType)
    author_list = graphene.List(AuthorType)
    book_list = graphene.List(BookType)

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)

        return None

    def resolve_publisher(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Publisher.objects.get(pk=id)

        return None

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Author.objects.get(pk=id)

        return None

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Book.objects.get(pk=id)

        return None

    def resolve_category_list(self, info, **kwargs):
        return Category.objects.all()

    def resolve_publisher_list(self, info, **kwargs):
        return Publisher.objects.all()

    def resolve_author_list(self, info, **kwargs):
        return Author.objects.all()

    def resolve_book_list(self, info, **kwargs):
        return Book.objects.all()


# Create Input Object Types
class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class PublisherInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    lastName = graphene.String()
    firstName = graphene.String()


class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    category = graphene.ID()
    publisher = graphene.ID()
    author = graphene.ID()


# Create mutations for category
class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        category_instance = Category(name=input.name)
        category_instance.save()
        return CreateCategory(ok=ok, category=category_instance)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        category_instance = Category.objects.get(pk=id)
        if category_instance:
            ok = True
            category_instance.name = input.name
            category_instance.save()
            return UpdateCategory(ok=ok, category=category_instance)
        return UpdateCategory(ok=ok, category=None)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        category_instance = Category.objects.get(pk=id)
        if category_instance:
            ok = True
            category_instance.delete()
            return DeleteCategory(ok=ok)
        return DeleteCategory(ok=ok)


# Create mutations for publisher
class CreatePublisher(graphene.Mutation):
    class Arguments:
        input = PublisherInput(required=True)

    ok = graphene.Boolean()
    publisher = graphene.Field(PublisherType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        publisher_instance = Publisher(name=input.name)
        publisher_instance.save()
        return CreatePublisher(ok=ok, publisher=publisher_instance)


class UpdatePublisher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PublisherInput(required=True)

    ok = graphene.Boolean()
    publisher = graphene.Field(PublisherType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        publisher_instance = Publisher.objects.get(pk=id)
        if publisher_instance:
            ok = True
            publisher_instance.name = input.name
            publisher_instance.save()
            return UpdatePublisher(ok=ok, publisher=publisher_instance)
        return UpdatePublisher(ok=ok, publisher=None)


class DeletePublisher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        publisher_instance = Publisher.objects.get(pk=id)
        if publisher_instance:
            ok = True
            publisher_instance.delete()
            return DeletePublisher(ok=ok)
        return DeletePublisher(ok=ok)


# Create mutations for author
class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        author_instance = Author(
            last_name=input.lastName,
            first_name=input.firstName
        )
        author_instance.save()
        return CreateAuthor(ok=ok, author=author_instance)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        author_instance = Author.objects.get(pk=id)
        if author_instance:
            ok = True
            author_instance.last_name = input.lastName
            author_instance.first_name = input.firstName
            author_instance.save()
            return UpdateAuthor(ok=ok, author=author_instance)
        return UpdateAuthor(ok=ok, author=None)


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        author_instance = Author.objects.get(pk=id)
        if author_instance:
            ok = True
            author_instance.delete()
            return DeleteAuthor(ok=ok)
        return DeleteAuthor(ok=ok)


# Create mutations for book
class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        category_lookup = None
        publisher_lookup = None
        author_lookup = None
        categoryId = int(input.category)
        publisherId = int(input.publisher)
        authorId = int(input.author)
        if categoryId != 0:
            category_lookup = Category.objects.get(pk=categoryId)
        if publisherId != 0:
            publisher_lookup = Publisher.objects.get(pk=publisherId)
        if authorId != 0:
            author_lookup = Author.objects.get(pk=authorId)
        book_instance = Book(
            title=input.title,
            category=category_lookup,
            publisher=publisher_lookup,
            author=author_lookup
        )
        book_instance.save()
        return CreateBook(ok=ok, book=book_instance)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False

        book_instance = Book.objects.get(pk=id)
        if book_instance:
            ok = True
            category_lookup = None
            publisher_lookup = None
            author_lookup = None
            categoryId = int(input.category)
            publisherId = int(input.publisher)
            authorId = int(input.author)
            if categoryId != 0:
                category_lookup = Category.objects.get(pk=categoryId)
            if publisherId != 0:
                publisher_lookup = Publisher.objects.get(pk=publisherId)
            if authorId != 0:
                author_lookup = Author.objects.get(pk=authorId)
            book_instance.title = input.title
            book_instance.category = category_lookup
            book_instance.publisher = publisher_lookup
            book_instance.author = author_lookup
            book_instance.save()
            return UpdateBook(ok=ok, book=book_instance)
        return UpdateBook(ok=ok, book=None)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id, input=None):
        book_instance = Book.objects.get(pk=id)
        if book_instance:
            ok = True
            book_instance.delete()
            return DeleteBook(ok=ok)
        return DeleteBook(ok=ok)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    create_publisher = CreatePublisher.Field()
    update_publisher = UpdatePublisher.Field()
    delete_publisher = DeletePublisher.Field()
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
