"""
This type stub file was generated by pyright.
"""

from . import AWSObject, AWSProperty

MEMORY_VALUES = [x for x in range(128, 3009, 64)]
RESERVED_ENVIRONMENT_VARIABLES = [
    "AWS_ACCESS_KEY",
    "AWS_ACCESS_KEY_ID",
    "AWS_DEFAULT_REGION",
    "AWS_EXECUTION_ENV",
    "AWS_LAMBDA_FUNCTION_MEMORY_SIZE",
    "AWS_LAMBDA_FUNCTION_NAME",
    "AWS_LAMBDA_FUNCTION_VERSION",
    "AWS_LAMBDA_LOG_GROUP_NAME",
    "AWS_LAMBDA_LOG_STREAM_NAME",
    "AWS_REGION",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "AWS_SECURITY_TOKEN",
    "AWS_SESSION_TOKEN",
    "LAMBDA_RUNTIME_DIR",
    "LAMBDA_TASK_ROOT",
    "TZ",
]
ENVIRONMENT_VARIABLES_NAME_PATTERN = r"[a-zA-Z][a-zA-Z0-9_]+"

def validate_memory_size(memory_value):
    """ Validate memory size for Lambda Function
    :param memory_value: The memory size specified in the Function
    :return: The provided memory size if it is valid
    """
    ...

def validate_variables_name(variables): ...

class Code(AWSProperty):
    props = ...
    @staticmethod
    def check_zip_file(zip_file): ...
    def validate(self): ...

class VPCConfig(AWSProperty):
    props = ...

class OnFailure(AWSProperty):
    props = ...

class OnSuccess(AWSProperty):
    props = ...

class DestinationConfig(AWSProperty):
    props = ...

class EventInvokeConfig(AWSObject):
    resource_type = ...
    props = ...

class EventSourceMapping(AWSObject):
    resource_type = ...
    props = ...

class DeadLetterConfig(AWSProperty):
    props = ...

class Environment(AWSProperty):
    props = ...

class FileSystemConfig(AWSProperty):
    props = ...

class TracingConfig(AWSProperty):
    props = ...

class Function(AWSObject):
    resource_type = ...
    props = ...

class Permission(AWSObject):
    resource_type = ...
    props = ...

class VersionWeight(AWSProperty):
    props = ...

class AliasRoutingConfiguration(AWSProperty):
    props = ...

class ProvisionedConcurrencyConfiguration(AWSProperty):
    props = ...

class Alias(AWSObject):
    resource_type = ...
    props = ...

class Version(AWSObject):
    resource_type = ...
    props = ...

class Content(AWSProperty):
    props = ...

class LayerVersion(AWSObject):
    resource_type = ...
    props = ...

class LayerVersionPermission(AWSObject):
    resource_type = ...
    props = ...