from dataclasses import dataclass, field
from typing import List
from velocloud.models.validation_error_details import ValidationErrorDetails


@dataclass
class ErrorData:
    """Error Data
    This is a custom class.
    """
    valid: bool = None
    error: List[ValidationErrorDetails] = field(default_factory=list)
    warning: List[ValidationErrorDetails] = field(default_factory=list)


@dataclass
class ErrorObject:
    """Error Object
    This is a custom class.
    """
    code: int  # http://www.jsonrpc.org/specification#error_object
    message: str
    data: ErrorData = None


@dataclass
class Error:
    """Error"""
    error: ErrorObject
