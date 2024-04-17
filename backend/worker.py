from celery import Celery

def make_celery(app):
    celery = Celery(
        'Application Jobs',
        broker_url= 'redis://localhost:6379/3',
        result_backend='redis://localhost:6379/4',
        broker_connection_retry_on_startup=True,
        CELERY_TIMEZONE = "Asia/Kolkata"
    )
    
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def call(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery