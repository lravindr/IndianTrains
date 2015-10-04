__author__ = 'lokesh'

import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show


def numberOfRows(x):
    return len(x.index)

#Data obtained from data.gov.in
indianTrainDataset = pd.read_csv('isl_wise_train_detail_03082015_v1.csv')

#Convert pandas object to 32-bit integers
indianTrainDataset['Train No.'] = np.int32(indianTrainDataset['Train No.'].str.replace("'",""))

#Datset contain information of all trains along with the train stops. The set of unique
# trains can be calculated by finding all the train numbers and finding the unique set amongst them.
numberofTrains = indianTrainDataset['Train No.'].unique().size
print "Number of trains run by Indian Railways is "+str(numberofTrains)+"."

#Average number of stops by an Indian train is the number of stops/number of trains.
averageNumberOfStops = numberOfRows(indianTrainDataset)/numberofTrains
print "On an average Indian trains travel over "+ str(averageNumberOfStops)+" stops."

#Maximum number of stops by any train
stopsByEachTrain = indianTrainDataset['Train No.'].value_counts()

# output to static HTML file
output_file("numstations.html", title="Line plot of number of stations vs number of trains")

p = figure(title="Simple plot of trains versus stations",x_axis_label='No. of stations',y_axis_label='No. of trains')
p.line(stopsByEachTrain.value_counts(), stopsByEachTrain.value_counts().index)
show(p)

#Some trains have the complete train info http://etrain.info/in?TRAIN=12227#!TRAIN=59386
print numberOfRows(indianTrainDataset[indianTrainDataset['Train No.']==59386])

# and some trains dont ...http://etrain.info/in?TRAIN=12227
print numberOfRows(indianTrainDataset[indianTrainDataset['Train No.']==12227])