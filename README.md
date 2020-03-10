# pay-fake-api

This repo allows to use a (too) simple payment API from your localhost (also available online). Pull requests are welcomed!

## Quick Start:

```python
from requests import get

card_details = {
    'card_number': 4242420000000000, # Python int object, Accepted cards numbers are in the file 'card_numbers.csv'
    'card_cvc': 987, # Python int object, Any int is accepted 
    'card_name': 'Random Name', # Python str object, 
    'card_expiration_date': '12/2020' # Date in format %m/%Y
}

response = get('http://pay-fake.herokuapp.com/', data=card_details).json()
print(response)
```

This prints:

```sh
{'Payment Status': 'Payment Received'}
```

If card_name is 'Misionsio Salinas' the payment is rejected or the card_number is not in the accepted card_numbers list the output would be:

```sh
{'Payment Status': 'Payment Error. Check your card details or if you have enough fonds'}
```

## Another alternative is to use your local server

```sh
$ git clone repo && cd repo
$ pip3 install virtualenv && virtualenv .env && source .env/bin/activate
(.env) $ pip install -r requirements.txt
(.env) $ python app.py
```

**Usage**: Once your local server is up and running, replace the line 
```python
response = get('http://pay-fake.herokuapp.com/', data=card_details).json()
``` 
with  
```python 
response = get('http://localhost:5000/', data=card_details).json()
```
to use the API hosted on your local machine.  
