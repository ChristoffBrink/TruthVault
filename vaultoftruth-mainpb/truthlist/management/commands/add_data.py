from django.core.management.base import BaseCommand
import pandas as pd
from truthlist.models import quest
from sqlalchemy import create_engine
from django.forms.models import model_to_dict

class Command(BaseCommand):
    
    def handle(self,*args,**options):
        excel_file ='Questions.xlsx'
        df=pd.read_excel(excel_file)
        engine=create_engine('sqlite:///db.sqlite3')
        df.to_sql(quest._meta.db_table,if_exists='replace',con=engine,index=False)
        qs = quest.objects.values_list('number', 'question')
        data=pd.DataFrame(qs)
        #for q in qs:
        print(data[1][2])
        