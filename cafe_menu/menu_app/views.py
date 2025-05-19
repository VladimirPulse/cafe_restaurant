from django.views.generic import DetailView, TemplateView

from menu_app.models import MenuItem


class IndexPageView(TemplateView):
    template_name = "index.html"


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = "menu.html"
    context_object_name = "menu_item"

    def get_object(self):
        named_url = self.kwargs.get("slug")
        return MenuItem.objects.get(named_url=named_url)
