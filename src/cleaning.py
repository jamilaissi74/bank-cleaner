from datetime import date
import re  
import pandas as pd
from unidecode import unidecode

EUR_TO_MAD=10.93     # RATE of conversion from EUR to MAD

def label_normalizing(label):
    if pd.isnull(label) or str(label).strip() == "":
            raise ValueError("label is empty")
    label=str(label)
    a=label.strip()
    a=a.lower()
    a=str(re.sub(" +", "_", a))
    a=unidecode(a)
    return a

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

def amount_cleaning(amount, currency):
    if pd.isnull(amount) or str(amount).strip() == "":
            raise ValueError("amount is empty")
    amount=str(amount).strip()
    amount= str(re.sub(" +", "", amount))
    amount= str(re.sub(",", ".", amount))
    amount= pd.to_numeric(amount,  errors='raise')
    currency=currency_normalizing(currency)
    if currency == "EUR":
        amount = amount * EUR_TO_MAD
    amount=float(amount)
    return round(amount, 2)