from django_components import component


@component.register("input")
class Input(component.Component):
    template_name = "input/input.html"

    def get_context_data(self, **kwargs):
        return kwargs
