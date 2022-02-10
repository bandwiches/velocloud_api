from dataclasses import dataclass


@dataclass
class QuickSearch:
    """Quick Search"""
    search: str = None  # minLength = 1
