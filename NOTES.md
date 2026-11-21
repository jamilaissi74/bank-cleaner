first we have 4 collumns : date , name of what we bought , the amount , and the currency 
<ul>
    <li>in b the columns are seperated by ; while in c and a it's a , </li>
    <li>in a the date is seprated by - but in b it's seperated with / and c is a mixture</li> 
    <li>THE AMMOUNT  some are between "" bcz the decimal are separated with , while others it's just a dot , some are - some are positive numbers , in some cases the isn't a specific number or it's letters </li>
    <li>in c the currency is mixed between euro and mad</li> 
    <li>even the name of the columns are not unified </li>
    <li>there are different versions of the same purchase </li>
    file b is considered to have one columns
</ul>


## what we need at the end 
<ul>
    <li>HOW MUCH WE SPEND IN A MONTH </li>
    <li>HOW MUCH WE SPENT BY CATEGORY</li>
</ul>

<ol>
    <li>read the files  </li>
    <li>clean data , unify data</li>
    <li>reject unusable data output in rejects.csv</li>
    <li>put each row in a category based on its name</li>
    <li>output : month total of expenses + total of expenses per category</li>
</ol>

## the 3 question my programm should answer 

<ol>
    <li>how much did i spend per month  </li>
    <li>how much did i spend per category</li>
    <li>how much did i receive </li>
</ol>

## the  5lines of expected output 
on month 5 you spend total : 7000dh
on FOOD : 1000dh
on GROCERIES : 500dh
on TRANSPORTATION :1000dh
on SUBSCRIPTIONS : 200dh 

## questions for M2
How do you read a CSV file in Python?
How do you change the separator for banque_b.csv?
How do you loop over every file in a folder? <----------- what ?


when i run df.head() it gives me the first 5 rows
df.shap gives me how many rows and columns 
df.columns gives me the columns name and their type 

i choose pandas because it's easy and straight to the point 


# I'm in M3 and the prob is how do i know if it's a day or month !!!!


## put this in read me file : Dates passed should be either iso or d/m/y

## LIL MODIFICATIONS ON LABEL TO DO LATER 

## dependencies i installed unidecode 


## les doublons sont the ones where  date,amount, and name is the same 

## the first occurences in duplicates.csv are kept 
## the file_name is not part of the decision of duplicates because there can be duplicates across multiple banks

## “M5: simplify the duplicates block with masks, and add a kept/removed status”.

----------M6----------------
# categories: 
outcome:
transportation: oncf ,ctm
online subscriptions:netflix,spotify,youtube
bills: iam_facture_internet, amendis_eau_elec,amendis,loyer_appartement
groceries: boulangerie ,carrefour, market,marjane, bim,lazyon,supeco
necessities (health, education):pharmacie,librairie
purchases(clothings):decathlon,jumia, temu, 
leisure(going out,fast food,...):cafe, restaurant,glovo,recharge
others: ...
carburant:afriquia_carburant, carburant
income :
work : client
others:....


i use keywords, and exact matching 
others has anything that doesnt match the categories


##
-every negative number is an expense
-report income seperately too , maybe add income - expense = to see if i got something left 
-maybe put expenses in a positive number but make it red if possible + explicitly state that they are expenses
-it's a calendar month for sure , months with 0 spending are shown  too
-i think it's month : category : total 
 -it's always 2decimals 