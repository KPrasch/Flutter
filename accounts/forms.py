from django import forms
from .models import Member


class MemberRegistrationForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('offline_name',
                  'phone_number',
                  'bio',
                  'dob',
                  'likes_pickles',
                  'favors_llamas',
                  )
