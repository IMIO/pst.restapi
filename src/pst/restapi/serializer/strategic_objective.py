# -*- coding: utf-8 -*-

from plone.restapi.interfaces import ISerializeToJsonSummary
from plone.restapi.serializer.summary import DefaultJSONSummarySerializer
from zope.interface import implementer


@implementer(ISerializeToJsonSummary)
class OSSummarySerializer(DefaultJSONSummarySerializer):
    def __call__(self):
        result = super(OSSummarySerializer, self).__call__()
        result["original_title"] = getattr(self.context, "title", "")
        return result
