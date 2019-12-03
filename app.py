from datetime import date
from flask import Flask, request, abort, jsonify, redirect
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
    content = request.get_json(force=True)

    if content is None:
        print("No content")

    if 'email' not in content:
        abort(400)
    else:
        company = content.get('company')
        contact = content.get('contact')
        email = content.get('email')
        desc = content.get('description')
        newDate = NotionDate(date.today())
        status = 'Lead'

        client = NotionClient(
            token_v2="           bfd1304b470346fe0fdefb04ac0ac10c9c8d65d23e4815c391ce8e98c69036d51aaa1fcb7d13ff5b7505fdd7dc0b83065ef9733ed6440f4956f0be0500d21025c3e7dcc1db388111f294e66972c3")
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
    ip = request.environ['REMOTE_ADDR']
    return redirect(ip, code=302)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
