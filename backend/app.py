from typing import Tuple, List

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


def validate_args(
    body: dict, required_args: List[Tuple[str, type]], optional_args: List[Tuple[str, type]] = []
) -> Tuple[Tuple[Response, int]]:
    """Checks that required args are present, and that required and optional args are of
    the correct type. If so, returns body with coerced types. Otherwise, returns error
    response for Flask.

    :param body <dict> args body
    :param required_args <list> list of (arg, type) which are required to be in body
    :param optional_args <list> list of (arg, type) which can be in body
    :returns (coerced data, (tuple of Flask Response and int, which is what flask expects for a
        response))
    """

    if body is None:
        return None, create_response(status=422, message='Missing body')

    missing_args = []
    invalid_args = []

    coerced_body = {}

    for arg, type_ in required_args:
        if arg not in body or not body[arg]:
            missing_args.append(arg)
        else:
            try:
                coerced_body[arg] = type_(body[arg]) 
            except:
                invalid_args.append(arg)

    for arg, type_ in optional_args:
        if arg in body:
            try:
                coerced_body[arg] = type_(body[arg]) 
            except:
                invalid_args.append(arg)

    if missing_args or invalid_args:
        error_msg = ''

        if missing_args:
            error_msg += f'Missing args: {", ".join(missing_args)}   '
        if invalid_args:
            error_msg += f'Invalid args: {", ".join(invalid_args)}'

        return None, create_response(status=422, message=error_msg)

    return coerced_body, None

"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)


# Parts 1 & 3
@app.route("/restaurants", methods=['GET'])
def get_all_restaurants():
    args, error = validate_args(request.args, [], [('minRating', int)])
    if error:
        return error

    restaurants = db.get('restaurants')
    minRating = args.get('minRating', 0)

    filtered_restaurants = [restaurant for restaurant in restaurants if \
        restaurant['rating'] >= minRating]

    return create_response({"restaurants": filtered_restaurants})


# Part 4
@app.route("/restaurants", methods=['POST'])
def new_restaurant():
    body, error = validate_args(request.json, [('name', str), ('rating', int)])
    if error:
        return error

    restaurant = db.create('restaurants', body)
    return create_response(restaurant, status=201)


# Part 2
@app.route("/restaurants/<int:id>", methods=['GET'])
def get_restaurant(id):
    restaurant = db.getById('restaurants', id)
    if restaurant is None:
        return create_response(status=404, message="No restaurant with this id exists")

    return create_response(restaurant)


# Part 5
@app.route("/restaurants/<int:id>", methods=['PUT'])
def update_restaurant(id):
    body, error = validate_args(request.json, [], [('name', str), ('rating', int)])
    if error:
        return error

    restaurant = db.updateById('restaurants', id, body)
    if restaurant is None:
        return create_response(status=404, message="No restaurant with this id exists")

    return create_response(restaurant)


# Part 6
@app.route("/restaurants/<int:id>", methods=['DELETE'])
def delete_restaurant(id):
    if db.getById('restaurants', id) is None:
        return create_response(status=404, message="No restaurant with this id exists")
    db.deleteById('restaurants', id)
    return create_response(message="Restaurant deleted")


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
