import pandas as pd
import plotly.graph_objects as go


def load_data():
    return pd.read_csv('/path/monitor/2021-01-26.csv', sep=";")
    # return pd.read_csv('https://raw.githubusercontent.com/FBosler/AdvancedPlotting/master/combined_set.csv')


def create_topics():
    values = data.groupby(['TOPICS']).size()
    labels = data['TOPICS']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    img_bytes = fig.to_image(format="svg")
    new_file = open("topics.svg", "wb")
    new_file.write(img_bytes)
    new_file.close()


def create_senders():
    values = data.groupby(['SENDER']).size()
    labels = data['SENDER']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    img_bytes = fig.to_image(format="svg")
    new_file = open("sender.svg", "wb")
    new_file.write(img_bytes)
    new_file.close()


if __name__ == '__main__':
    data = load_data()
    create_topics()
    create_senders()
