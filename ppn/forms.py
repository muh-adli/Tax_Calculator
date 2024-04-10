from django import forms

class PPNForm(forms.Form):

    price = forms.CharField(
        label='Dasar Perkenaan Pajak (DPP)',
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'type': 'text',
                'id': 'price',
                'name':'price',
                'class':'form-control',
                'localize': True,
                }
            )
        )

    tax = forms.DecimalField(
        label='Pajak Pertambahan Nilai (PPN)',
        initial=11,
        widget=forms.NumberInput(
            attrs={
                'min': 0,
                'max': '100',
                'type': 'text',
                'id': 'tax',
                'name': 'tax',
                'class': 'form-control',
                'readonly':'readonly'
                }
            )
        )

    discount = forms.CharField(
        label='Diskon',
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'id' : 'disc',
                'class': 'form-control',
                'min': 0,
                'max': '100',
                }
            )
        )

    total_discount = forms.CharField(
        label='Total Diskon',
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'type': 'text',
                'id' : 'disc-price',
                'name':'disc-price',
                'class': 'form-control',
                'readonly':'readonly',
                }
            )
        )

    result = forms.CharField(
        label='Harga Total',
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'type': 'text',
                'id': 'result',
                'name':'result',
                'class': 'form-control',
                'readonly':'readonly',
                }
            )
        )