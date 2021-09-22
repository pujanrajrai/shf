from .models import ProductInquiry
from django import forms


class ProductInquiryForm(forms.ModelForm):
    class Meta:
        model = ProductInquiry
        fields = ['name', 'phone_number', 'address', 'quantity']

    def clean(self):
        super(ProductInquiryForm, self).clean()
        phone_number = self.cleaned_data.get('phone_number')
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        quantity = self.cleaned_data.get('quantity'),
        if len(phone_number) != 10:
            self._errors['phone_number'] = self.error_class([
                'Phone Number should be of 10 character'])

        if len(name) < 4:
            self._errors['name'] = self.error_class([
                'Name should of at least 4 character'])

        if len(address) < 3:
            self._errors['address'] = self.error_class([
                'address should of at least 3 character'])

