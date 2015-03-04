# -*- coding: utf-8 -*-
from pymongo import MongoClient

from django.test import TestCase
from django.conf import settings

from proxy_storage.meta_backends.orm import MultipleORMMetaBackend
from proxy_storage.storages.base import ProxyStorageBase, MultipleStoragesMixin
from proxy_storage.testutils import create_test_cases_for_proxy_storage

from tests_app.models import (
    ProxyStorageModelMultiple,
)
from .base_test_cases import (
    PrepareMixin,
    TestExistsMixin,
    TestSaveMixin,
    TestDeleteMixin,
    TestOpenMixin,
)


class MultipleStoragesProxyStorage(MultipleStoragesMixin, ProxyStorageBase):
    pass


base_test_case_classes = [
    (TestExistsMixin, PrepareMixin, TestCase),
    (TestSaveMixin, PrepareMixin, TestCase),
    (TestDeleteMixin, PrepareMixin, TestCase),
    (TestOpenMixin, PrepareMixin, TestCase)
]

meta_backend_instances = [
    MultipleORMMetaBackend(model=ProxyStorageModelMultiple),
]


# test default behaviour of proxy storage with fallback
locals().update(
    create_test_cases_for_proxy_storage(
        MultipleStoragesProxyStorage,
        base_test_case_classes,
        meta_backend_instances
    )
)
