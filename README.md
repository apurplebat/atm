This script checks if a user has entered the correct PIN to view the ATM's info.
If the PIN is incorrect, the user cannot access the information.
The user has 3 attempts to get it right - anything more will lock out.

In this script, the PIN is a predefined global variable ("1234").
Entering this PIN will reveal the account balance to the user.

The user can try to enter other PINs, to no avail. It will prompt the user again,
until 3 attempts have passed. At this point, the account will lock out and
the user cannot proceed any further.

The PIN, by definition, must be an integer. Anything else (i.e. chars etc.) will
be caught by the try-except statement in the code as a ValueError. This is done
to avoid breaking the program.
