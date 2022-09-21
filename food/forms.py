from django.forms import ModelForm

from food.models import Food


class FoodForm(ModelForm):

    class Meta:
        model = Food
        fields = ["f_id","category","name","price","description"]
        labels = {
            "f_id":"Food ID (unique)"
        }


    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'