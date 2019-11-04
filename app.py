from flask import Flask, request, abort, jsonify
from notion.client import NotionClient
from notion.block import TextBlock

import sys
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask!"

# @crossdomain(origin='*', headers=['access-control-allow-origin', 'Content-Type'])
@app.route('/api/notion', methods=['POST'])
def create_row():
    # raise exception(request)
    content = request.get_json(force=True)

    # if not request.form:
        # abort(400, 'it broke dood')


    return content, 201

    # company = request.form.get('company')
    # contact = request.form.get('contact')
    # email = request.form.get('email')
    # desc = request.form.get('description')

    company = content.get('company')
    contact = content.get('contact')
    email = content.get('email')
    desc = content.get('description')

    client = NotionClient(
        token_v2="9a77f433e1fd89ba5ead35ecc8c1e4d446398843d213840a309f9fd51032aeab94e9da37b9fcf73699f99c5fcfb9281e3431d558cfa80cf4b070eba9fe30b3302d5d53f4f071b8096513708dee9b")
    cv = client.get_collection_view(
        'https://www.notion.so/madebyarticle/bb81bb0ef05547eab80b7a24339a3679?v=19f71a5d05c74810a8ebbf5f76580ca7')

    row = cv.collection.add_row()
    row.company = company
    row.contact = contact
    row.email = email
    row.children.add_new(TextBlock, title=desc)

    return jsonify({'done': 'true'}), 201

if __name__ == '__main__':
    app.run()
