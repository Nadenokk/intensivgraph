import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
x=pd.read_csv('z.csv', index_col='z, М')
plt.ylabel('I')
x.plot(figsize=(15, 10))
plt.savefig('out')