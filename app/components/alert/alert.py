from django_components import component


@component.register("alert")
class Alert(component.Component):
    template_name = "alert/alert.html"

    def get_context_data(self, text, type):
        return {
            "text": text,
            "type": type,
        }
