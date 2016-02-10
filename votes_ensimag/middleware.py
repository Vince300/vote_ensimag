from votes_ensimag import settings
from datetime import datetime
from django.shortcuts import render
import re

class DateTimeLimitMiddleware(object):
    def process_request(self, request):
        if not request.session.get('bypass_date', False):
            if request.GET.get('bypass') == settings.DATE_BYPASS_SECRET:
                request.session['bypass_date'] = True
            else:
                now = settings.TIMEZONE.localize(datetime.now())
                if not re.match('/admin', request.path):
                    if now < settings.START_DATE:
                        return render(request, 'not_yet.html', {'date': settings.START_DATE })
                    elif now > settings.END_DATE:
                        return render(request, 'termine.html', {'date': settings.END_DATE })

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response
