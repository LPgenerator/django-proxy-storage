# coding=utf-8;
__author__ = 'ilstreltsov'

from celery import current_app
from celery.contrib.methods import task_method


class CeleryMixin(object):

    @current_app.task(name='multiple_storage.delete_delay', filter=task_method)
    def delete_delay(self, name):
        super(CeleryMixin, self).delete(name)

    @current_app.task(name='multiple_storage.save_delay', filter=task_method)
    def save_delay(self, path, original_storage_path, name, using):
        if self.exists(path):
            original_file = self.open(path)
            super(CeleryMixin, self).save(name,
                                          original_file,
                                          original_storage_path,
                                          using)
