import os
import pandas as pd
import scipy as sp
import scipy.stats  as stats
import matplotlib.pyplot as plt

df = pd.read_csv(r'MostStreamed.csv')
data = df[['Track Score','Apple Music Playlist Count', 'Amazon Playlist Count', 'Deezer Playlist Count']]
df = pd.DataFrame(data, columns=['Track Score','Apple Music Playlist Count', 'Amazon Playlist Count', 'Deezer Playlist Count'])

df['Apple Music Playlist Count'] = df['Apple Music Playlist Count'].fillna(0)
df['Amazon Playlist Count'] = df['Amazon Playlist Count'].fillna(0)
df['Deezer Playlist Count'] = df['Deezer Playlist Count'].fillna(0)

correlA = stats.pearsonr(df['Track Score'], df['Apple Music Playlist Count'])
correlB = stats.pearsonr(df['Track Score'], df['Amazon Playlist Count'])
correlC = stats.pearsonr(df['Track Score'], df['Deezer Playlist Count']
                         )
corA = "Apple Music Correlation: " + str(correlA)[25: 29]
corB = "Amazon Correlation: " + str(correlB)[25: 29]
corC = "Deezer Correlation: " + str(correlC)[25: 29]

font1 = {'family':'serif','color':'purple','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

df.plot(x="Track Score", y=['Apple Music Playlist Count', 'Amazon Playlist Count', 'Deezer Playlist Count'],
        kind="line", figsize=(10, 10))

plt.title('Playlist Count Vs Track Score', fontdict=font1)

plt.figtext(.67, .79, corA)
plt.figtext(.67, .77, corB)
plt.figtext(.67, .75, corC)

plt.xlabel('Track Score', fontdict=font2)
plt.ylabel('Playlist Count', fontdict=font2)

plt.show()

