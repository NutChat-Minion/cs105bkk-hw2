"""HW2 · event.py: one club event with limited seats."""

from dataclasses import dataclass, field
from errors import AlreadySignedUpError, NotSignedUpError


@dataclass
class Event:
    """One event with seats and a waitlist."""

    title: str
    capacity: int
    seats: list[str] = field(default_factory=list)
    waitlist: list[str] = field(default_factory=list)

    def seats_left(self) -> int:
        """How many seats are still free."""
        return self.capacity - len(self.seats)

    def sign_up(self, member: str) -> str:
        """Sign up a member or place them on the waitlist."""
        if member in self.seats or member in self.waitlist:
            raise AlreadySignedUpError(member, self.title)

        if self.seats_left() > 0:
            self.seats.append(member)
            return "seat"

        self.waitlist.append(member)
        return "waitlist"

    def cancel(self, member: str) -> str | None:
        """Cancel signup and promote the first waitlisted member if possible."""
        if member in self.waitlist:
            self.waitlist.remove(member)
            return None

        if member in self.seats:
            self.seats.remove(member)

            if self.waitlist:
                promoted = self.waitlist.pop(0)
                self.seats.append(promoted)
                return promoted

            return None

        raise NotSignedUpError(member, self.title)

    def place(self, member: str) -> int:
        """Return 0 for a seat, or the waitlist position starting at 1."""
        if member in self.seats:
            return 0

        if member in self.waitlist:
            return self.waitlist.index(member) + 1

        raise NotSignedUpError(member, self.title)