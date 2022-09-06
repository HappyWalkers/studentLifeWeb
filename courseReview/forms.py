import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

from django.forms import ModelForm
from .models import college, department, major, course, professor

class reviewCourseForm(forms.Form):
    rating = forms.IntegerField(max_value=100, min_value=0, required=True, label="rating", initial=100, help_text="Rate this course with a value between 0 and 100")
    qualityRating = forms.IntegerField(max_value=100, min_value=0, required=True, label="quality rating", initial=100, help_text="Rate the quality of this course with a value between 0 and 100")
    score = forms.IntegerField(max_value=100, min_value=0, required=False, label="score", initial=100, help_text="Input your score on this course with a value between 0 and 100")
    content = forms.CharField(max_length=1000, min_length=0, strip=True, required=False, label="comment", initial="comment", help_text="Comment on this course")

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 0:
            raise ValidationError(gettext_lazy('Invalid Value - rating should be no less than 0'))

        if rating > 100:
            raise ValidationError(gettext_lazy('Invalid Value - rating should be no more than 100'))

        return rating

    def clean_qualityRating(self):
        qualityRating = self.cleaned_data['qualityRating']

        if qualityRating < 0:
            raise ValidationError(gettext_lazy('Invalid Value - qualityRating should be no less than 0'))

        if qualityRating > 100:
            raise ValidationError(gettext_lazy('Invalid Value - qualityRating should be no more than 100'))

        return qualityRating

    def clean_score(self):
        score = self.cleaned_data['score']

        if score < 0:
            raise ValidationError(gettext_lazy('Invalid Value - score should be no less than 0'))

        if score > 100:
            raise ValidationError(gettext_lazy('Invalid Value - score should be no more than 100'))

        return score

    def clean_content(self):
        content = self.cleaned_data['content']

        if len(content) > 1000:
            raise ValidationError(gettext_lazy('Invalid Content Length - content should be no more than 1000 characters'))

        return content

class collegeEditForm(ModelForm):
    class Meta:
        model = college
        fields = ['name', 'introduction', 'web']

class departmentEditForm(ModelForm):
    class Meta:
        model = department
        fields = ['name', 'introduction', 'web']

class majorEditForm(ModelForm):
    class Meta:
        model = major
        fields = ['name', 'introduction']

class courseEditForm(ModelForm):
    class Meta:
        model = course
        fields = ['name', 'introduction', 'rating']