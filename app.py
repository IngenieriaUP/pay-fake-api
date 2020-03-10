import pandas as pd
from datetime import datetime
from flask import Flask
from flask_restful import Resource, Api, reqparse, marshal_with

app = Flask(__name__)
api = Api(app)

CARD_NUMBERS = pd.read_csv('card_numbers.csv')['NUMBER'].values.tolist()
print(CARD_NUMBERS)
def verify_card_details(card_number, card_expiration_date, card_name):
    card_number_accepted = card_number in CARD_NUMBERS
    card_name_accepted = card_name != 'Misionsio Salinas'
    card_expiration_date_accepted = card_expiration_date > datetime.today()
    print('card_number_accepted', card_number_accepted)
    print('card_name_accepted', card_name_accepted)
    print('card_expiration_date_accepted',card_expiration_date_accepted)

    if card_number_accepted and card_name_accepted and card_expiration_date_accepted:
        print('all accepted')
        return True
    else:
        return False

parser = reqparse.RequestParser()
parser.add_argument('card_number', type=int, required=True)
parser.add_argument('card_cvc', type=int, required=True)
parser.add_argument('card_expiration_date', type=lambda date_str: datetime.strptime(date_str, '%m/%Y'), required=True)
parser.add_argument('card_name', type=str, required=True)

class Payment(Resource):
    def get(self):
        args = parser.parse_args(strict=True)
        print(args)
        if verify_card_details(args['card_number'], args['card_expiration_date'], args['card_name']):
            return {'Payment Status': 'Payment Received'}

        return {'Payment Status': 'Payment Error. Check your card details or if you have enough fonds'}

api.add_resource(Payment, '/')

# Python Usage
# from requests import get
card_details = {
    'card_number':4242420000000000,
    'card_cvc':987,
    'card_name':'Misionsio Salinas',
    'card_expiration_date':'12/2020'
}
# response = get('http://localhost:5000/', data=card_details).json()

if __name__ == '__main__':
    app.run(debug=False)
