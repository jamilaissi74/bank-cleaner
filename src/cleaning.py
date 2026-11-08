from datetime import datetime,date
import re  
from matplotlib import text
import pandas as pd
from pandas._libs.tslibs.parsing import DateParseError


def label_normalizing(label):
    label=str(label)
    a=label.strip()
    a=a.lower()
    a=str(re.sub(" +", "_", a))
    return a

# def amount_cleaning(amount):

def date_normalizing(date):
    if pd.isnull(date) or str(date).strip() == "":
        raise ValueError("date is empty")

    date = str(date).strip()

    if "/" in date:
      return pd.to_datetime(date, errors='raise', format="%d/%m/%Y").date()
    else:
     return pd.to_datetime(date, errors='raise').date()
      
def currency_normalizing(currency):
    if pd.isnull(currency) or str(currency).strip() == "":
            raise ValueError("currency is empty")

    currency= re.sub("EURO|EUR", "EUR", str(currency).strip(), flags=re.IGNORECASE)
    if currency == "EUR":
         return "EUR"
    currency= re.sub("mad|DH|DIRHAM", "MAD", str(currency).strip(), flags=re.IGNORECASE)

    if currency == "MAD":
         return "MAD"
    else:
        raise ValueError("currency is not known or not supported")
