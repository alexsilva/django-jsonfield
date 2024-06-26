import json

from django import forms
from jsonfield.utils import default


class JSONWidget(forms.Textarea):
	def render(self, name, value, attrs=None, **kwargs):
		if value is None:
			value = ""
		if not isinstance(value, str):
			value = json.dumps(value, indent=2, default=default)
		return super(JSONWidget, self).render(name, value, attrs, **kwargs)


class JSONSelectWidget(forms.SelectMultiple):
	pass
