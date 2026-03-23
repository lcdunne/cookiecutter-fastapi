class CoreException(Exception):
    """Base exception class for all API exceptions to inherit from.

    Application-specific exceptions should be raised in the services layer and a
    corresponding exception handler should be registered."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class InputException(CoreException): ...


class ResourceNotFoundException(CoreException): ...


class ResourceConflictException(CoreException): ...
