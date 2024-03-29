from django import forms
from .models import Comment


class AddCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))
    stars_given = forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Comment
        fields = ['comment', 'stars_given']