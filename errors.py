
"""HW2 · errors.py: the club's own exceptions."""


class SignupError(Exception):
    """The parent of every sign-up problem."""


class NotSignedUpError(SignupError):
    """The member is not signed up for the event."""

    def __init__(self, member: str, event: str):
        super().__init__(f"{member} is not signed up for {event}")
        self.member = member
        self.event = event


class AlreadySignedUpError(SignupError):
    """The member is already signed up for the event."""

    def __init__(self, member: str, event: str):
        super().__init__(f"{member} is already signed up for {event}")
        self.member = member
        self.event = event


class UnknownEventError(SignupError):
    """The requested event does not exist."""

    def __init__(self, title: str):
        super().__init__(f"there is no event called {title!r}")
        self.title = title
