import pandas as pd
df=pd.read_csv('weather.csv')
print(df)
grp=df.groupby('Events')
print(grp)
for EST,Events in grp:
    print(EST,Events)