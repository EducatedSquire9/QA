import pandas as pd
import DatabaseManager
from prophet import Prophet
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

DB = DatabaseManager.DB()


class FB:
    def __init__(self):
        i_list = DB.get_invoice()
        f = open("Dataset/data.csv", "w")
        f.write("{},{}\n".format('ds', 'y'))
        for i in i_list:
            f.write("{},{}\n".format(i[3], i[1]))
        f.close()
        self.labels = []
        self.data = []
        self.do_predict()

    def get_path(self):
        return self.path

    def do_predict(self):
        df = pd.read_csv('Dataset/sample.csv')
        df.head()
        m = Prophet()
        m.fit(df)

        future = m.make_future_dataframe(periods=30)
        future.tail()

        forecast = m.predict(future)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

        for x in forecast['ds']:
            self.labels.append(str(x).split(" ")[0])
        for x in forecast['yhat']:
            self.data.append(round(x, 2))

    def get_lables(self):
        return self.labels

    def get_data(self):
        return self.data
