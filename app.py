from datetime import date
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
from notion.client import NotionClient
from notion.block import TextBlock
from notion.collection import NotionDate

import sys
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',  methods=['GET'])
@cross_origin()
def hello():
    return jsonify({'done': 'true'}), 201

@app.route('/api/notion', methods=['POST'])
@cross_origin()
def create_row():
    content = request.get_json()
    if 'company' not in content:
        return jsonify({'error': 'false'}), 400
    
    company = content.get('company')
    contact = content.get('contact')
    email = content.get('email')
    desc = content.get('description')
    newDate = NotionDate(date.today())
    status = 'Lead'

    client = NotionClient(
        token_v2="9a77f433e1fd89ba5ead35ecc8c1e4d446398843d213840a309f9fd51032aeab94e9da37b9fcf73699f99c5fcfb9281e3431d558cfa80cf4b070eba9fe30b3302d5d53f4f071b8096513708dee9b")
    cv = client.get_collection_view(
        'https://www.notion.so/madebyarticle/29fe85ffc337456bb079698ee42ef9d7?v=8cebb3b6b1f048e68c33f7e0720714e0')
    
    row = cv.collection.add_row()
    row.icon = '🤖'
    row.company = company
    row.contact = contact
    row.email = email
    row.last_contact = newDate
    row.status = status
    row.children.add_new(TextBlock, title=desc)

    return jsonify({'done': 'true'}), 201

@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
