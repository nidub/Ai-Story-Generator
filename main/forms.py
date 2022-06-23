from django import forms

genre_Choices=[
    ('superhero','Superhero'), 
    ('action', 'Action'), 
    ('drama','Drama'), 
    ('horror', 'Horror'), 
    ('thriller','Thriller'), 
    ('sci_fi','Sci_fi')
]

class GetText(forms.Form):
    given_text=forms.CharField( max_length=1000)
    g_Choice=forms.CharField(widget=forms.RadioSelect(choices=genre_Choices))

class Stories_Submitted(forms.Form):
    my_story=forms.CharField(max_length=1000)
