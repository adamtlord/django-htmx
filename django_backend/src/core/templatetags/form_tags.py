from django import template
from django.forms import widgets
from django.template.loader import get_template

register = template.Library()


class FormFieldNode(template.Node):
    """
    Helper class for the render_form_field below
    """

    def __init__(self, form_field, help_text=None, css_classes=None, icon=None):
        self.form_field = template.Variable(form_field)
        self.help_text = help_text[1:-1] if help_text else help_text
        self.css_classes = css_classes[1:-1] if css_classes else css_classes

    def render(self, context):

        try:
            form_field = self.form_field.resolve(context)
        except template.VariableDoesNotExist:
            return ""

        widget = form_field.field.widget

        if isinstance(widget, widgets.HiddenInput):
            return form_field
        elif isinstance(widget, widgets.RadioSelect):
            t = get_template("common/fragments/radio_field.html")
        elif isinstance(widget, widgets.CheckboxInput):
            t = get_template("common/fragments/checkbox_field.html")
        elif isinstance(widget, widgets.CheckboxSelectMultiple):
            t = get_template("common/fragments/multi_checkbox_field.html")
        elif isinstance(widget, widgets.Select):
            t = get_template("common/fragments/select_field.html")
        elif isinstance(widget, widgets.ClearableFileInput) or isinstance(widget, widgets.FileInput):
            t = get_template("common/fragments/file_field.html")
        else:
            t = get_template("common/fragments/form_field.html")

        help_text = self.help_text
        if help_text is None:
            help_text = form_field.help_text

        return t.render(
            {
                "form_field": form_field,
                "help_text": help_text,
                "css_classes": self.css_classes,
            }
        )


@register.tag
def render_form_field(parser, token):
    try:
        help_text = None
        css_classes = None

        token_split = token.split_contents()
        if len(token_split) == 4:
            (
                tag_name,
                form_field,
                help_text,
                css_classes,
            ) = token.split_contents()
        elif len(token_split) == 3:
            tag_name, form_field, help_text = token.split_contents()
        else:
            tag_name, form_field = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("Unable to parse arguments for {0}".format(repr(token.contents.split()[0])))

    return FormFieldNode(form_field, help_text=help_text, css_classes=css_classes)


@register.filter(name="add_class")
def add_class(field, _class):
    class_old = field.field.widget.attrs.get("class", None)
    class_new = class_old + " " + _class if class_old else _class
    return field.as_widget(attrs={"class": class_new})


@register.filter(name="add_attributes")
def add_attributes(field, _attrs):
    attrs = {}
    definition = _attrs.split(",")

    for d in definition:
        if ":" not in d:
            attrs["class"] = d
        else:
            t, v = d.split(":")
            attrs[t] = v

    return field.as_widget(attrs=attrs)


@register.inclusion_tag("common/fragments/float_input.html")
def float_input(field, _type="text", step="1", places="-2"):
    return {"field": field, "type": _type, "step": step, "places": places}
