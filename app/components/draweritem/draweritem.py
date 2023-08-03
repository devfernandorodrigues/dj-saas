from django_components import component


@component.register("draweritem")
class DrawerItem(component.Component):
    template_name = "draweritem/draweritem.html"

    def get_context_data(self, **kwargs):
        return kwargs
