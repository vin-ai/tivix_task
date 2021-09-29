import graphene

import school.schema


class Query(school.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(school.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
