# -*- coding: utf-8 -*-
import tempfile
import shutil
import os
from mock import Mock

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.utils.encoding import force_text

from proxy_storage.settings import proxy_storage_settings

from proxy_storage.storages.fallback import OriginalStorageFallbackMixin
from tests_app.tests.functional.storages.base.proxy_storage_base.base_test_cases import (
    TestExistsMixin as TestExistsMixinBase,
    TestDeleteMixin as TestDeleteMixinBase,
)

from tests_app.tests.functional.storages.base.multiple_original_storages_mixin.base_test_cases import (
    TestSaveMixin as TestSaveMixinBase,
    TestOpenMixin as TestOpenMixinBase,
)

class PrepareMixin(object):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.temp_dir_2 = tempfile.mkdtemp()
        self.file_name = u'hello.txt'
        self.content = u'some content'
        self.content_file = ContentFile(self.content)
        self.file_full_path = os.path.join(self.temp_dir, self.file_name)
        self.proxy_storage.original_storages = [
            ('original_storage_1', FileSystemStorage(location=self.temp_dir)),
            ('original_storage_2', FileSystemStorage(location=self.temp_dir_2)),
        ]
        self.proxy_storage._init_original_storages()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)
        shutil.rmtree(self.temp_dir_2)


class TestExistsMixin(TestExistsMixinBase):
    pass


class TestSaveMixin(TestSaveMixinBase):

    def test_save_should_save_file_on_each_storages(self):
        saved_file_name = self.proxy_storage.save(self.file_name, self.content_file)
        related_names = self.proxy_storage.meta_backend.get_related(path=saved_file_name)
        self.assertEqual(len(related_names), len(self.proxy_storage.original_storages) - 1)

        for path in related_names:
            msg = 'should save file content to all storages'
            self.assertTrue(self.proxy_storage.exists(path), msg)
            self.assertEqual(
                self.proxy_storage.open(path, 'r').read(),
                self.content
            )

    def test_with_original_storage_path_argument_should_not_perform_saving_to_original_storage(self):
        original_storage_path = 'hello.txt'
        saved_file_name = self.proxy_storage.save(
            self.file_name,
            self.content_file,
            original_storage_path=original_storage_path
        )
        meta_backend_obj = self.proxy_storage.meta_backend.get(path=saved_file_name)

        self.assertTrue(self.proxy_storage.exists(saved_file_name))
        self.assertFalse(self.proxy_storage.get_original_storage(
            meta_backend_obj=meta_backend_obj
        ).exists(saved_file_name))
        self.assertEqual(meta_backend_obj['original_storage_path'], original_storage_path)

class TestDeleteMixin(TestDeleteMixinBase):
    pass


class TestOpenMixin(TestOpenMixinBase):
    pass
