# Property value calculator
## What is this for
Command line calculator to help work out what property value is affordable and what yearly/monthly savings are required to save for buying a property in a given number of years. 
## Getting started
Setup the environment
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
## Run
With default parameters
```
python calc.py 26500
```
Pass in custom parameters
```
python calc.py 26500 --multiplier 4 --deposit 100000
```
## Notes
* The table is produced for properties from 50,000 to 1,000,000.
* Mortgage deposit is the deposit required for the mortgage.
* Salary deposit is the deposit required to counter salary * multiplier not being enough to reach the desired deposit.
* Savings per year is average savings per year required to reach total deposit.
* --deposit parameter is how much deposit is available and is taken out of total deposit.
### Example
```
# python calc.py 26500 --multiplier 4 --deposit 100000
Deposit £100,000
LTV %15
Saving over 10 years
Salary multiplier x4.0
Salary: £26,500
+------------------+------------+--------------------+------------------+-----------------+--------------------+---------------------+
|   Property value |   Mortgage |   Mortgage deposit |   Salary deposit |   Total deposit |   Savings per year |   Savings per month |
|------------------+------------+--------------------+------------------+-----------------+--------------------+---------------------|
|           50,000 |     42,500 |              7,500 |                0 |               0 |                  0 |                   0 |
|          100,000 |     85,000 |             15,000 |                0 |               0 |                  0 |                   0 |
|          150,000 |    127,500 |             22,500 |           21,500 |               0 |                  0 |                   0 |
|          200,000 |    170,000 |             30,000 |           64,000 |               0 |                  0 |                   0 |
|          250,000 |    212,500 |             37,500 |          106,500 |          44,000 |              4,400 |                 367 |
|          300,000 |    255,000 |             45,000 |          149,000 |          94,000 |              9,400 |                 783 |
|          350,000 |    297,500 |             52,500 |          191,500 |         144,000 |             14,400 |               1,200 |
|          400,000 |    340,000 |             60,000 |          234,000 |         194,000 |             19,400 |               1,617 |
|          450,000 |    382,500 |             67,500 |          276,500 |         244,000 |             24,400 |               2,033 |
|          500,000 |    425,000 |             75,000 |          319,000 |         294,000 |             29,400 |               2,450 |
|          550,000 |    467,500 |             82,500 |          361,500 |         344,000 |             34,400 |               2,867 |
|          600,000 |    510,000 |             90,000 |          404,000 |         394,000 |             39,400 |               3,283 |
|          650,000 |    552,500 |             97,500 |          446,500 |         444,000 |             44,400 |               3,700 |
|          700,000 |    595,000 |            105,000 |          489,000 |         494,000 |             49,400 |               4,117 |
|          750,000 |    637,500 |            112,500 |          531,500 |         544,000 |             54,400 |               4,533 |
|          800,000 |    680,000 |            120,000 |          574,000 |         594,000 |             59,400 |               4,950 |
|          850,000 |    722,500 |            127,500 |          616,500 |         644,000 |             64,400 |               5,367 |
|          900,000 |    765,000 |            135,000 |          659,000 |         694,000 |             69,400 |               5,783 |
|          950,000 |    807,500 |            142,500 |          701,500 |         744,000 |             74,400 |               6,200 |
|        1,000,000 |    850,000 |            150,000 |          744,000 |         794,000 |             79,400 |               6,617 |
+------------------+------------+--------------------+------------------+-----------------+--------------------+---------------------+
```
In this example, average UK salary is used, salary multiplier of x4 and a saved up deposit of £100,000. This shows that the applicant can look at properties worth a bit more then £200,000.
Trying to get a £300,000 property would require an extra deposit of £94,000 which can be saved over 10 years, saving £783 per month.
