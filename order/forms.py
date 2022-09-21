from django.forms import  ModelForm

from order.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["food","count"]

    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'