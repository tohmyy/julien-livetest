from django.forms import ModelForm
from .models import Order
from .models import Customer

class OrderForm(ModelForm):
    class Meta:
         model = Order
         fields = '__all__'#allows me to import all fields(models)
         # (customer field, product field, status field (model))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer

        fields = "__all__"

