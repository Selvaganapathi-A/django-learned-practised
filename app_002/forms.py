from django import forms


class ComplaintForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1)
    cc_to_govt = forms.BooleanField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(
        widget=forms.widgets.Textarea(
            {
                "cols": 60,
                "rows": 5,
            }
        )
    )

    def send_mail(self):
        print(
            f"""
from        : {self.cleaned_data['name']}
to_Govt     : {'yes' if self.cleaned_data['cc_to_govt'] else 'No'}
to          : admin@mysite.com
subject     : {self.cleaned_data['subject']}
message     :
{self.cleaned_data['message']}"""
        )
        return None
