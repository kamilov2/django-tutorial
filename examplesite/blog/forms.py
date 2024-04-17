from django import forms 
from .models import Comment

class SetCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body":forms.Textarea(attrs={"cols":40,"rows":5,"class":"comment_text"})
        }