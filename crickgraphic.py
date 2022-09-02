import plotly.graph_objects as go

import pandas as pd


dataset = pd.read_csv('C:\Users\jaravin1\Desktop\ipl\IPL-ML-2018-master\IPL-ML-2018-master\Dataset\ip.csv')

Seasons = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017",
         "2018"]

# make list of citys
citys = []
for city in dataset["city"]:
    if city not in citys:
        citys.append(city)
# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}

# fill in most of layout
fig_dict["layout"]["xaxis"] = {"range": [30, 85], "title": "Life Expectancy"}
fig_dict["layout"]["yaxis"] = {"title": "GDP per Capita", "type": "log"}
fig_dict["layout"]["hovermode"] = "closest"
fig_dict["layout"]["sliders"] = {
    "args": [
        "transition", {
            "duration": 400,
            "easing": "cubic-in-out"
        }
    ],
    "initialValue": "1952",
    "plotlycommand": "animate",
    "values": Seasons,
    "visible": True
}
fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 500, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]

sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "Season:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
}

# make data
Season = 1952
for city in citys:
    dataset_by_Season = dataset[dataset["Season"] == Season]
    dataset_by_Season_and_cont = dataset_by_Season[
        dataset_by_Season["city"] == city]

    data_dict = {
        "x": list(dataset_by_Season_and_cont["team2"]),
        "y": list(dataset_by_Season_and_cont["winner"]),
        "mode": "markers",
        "text": list(dataset_by_Season_and_cont["team1"]),
        "marker": {
            "sizemode": "area",
            "sizeref": 200000,
            "size": list(dataset_by_Season_and_cont["pop"])
        },
        "name": city
    }
    fig_dict["data"].append(data_dict)

# make frames
for Season in Seasons:
    frame = {"data": [], "name": str(Season)}
    for city in citys:
        dataset_by_Season = dataset[dataset["Season"] == int(Season)]
        dataset_by_Season_and_cont = dataset_by_Season[
            dataset_by_Season["city"] == city]

        data_dict = {
            "x": list(dataset_by_Season_and_cont["team2"]),
            "y": list(dataset_by_Season_and_cont["winner"]),
            "mode": "markers",
            "text": list(dataset_by_Season_and_cont["team1"]),
            "marker": {
                "sizemode": "area",
                "sizeref": 200000,
                "size": list(dataset_by_Season_and_cont["pop"])
            },
            "name": city
        }
        frame["data"].append(data_dict)

    fig_dict["frames"].append(frame)
    slider_step = {"args": [
        [Season],
        {"frame": {"duration": 300, "redraw": False},
         "mode": "immediate",
         "transition": {"duration": 300}}
    ],
        "label": Season,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)


fig_dict["layout"]["sliders"] = [sliders_dict]

fig = go.Figure(fig_dict)

fig.show()
