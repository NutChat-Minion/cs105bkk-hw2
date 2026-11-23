# HW2 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?
I implemented the Event and Club classes, along with custom exceptions in errors.py. I used sign_up(), cancel(), and place() to manage event registration, seats, and waitlists. I also ran pytest to check my code.

## What broke, and how did you fix it?
Some tests failed because AlreadySignedUpError and UnknownEventError still had NotImplementedError placeholders. I implemented their __init__() methods, added the correct error messages, and stored the required attributes (member, event, and title). I then tested the program again.

## What would you do differently next time?
I would implement and test each function and custom exception one at a time instead of waiting until the end. I would also run pytest more frequently to catch errors earlier.