[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

The scatter plot doesn't show a very strong relationship between birth weight and mothers age.

Pearsons is around .068 and Spearmans is around .094, both very low correlation

However taking a look at the percentiles shows there is some pattern to the madness in which birth weight increases the older you get, this pattern very strong in those with young mothers, and then once we reach around 45, birth weights drop drastically.


```python
import numpy as np

import first
import thinkplot
import thinkstats2

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

ages = live.agepreg
weights = live.totalwgt_lb

print('Pearsons', thinkstats2.Corr(ages, weights))
print('Spearmans', thinkstats2.SpearmanCorr(ages, weights))

thinkplot.Scatter(ages, weights, alpha=0.1)
thinkplot.Config(xlabel='age (years)',
                 ylabel='weight (lbs)',
                 xlim=[10, 50],
                 ylim=[0, 15],
                 legend=False)
thinkplot.Show()

bins = np.arange(10, 50, 2)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)

ages = [group.agepreg.mean() for i, group in groups][1:-1]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label=label)

thinkplot.Config(xlabel="mother's age (years)",
               ylabel='birth weight (lbs)')
thinkplot.Show()
```
