from django.apps import apps
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


class ListChoiceAPIView(APIView):

    def get_model(self, *args, **kwargs):
        try:
            return apps.get_model(kwargs['app_label'], kwargs['model'])
        except LookupError:
            raise Http404()

    def get_choices(self, *args, **kwargs):
        choices = getattr(self.model, kwargs['choice'], None)

        if choices is None:
            raise Http404()

        return choices

    def format_choice(self, choice):
        return {
            'code': choice[0],
            'description': choice[1],
        }

    def get(self, request, *args, **kwargs):

        self.model = self.get_model(*args, **kwargs)

        choices = self.get_choices(*args, **kwargs)

        data = [self.format_choice(choice) for choice in choices]

        return Response(data)
