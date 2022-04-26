from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    # path('staff/', admin.site.urls),

    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    path('', HomeView.as_view(), name='splash'),
    path('skills', SkillsView.as_view(), name='skills'),
    path('experience', ExperienceView.as_view(), name='experience'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('print', PrintableView.as_view(), name='printable'),
]
