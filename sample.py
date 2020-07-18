# Import SnooNotes from Core
from SnooNotes.core import SnooNotes

if __name__ == "__main__":

    # Authenticate with a reddit username and an user_key that can be generated from "https://snoonotes.com/#!/userkey". The generated key is sent via PM to your reddit account.
    sn = SnooNotes("username", "user_key")

    # Returns a dictionary with usernames and their associated usernotes.
    notes_for_username = sn.get_notes_for_user("username")
    notes_for_usernames12 = sn.get_notes_for_user(["username1", "username2"])
    
    # Returns a dictionary to get NoteTypes supported in that particular subreddit
    subreddit_notes = sn.get_notes_for_subreddit("subreddit")

    # Add a new usernote to the user under the subreddit with a note with a link to the comment/post.
    sn.add_note_for_user("username", "note_type", "subreddit", "Reason for note", "www.reddit.com/r/subreddit/123jks/.../jkas12")
