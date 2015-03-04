# coding=utf-8;
__author__ = 'ilstreltsov'

from celery import current_app
from celery.contrib.methods import task_method


class CeleryMixin(object):

    is_celery = True

    @current_app.task(name='multiple_storage.delete_delay', filter=task_method)
    def delete_delay(self, name):
        self.run_delete(name, not_assync=True)

    @current_app.task(name='multiple_storage.save_delay', filter=task_method)
    def save_delay(self, path, original_storage_path, name, using):
        self.run_save(path, name, original_storage_path, using, not_assync=True)
