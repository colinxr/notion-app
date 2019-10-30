from notion.client import NotionClient
from notion.block import TextBlock
import sys

from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {"hello": "world"}
        self.wfile.write(json.dumps(response).encode("utf-8"))

        return

    # def do_POST(self):

    #     self.send_response(200)
    #     self.send_header("Content-type", "application/json")
    #     self.end_headers()

    #     response = {"hello": "world"}
    #     self.wfile.write(json.dumps(response).encode("utf-8"))

    #     return



# client = NotionClient(token_v2="9a77f433e1fd89ba5ead35ecc8c1e4d446398843d213840a309f9fd51032aeab94e9da37b9fcf73699f99c5fcfb9281e3431d558cfa80cf4b070eba9fe30b3302d5d53f4f071b8096513708dee9b")

# page = client.get_block('https://www.notion.so/madebyarticle/29fe85ffc337456bb079698ee42ef9d7?v=8cebb3b6b1f048e68c33f7e0720714e0')

# cv = client.get_collection_view(
#     'https://www.notion.so/madebyarticle/bb81bb0ef05547eab80b7a24339a3679?v=19f71a5d05c74810a8ebbf5f76580ca7')


# row = cv.collection.add_row()
# row.company = sys.argv[1]
# row.contact = sys.argv[2]
# row.email = sys.argv[3]
# row.last_contact = sys.argv[4]
# description = row.children.add_new(TextBlock, title=sys.argv[5])
