from django import forms


class BulkUpdateForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea, label="Skills (enter one per line)")
