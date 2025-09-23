from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Optional, NumberRange

def wtfield_for(field_def):
    ftype = field_def["type"]
    required = field_def.get("required", False)
    validators = [DataRequired()] if required else [Optional()]

    if ftype == "text":
        return StringField(field_def["label"], validators=validators, render_kw={"placeholder": field_def.get("placeholder", "")})
    if ftype == "number":
        v = validators[:]
        if field_def.get("min") is not None:
            v.append(NumberRange(min=field_def.get("min")))
        return IntegerField(field_def["label"], validators=v)
    if ftype == "textarea":
        return TextAreaField(field_def["label"], validators=validators, render_kw={"rows": 4})
    if ftype == "select":
        choices = [(opt["value"], opt["label"]) for opt in field_def["options"]]
        return SelectField(field_def["label"], validators=validators, choices=choices)
    if ftype in ("multicheck", "list", "file", "date", "table"):
        # custom-rendered in template
        return None
    # default fallback
    return StringField(field_def["label"], validators=validators)
