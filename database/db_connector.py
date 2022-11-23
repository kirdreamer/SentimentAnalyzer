import logging

from database.comment_models import Comment


def get_all_unprocessed_body() -> list[Comment]:
    logging.info("Trying to get unprocessed data from database")
    Comments = Comment.query.filter(Comment.mood == "")
    return Comments
