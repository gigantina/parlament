from congress.models import Meeting

def get_object_or_none(Model, **kwargs):
    try:
        return Model.objects.get(**kwargs)
    except Model.DoesNotExist:
        return None

def get_years():
    obj = Meeting.objects.all()
    obj = [i[1].year for i in obj.values_list()]
    obj = reversed(sorted(list(set(obj))))
    return obj


