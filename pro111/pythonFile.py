import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random



marks = pd.read_csv("data.csv")
markslist = marks["reading_time"].tolist()

meanP = statistics.mean(markslist)
sDevP = statistics.stdev(markslist)


def randomSet_mean(counter):
    data_set = []

    for i in range(0,counter):
        index = random.randint(0,len(markslist) - 1)
        value = markslist[index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    sDev = statistics.stdev(data_set)

    return(mean)



mean_list = []

for i in range(0,1000):
    setOfMeans = randomSet_mean(100)
    mean_list.append(setOfMeans)

mean = statistics.mean(mean_list)
sDev = statistics.stdev(mean_list)

print("mean = ",mean)
print(meanP)
print("sDev =", sDev)

z_score = (mean - meanP)/sDev

print("z score = ", z_score)


sdev1s = mean - sDev
sdev2s = mean - (2*sDev)
sdev3s = mean - (3*sDev)
sdev1e = mean + sDev
sdev2e = mean + (2*sDev)
sdev3e = mean + (3*sDev)

fig = ff.create_distplot([mean_list], ['marks'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [sdev1s,sdev1s], y = [0,1], mode = "lines", name = "1st sDev start"))
fig.add_trace(go.Scatter(x = [sdev1e,sdev1e], y = [0,1], mode = "lines", name = "1st sDev end"))
fig.add_trace(go.Scatter(x = [sdev2s,sdev2s], y = [0,1], mode = "lines", name = "2nd sDev start"))
fig.add_trace(go.Scatter(x = [sdev2e,sdev2e], y = [0,1], mode = "lines", name = "2nd sDev end"))
fig.add_trace(go.Scatter(x = [sdev3s,sdev3s], y = [0,1], mode = "lines", name = "3rd sDev start"))
fig.add_trace(go.Scatter(x = [sdev3e,sdev3e], y = [0,1], mode = "lines", name = "3rd sDev end"))
fig.show()




