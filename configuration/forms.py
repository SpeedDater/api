from django import forms


class BulkUpdateForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
