from dataclasses import dataclass


@dataclass
class AuthObject:
    """Auth Object
    This is a custom class.
    """
    username: str
    password: str
    email: str = None
    password2: str = None

    def __repr__(self):
        return str(type(self))

    @classmethod
    def from_dict(cls, profile: dict):
        """Factory Method"""
        INST = cls()
        INST.username = profile.get('username')
        INST.password = profile.get('password')
        INST.email = profile.get('email')
        INST.password2 = profile.get('password2')

        return INST
