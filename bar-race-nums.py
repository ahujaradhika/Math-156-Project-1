import pandas as pd
import math

PATH = 'fares_by_hour/hour-'
HOURS = 24

final = {'Distance': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
final_df = pd.DataFrame(data=final)

for i in range(HOURS):
    data = pd.read_csv(PATH + str(i) + '.txt')

    # create column with floor distance for easy averages
    floor_dist = list()
    for j in range(len(data.index)):
        floor_dist.append(math.floor(data['distance'][j]))
    data['floor-dist'] = floor_dist
    data.drop(columns=['distance', 'hour'], inplace=True)

    # get average by floored distance andd add to new df
    df = data.groupby('floor-dist').mean()
    final_df['Hour ' + str(i)] = df['fare']  
    
final_df.to_csv(path_or_buf='bar-race-data.csv', index=False)