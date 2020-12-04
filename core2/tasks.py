from celery.decorators import task
from .email import send_email_review
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    logger.info("sent review email")
    return send_email_review(name, email, review)