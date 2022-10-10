import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

train = pd.read_parquet('../data/train_after.parquet')
test = pd.read_parquet('../data/test_after.parquet')


def survived_table(feature):
    return train[[feature, "target"]].groupby([feature], as_index=False).mean().sort_values(by='target', ascending=False).style.background_gradient(low=0.75,high=1)


def survived_bar_plot(feature):
    plt.figure(figsize = (5,3))
    sns.barplot(data = train , x = feature , y = "target").set_title(f"{feature} Vs Target")
    plt.show()

plt.figure()

sns.displot(train['vehicle_restricted'])
plt.title('road_in_use'+"Kernel Density Plot")
plt.show()
