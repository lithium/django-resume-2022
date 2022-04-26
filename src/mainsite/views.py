from django.views.generic.base import TemplateView

from mainsite.fixedcontent import FixedContent

_content = FixedContent()


class FixedContentMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'skills': _content.skills,
        })
        return context


class HomeView(TemplateView):
    template_name = 'splash.html'


class PrintableView(FixedContentMixin, TemplateView):
    template_name = 'printable.html'


class SkillsView(FixedContentMixin, TemplateView):
    template_name = 'skills.html'

