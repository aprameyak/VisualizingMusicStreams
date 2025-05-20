import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv('MostStreamed.csv')
df = df[['Track Score', 'Apple Music Playlist Count', 'Amazon Playlist Count', 'Deezer Playlist Count']]

df.fillna({'Apple Music Playlist Count': 0,
           'Amazon Playlist Count': 0,
           'Deezer Playlist Count': 0}, inplace=True)

correl_apple = stats.pearsonr(df['Track Score'], df['Apple Music Playlist Count'])[0]
correl_amazon = stats.pearsonr(df['Track Score'], df['Amazon Playlist Count'])[0]
correl_deezer = stats.pearsonr(df['Track Score'], df['Deezer Playlist Count'])[0]

corA = f"Apple Music Correlation: {correl_apple:.2f}"
corB = f"Amazon Correlation: {correl_amazon:.2f}"
corC = f"Deezer Correlation: {correl_deezer:.2f}"

font1 = {'family': 'serif', 'color': 'purple', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

df.plot(x="Track Score", 
        y=['Apple Music Playlist Count', 'Amazon Playlist Count', 'Deezer Playlist Count'],
        kind="line", figsize=(10, 10))

plt.title('Playlist Count vs Track Score', fontdict=font1)
plt.xlabel('Track Score', fontdict=font2)
plt.ylabel('Playlist Count', fontdict=font2)

plt.figtext(0.67, 0.79, corA)
plt.figtext(0.67, 0.77, corB)
plt.figtext(0.67, 0.75, corC)

plt.tight_layout()
plt.show()
