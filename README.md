# PySnooNotes

Python wrapper for the Snoonotes API

## Currently Supported Features:

1. Fetch notes for a particular user
2. Fetch Subreddit Notes - Caching implemented 
3. Add notes for a user

## Not Supported Currently:

1. Removing usernotes

## Usage:

### Imports

To use in your python project, use:

```python
from SnooNotes.core import SnooNotes
```

### Sample Usage

Authenticate using a Reddit account that can add usernotes and a user_key for that account that can be generated from "https://snoonotes.com/#!/userkey". The generated key is sent via PM to your reddit account.

```python
sn = SnooNotes("username", "user_key")
```

Returns a dictionary with usernames and their associated usernotes:

```python
notes_for_username = sn.get_notes_for_user("username")
notes_for_usernames12 = sn.get_notes_for_user(["username1", "username2"])
```

Returns notes supported in that particular subreddit:

```python
subreddit_notes = sn.get_notes_for_subreddit("subreddit")
```

Add a new usernote for the user under a subreddit with a custom note and a link to the comment/post:

```python
sn.add_note_for_user("username", "note_type_id", "subreddit", "Reason for note", "www.reddit.com/r/subreddit/123abc/.../123abc")
```


The above is also summarized in the `sample.py` script
