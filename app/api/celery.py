from __future__ import absolute_import
from __future__ import unicode_literals
from celery import Celery, shared_task
from core.email import CotizateSendEmail
from api.settings import production
import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings.development')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.production")
app = Celery("api", broker="pyamqp://rabbitmq_user:admin2020@broker//")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@shared_task(bind=True)
def send_email_module(self, subject, to, body, template_name=None, context=None):
    try:
        CotizateSendEmail(
            subject=subject, to=to, from_email=production.DEFAULT_FROM_EMAIL, body=body,
        ).send_email_with_custom_template(
            template_name=template_name, context=context,
        )
        return True
    except Exception as e:
        return self.retry(exc=e, countdown=10)
