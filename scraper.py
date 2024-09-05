import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 根据实际情况提取数据
    data = {'title': soup.title.string}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
