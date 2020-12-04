from celery.decorators import task
from .email import send_email_review
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name="send_review_email_task")
logger.info("sent review email")