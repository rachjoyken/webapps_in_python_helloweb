import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

#Test-Driving Routes | Exercise One:

@app.route('/count_vowels', methods=["POST"])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"'

#Test-Driving Routes | Exercise Two:

@app.route('/sort-names', methods=["POST"])
def post_sort_names():
    if 'names' not in request.form:
        return "You didn't submit any names!", 404
    names = request.form['names'].split(',')
    sorted_names = sorted(names)
    return ','.join(sorted_names)

#Test-Driving Routes | Challenge One:

@app.route('/names', methods = ['GET'])
def get_existing_names():
    if 'add' not in request.args:
        return "You didn't add a name.", 400
    names = 'Julia, Alice, Karim'
    add = request.args['add']
    return f"{names}, {add}"














# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

