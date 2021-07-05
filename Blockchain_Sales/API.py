from flask import Flask, request, render_template
from copy import copy
import json
import DatabaseManager
import Prediction
import Blockchain as blockC
import Block as block
from Model import Invoice

blockchain = blockC.Blockchain()

db = DatabaseManager.DB()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    return render_template("save_invoice.html", status="")


@app.route('/save_invoice', methods=['POST'])
def save_invoice():
    product = request.form.get('product')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    new_invoice = Invoice(product, quantity, price, '')
    new_block = block.Block(str(new_invoice))

    blockchain.add(new_block)
    db.save_invoice(product, quantity, price)

    return render_template("save_invoice.html", status="Saved Invoice to mysql and Blockchain")


@app.route('/view_invoice', methods=['GET'])
def view_invoice():
    data = db.get_invoice()

    return render_template("view_invoice.html", data=data)


@app.route('/view_block', methods=['GET'])
def view_block():
    temp = copy(blockchain)
    hash = []
    no = []
    data = []

    while temp.head != None:
        hash.append(str(temp.head).split('_')[0])
        no.append(str(temp.head).split('_')[1])
        data.append(str(temp.head).split('_')[2])
        print(temp.head)
        temp.head = temp.head.next
    length = len(hash)

    return render_template("blockchain_view.html", hash=hash, no=no, data=data, length=length)


@app.route('/view_prediction', methods=['GET'])
def view_prediction():
    labels = []
    data = []
    fb = Prediction.FB()
    labels = fb.get_lables()
    data = fb.get_data()
    print(len(labels))
    print(len(data))

    return render_template("prediction_view.html", data=data, labels=labels)


if __name__ == '__main__':
    app.run(debug=True)
