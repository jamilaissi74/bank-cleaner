import pandas as pd 

CATEGORY_RULES = {
    "income":        ["client"],
    "transport":     ["oncf", "ctm"],
    "subscriptions": ["netflix", "spotify", "youtube"],
    "bills":         ["iam_facture_internet", "amendis", "loyer_appartement"],
    "groceries":     ["boulangerie", "carrefour", "marjane", "bim", "lazyon", "supeco"],
    "necessities":   ["pharmacie", "librairie"],
    "purchases":     ["decathlon", "jumia", "temu"],
    "leisure":       ["cafe", "restaurant", "glovo", "recharge"],
    "fuel":          ["carburant"],
}
DEFAULT_CATEGORY = "others"

def categorize(label):
    for key, value in CATEGORY_RULES.items():
        for keyword in value:
            if keyword in label:
                return key

    return DEFAULT_CATEGORY

def add_category(df_no_duplicates):
    categories=[]
    for row_m6 in df_no_duplicates.itertuples():
        categories.append(categorize(row_m6.label))
    
    df_no_duplicates ['category']=categories
    return df_no_duplicates