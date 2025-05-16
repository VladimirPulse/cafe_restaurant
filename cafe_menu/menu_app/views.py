# from django.shortcuts import render

# def home(request):
#     return render(request, 'index.html')


from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "index.html"
