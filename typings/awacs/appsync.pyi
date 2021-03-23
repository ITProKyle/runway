"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS AppSync"
prefix = "appsync"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

CreateApiKey = Action("CreateApiKey")
CreateDataSource = Action("CreateDataSource")
CreateFunction = Action("CreateFunction")
CreateGraphqlApi = Action("CreateGraphqlApi")
CreateResolver = Action("CreateResolver")
CreateType = Action("CreateType")
DeleteApiKey = Action("DeleteApiKey")
DeleteDataSource = Action("DeleteDataSource")
DeleteFunction = Action("DeleteFunction")
DeleteGraphqlApi = Action("DeleteGraphqlApi")
DeleteResolver = Action("DeleteResolver")
DeleteType = Action("DeleteType")
GetDataSource = Action("GetDataSource")
GetFunction = Action("GetFunction")
GetGraphqlApi = Action("GetGraphqlApi")
GetIntrospectionSchema = Action("GetIntrospectionSchema")
GetResolver = Action("GetResolver")
GetSchemaCreationStatus = Action("GetSchemaCreationStatus")
GetType = Action("GetType")
GraphQL = Action("GraphQL")
ListApiKeys = Action("ListApiKeys")
ListDataSources = Action("ListDataSources")
ListFunctions = Action("ListFunctions")
ListGraphqlApis = Action("ListGraphqlApis")
ListResolvers = Action("ListResolvers")
ListResolversByFunction = Action("ListResolversByFunction")
ListTagsForResource = Action("ListTagsForResource")
ListTypes = Action("ListTypes")
SetWebACL = Action("SetWebACL")
StartSchemaCreation = Action("StartSchemaCreation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApiKey = Action("UpdateApiKey")
UpdateDataSource = Action("UpdateDataSource")
UpdateFunction = Action("UpdateFunction")
UpdateGraphqlApi = Action("UpdateGraphqlApi")
UpdateResolver = Action("UpdateResolver")
UpdateType = Action("UpdateType")