"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon MQ"
prefix = "mq"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

CreateBroker = Action("CreateBroker")
CreateConfiguration = Action("CreateConfiguration")
CreateTags = Action("CreateTags")
CreateUser = Action("CreateUser")
DeleteBroker = Action("DeleteBroker")
DeleteTags = Action("DeleteTags")
DeleteUser = Action("DeleteUser")
DescribeBroker = Action("DescribeBroker")
DescribeBrokerEngineTypes = Action("DescribeBrokerEngineTypes")
DescribeBrokerInstanceOptions = Action("DescribeBrokerInstanceOptions")
DescribeConfiguration = Action("DescribeConfiguration")
DescribeConfigurationRevision = Action("DescribeConfigurationRevision")
DescribeUser = Action("DescribeUser")
ListBrokers = Action("ListBrokers")
ListConfigurationRevisions = Action("ListConfigurationRevisions")
ListConfigurations = Action("ListConfigurations")
ListTags = Action("ListTags")
ListUsers = Action("ListUsers")
RebootBroker = Action("RebootBroker")
UpdateBroker = Action("UpdateBroker")
UpdateConfiguration = Action("UpdateConfiguration")
UpdateUser = Action("UpdateUser")