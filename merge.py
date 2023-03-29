class MergeRequest:
    """
    Represents a merge request that can be voted on by users.
    The `MergeRequest` object keeps track of the number of upvotes and downvotes
    for the merge request, as well as its status (open or closed).
    Attributes:
        _context (dict): A dictionary that stores the number of upvotes and downvotes
            for the merge request.
        _status (str): A string that represents the status of the merge request.
    Methods:
        status(): Returns the status of the merge request based on the number of
            upvotes and downvotes.
        vote(by_user, type): Records a vote by a user (either an upvote or downvote)
            for the merge request.
    """

    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}
        self._status = "open"

    def status(self):
        if self._status == "closed":
            return self._status

        if self._context["downvotes"]:
            return "rejected"

        if len(self._context["upvotes"]) >= 2:
            return "approved"

        return "pending"

    def vote(self, by_user, type):
        if self._status == "closed":
            return "can't vote on a closed merge request"

        if type not in ["upvote", "downvote"]:
            return "not correct type"

        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].discard(by_user)
        self._context[f'{type}s'].add(by_user)

    def close(self):
        if self.status() not in ["approved", "rejected"]:
            return "Cannot close merge request until it has been approved or rejected"

        previous_status = self.status()
        self._status = "closed"

        return f"Merge request has been {previous_status} and closed"

    def getvotes(self):
        upvotes = len(self._context["upvotes"])
        downvotes = len(self._context["downvotes"])
        if upvotes == 0 and downvotes == 0:
            return "No votes yet"
        elif upvotes == 0:
            return f"{downvotes} downvotes"
        elif downvotes == 0:
            return f"{upvotes} upvotes"
        else:
            return f"{upvotes} upvotes, {downvotes} downvotes"
