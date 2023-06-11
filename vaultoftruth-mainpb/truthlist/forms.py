from django import forms
from truthlist.models import quest
import pandas as pd


qs = quest.objects.values_list('number', 'question')
data=pd.DataFrame(qs)

FAVORITE_COLORS_CHOICES = [
    ('agree', 'Agree'),
    ('disagree', 'Disagree'),
    ('nocomment', 'No Comment'),
]

class listform(forms.Form):
    """
    q1=forms.ChoiceField(label="The earth round",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q2=forms.ChoiceField(label="In the moon landing",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q3=forms.ChoiceField(label="In creation",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q4=forms.ChoiceField(label="In one God",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q5=forms.ChoiceField(label="Gender cannot be choosen",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q6=forms.ChoiceField(label="The unviverse is finite",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q7=forms.ChoiceField(label="There is life after death",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q8=forms.ChoiceField(label="Aliens exists",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q9=forms.ChoiceField(label="There is people that control the world",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q10=forms.ChoiceField(label="There is more than 3 dimentions",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q11=forms.ChoiceField(label="We have free will",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q12=forms.ChoiceField(label="The seed came before the plant",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q13=forms.ChoiceField(label="God was not created",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q14=forms.ChoiceField(label="Its possible to think nothing",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q15=forms.ChoiceField(label="42 is the answer to the ultimate question in life",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q16=forms.ChoiceField(label="Soul mates do exists",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q17=forms.ChoiceField(label="We have free choise",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q18=forms.ChoiceField(label="Human cloning is unethical",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q19=forms.ChoiceField(label="Designer babies is unethical",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q20=forms.ChoiceField(label="People can choose to be happy",choices=FAVORITE_COLORS_CHOICES, required=True) 
    q21=forms.ChoiceField(label=data[1][2],choices=FAVORITE_COLORS_CHOICES, required=True) 
   """
    #this is to add the forms lines in the html from a datafram coming from and excel into SQLITE
    #q1=forms.ChoiceField(label=data[1][0],choices=FAVORITE_COLORS_CHOICES, required=True)
    """"
    q2=forms.ChoiceField(label=data[1][1],choices=FAVORITE_COLORS_CHOICES, required=True)
    q3=forms.ChoiceField(label=data[1][2],choices=FAVORITE_COLORS_CHOICES, required=True)
    q4=forms.ChoiceField(label=data[1][3],choices=FAVORITE_COLORS_CHOICES, required=True)
    q5=forms.ChoiceField(label=data[1][4],choices=FAVORITE_COLORS_CHOICES, required=True)
    q6=forms.ChoiceField(label=data[1][5],choices=FAVORITE_COLORS_CHOICES, required=True)
    q7=forms.ChoiceField(label=data[1][6],choices=FAVORITE_COLORS_CHOICES, required=True)
    q8=forms.ChoiceField(label=data[1][7],choices=FAVORITE_COLORS_CHOICES, required=True)
    q9=forms.ChoiceField(label=data[1][8],choices=FAVORITE_COLORS_CHOICES, required=True)
    q10=forms.ChoiceField(label=data[1][9],choices=FAVORITE_COLORS_CHOICES, required=True)
    q11=forms.ChoiceField(label=data[1][10],choices=FAVORITE_COLORS_CHOICES, required=True)
    q12=forms.ChoiceField(label=data[1][11],choices=FAVORITE_COLORS_CHOICES, required=True)
    q13=forms.ChoiceField(label=data[1][12],choices=FAVORITE_COLORS_CHOICES, required=True)
    q14=forms.ChoiceField(label=data[1][13],choices=FAVORITE_COLORS_CHOICES, required=True)
    q15=forms.ChoiceField(label=data[1][14],choices=FAVORITE_COLORS_CHOICES, required=True)
    q16=forms.ChoiceField(label=data[1][15],choices=FAVORITE_COLORS_CHOICES, required=True)
    q17=forms.ChoiceField(label=data[1][16],choices=FAVORITE_COLORS_CHOICES, required=True)
    q18=forms.ChoiceField(label=data[1][17],choices=FAVORITE_COLORS_CHOICES, required=True)
    q19=forms.ChoiceField(label=data[1][18],choices=FAVORITE_COLORS_CHOICES, required=True)
    q20=forms.ChoiceField(label=data[1][19],choices=FAVORITE_COLORS_CHOICES, required=True)
    q21=forms.ChoiceField(label=data[1][20],choices=FAVORITE_COLORS_CHOICES, required=True)

    def __init__(self, fields, *args, **kwargs):
        super(listform, self).__init__(*args, **kwargs)
        for i in data:
         self.data['my_field_%i' % i] = forms.ChoiceField(label=data[1][i],choices=FAVORITE_COLORS_CHOICES, required=True)
    """
    
    for i in  range(0, 3):
         i=forms.ChoiceField(label=data[1][i],choices=FAVORITE_COLORS_CHOICES, required=True)
    '''
    user_name=forms.ChoiceField(label=data[1][20],choices=FAVORITE_COLORS_CHOICES, required=True)
    review_text=forms.CharField(label="2",max_length=255)
    ratings=forms.IntegerField(label="3")
    '''

        
    