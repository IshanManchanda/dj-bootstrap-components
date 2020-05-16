from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BootstrapComponentsConfig(AppConfig):
	"""
	Configuration entry point for the bootstrap_components app
	"""
	label = name = 'bootstrap_components'
	verbose_name = _('Bootstrap Components App')
