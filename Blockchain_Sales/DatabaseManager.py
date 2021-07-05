from datetime import datetime
import mysql.connector as mysql


class DB:
    def __init__(self):
        self._conn = mysql.connect(
            host="localhost",
            user="root",
            password="password",
            database="blockchain_sale"
        )
        self._c = self._conn.cursor()

    def get_invoice(self):
        self._c.execute("SELECT * FROM invoice")
        invoice = self._c.fetchall()
        returnInvoice = []
        for i in range(0, len(invoice)):
            returnInvoice.append((invoice[i][1], invoice[i][2], invoice[i][3], invoice[i][4]))
        return returnInvoice

    def save_invoice(self, product, quantity, price):
        sql = "INSERT INTO invoice (product, quantity, price, date_time) VALUES (%s, %s, %s, %s)"
        val = (product, quantity, price, datetime.today().strftime('%Y-%m-%d'))
        self._c.execute(sql, val)
        self._conn.commit()

    def clean_invoice(self):
        self._c.execute('DELETE FROM assignment')


# db = DB()
# # db.save_invoice('sdfs', 89, 90.0)
# x = db.get_invoice()
# for i in x:
#     print(i)