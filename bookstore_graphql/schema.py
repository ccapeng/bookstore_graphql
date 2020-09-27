import graphene
import book.schema


class Query(book.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(book.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
