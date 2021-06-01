from dataclasses import dataclass, field
from typing import List


@dataclass
class ValidationErrorDetails:
    code: str = None
    message: str = None
    path: str = None

    def __iter__(self):
        return iter([self.code, self.message, self.path])


@dataclass
class ErrorData:
    """Error Data

    - if included in the response.
    """
    valid: bool
    error: List[ValidationErrorDetails] = field(default_factory=ValidationErrorDetails)
    warning: List[ValidationErrorDetails] = field(default_factory=ValidationErrorDetails)


@dataclass
class Error:
    """Error (Base Class)

    - data is not always included.
    """
    code: int
    message: str
    data: ErrorData = None
