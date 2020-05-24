import os

from .base_template_store import BaseTemplateStore
from . import template_store_mappings


class SimpleTemplateStore(BaseTemplateStore):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_store_url = kwargs["template_store_url"]

    def get_template(self, template_name: str):
        template_url = None
        if template_store_mappings.get(template_name):
            template_url = os.path.join(self.template_store_url, template_store_mappings.get(template_name))
        return template_url
