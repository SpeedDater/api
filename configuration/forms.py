from django import forms


class AddStaffForm(forms.Form):
    email = forms.EmailField(label="Email address")
    first_name = forms.CharField()
    last_name = forms.CharField()


class BulkUpdateForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea,
                              label="Skills (enter one per line)")
