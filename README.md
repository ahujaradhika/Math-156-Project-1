# Neural Networks and Traffic Flow

## Introduction

**Purpose and Project Goal**:  With the increasing popularity of ride sharing apps such as Uber
and Lyft, it is paramount for these companies to determine trends in taxi cab fares in order to
have additional information on the competition. It is also important for ride sharing companies
to analyze the trends in how their customers consume their services. With this in mind, we set
out to build a model to predict the cost of a taxi ride and determine the times of day which have
the greatest price surges.

**The Dataset**: We used a data set on Kaggle [2] with information about New York City taxi rides
to use for our input features which contained the associated fare values for these rides that we
could use for our target output. The data set itself contained millions of rows of data but with
limited time and computing power, we chose to randomly extract 20,000 points from the data,
with 80% being used for training and 20% being used for testing. The following were the input
features:
- pickup_datetime - timestamp value indicating when the taxi ride started.
- pickup_longitude - float for longitude coordinate of where the taxi ride started.
- pickup_latitude - float for latitude coordinate of where the taxi ride started.
- dropoff_longitude - float for longitude coordinate of where the taxi ride ended.
- dropoff_latitude - float for latitude coordinate of where the taxi ride ended.
- passenger_count - integer indicating the number of passengers in the taxi ride.

The target output was the following field:
- fare_amount - float dollar amount of the cost of the taxi ride.

**Overview of the Methodology**: We split this project into four main parts:
1. **Pre-processing the data** - clean and normalize the data entries so they can be effectively
fed into models.
2. **Explore Different Models** - research different machine learning models and methodologies before deciding on the optimal methods to use.
3. **Build the Model** - choose and build a model with the necessary parameters (ex. For a Neural Network, determine the number and type of layers as well as the activation functions).
4. **Test the Model and Obtain Insights** - Execute the model on test data and determine the
most valuable takeaways from the research.

## Model and Optimization Program

## Implementation

**The Haversine Function**: The pick-up and drop-off locations are in degrees latitude and longitude. As we want straight-line distance as an input for our neural network, we use the Haversine function to find the shortest great-circle distance over the Earth’s surface between the latitude-longitude coordinates of the pick-up and drop-off, with the answer returned in kilometres.

**Cleaning the Data**: We clean the data before feeding it into the neural network to catch incorrectlyentered data. We require that each ride has
- Haversine distance < 30km
- cost < $75
- year ∈ {2001, 2002, . . . , 2019}
We also require for simplicity that each ride has passenger count = 1, and for general use, the
model can be retrained with a passenger count of 2, etc.

**Cutting out Manhattan**: Upon graphing pick-up and drop-off locations on a map of New York
City (see figures below), we notice that the Haversine function will be less accurate if a ride
starting on the island of Manhattan does not stay confined to Manhattan. This is because the taxi
will first have to travel to a bridge and then to the drop-off, and the straight-line distance will be
an inaccurate measure of the distance.

To make our model more accurate, albeit at the expense of limiting its use, we restrict our data
set to rides that begin and end in Manhattan. We identified the points A, B, C, and D as the
vertices of a quadrilateral that enclose Manhattan,

A = (40.693598, −74.043508)   B = (40.887045, −73.935076)
C = (40.796631, −73.928354)   D = (40.709264, −73.977696)



