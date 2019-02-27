import graphene

import links.schema
import users.schema
import graphene
import graphql_jwt
import links.schema_relay


class Query(users.schema.Query, links.schema.Query,
            links.schema_relay.RelayQuery, graphene.ObjectType):
    pass


class Mutation(
        links.schema.Mutation,
        users.schema.Mutation,
        graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
