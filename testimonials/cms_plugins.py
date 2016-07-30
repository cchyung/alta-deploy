from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import TestimonialPluginModel


class TestimonialPlugin(CMSPluginBase):
    model = TestimonialPluginModel
    render_template = 'testimonial_plugin.html'
    cache = False
    name = _("Testimonial")

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(TestimonialPlugin)
