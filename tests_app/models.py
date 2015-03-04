# -*- coding: utf-8 -*-
from proxy_storage.meta_backends.orm import (
    ProxyStorageModelBase,
    ContentObjectFieldMixin,
    OriginalStorageNameMixin,
    ProxyMultipleStorageModel,
)


class ProxyStorageModel(ProxyStorageModelBase):
    pass


class ProxyStorageModelWithContentObjectField(ContentObjectFieldMixin, ProxyStorageModelBase):

    class Meta:
        verbose_name = 'Proxy storage with field'


class ProxyStorageModelWithOriginalStorageName(OriginalStorageNameMixin, ProxyStorageModelBase):

    class Meta:
        verbose_name = 'Proxy storage with orig'


class ProxyStorageModelMultiple(ProxyMultipleStorageModel):

    class Meta:
        verbose_name = 'Proxy storage multiple'


class ProxyStorageModelWithContentObjectFieldAndOriginalStorageName(OriginalStorageNameMixin,
                                                                    ProxyStorageModelBase):
    class Meta:
        verbose_name = 'Proxy storage with field and orig'
