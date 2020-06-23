# -*- coding: utf-8 -*-

from imio.restapi.serializer.base import SerializeToJson
from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.interfaces import ISerializeToJsonSummary
from zope.component import queryMultiAdapter
from zope.interface import implementer


@implementer(ISerializeToJson)
class ActionSerializer(SerializeToJson):
    def __call__(self, *args, **kwargs):
        result = super(ActionSerializer, self).__call__(*args, **kwargs)
        result["operational_objective"] = self.get_oo()
        result["strategic_objective"] = self.get_os()
        return result

    def get_oo(self):
        """Return the serialized parent that is the Operational Objective"""
        return queryMultiAdapter(
            (self.context.aq_parent, self.request), ISerializeToJsonSummary,
        )()

    def get_os(self):
        """Return the serialized parent of the parent that is the Strategic Objective"""
        return queryMultiAdapter(
            (self.context.aq_parent.aq_parent, self.request), ISerializeToJsonSummary,
        )()
