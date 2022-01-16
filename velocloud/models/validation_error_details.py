from dataclasses import dataclass


@dataclass
class ValidationErrorDetails:
    """Validation Error Details"""
    code: str
    message: str
    path: str
