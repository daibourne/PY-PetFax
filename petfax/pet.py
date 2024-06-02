import json
from flask import (Blueprint, render_template, Flask)# type: ignore

pets = json.load(open('pets.json'))
print(pets[2])

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<pet_name>')
def show_pet(pet_name):
    pet = [pet for pet in pets if pet.get('pet_name')==pet_name][0]
    if pets:
        print(f'Found pet: {pets}')
        return render_template('show.html', pet=pet)
    else:
        print('pet not found')
        return 'Pet Not Found', 404
    
@bp.route('/new')
def new_fact():
    return render_template('new_fact.html')
        

if __name__ == '__main__':
    bp.run(debug=True) 