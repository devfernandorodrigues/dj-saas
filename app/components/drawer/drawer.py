from django_components import component


@component.register("drawer")
class Drawer(component.Component):
    template_name = "drawer/drawer.html"

    def get_context_data(self, **kwargs):
        return kwargs
