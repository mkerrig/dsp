[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

Sample size of 10 results:

('stderr', 0.3377050619352654)

('ci', (1.6068542339409468, 2.4707276582537223))

Notable patterns are as sampling population increases, the confidence interval becomes more narrow, and the standard error decreases, both as one would expect them to.

```python
import thinkstats2
import thinkplot

import random
import numpy as np

from scipy import stats
from estimation import RMSE, MeanError

stderrlst=[]
nlist = [10,50,100,200,300,500,750,1000]
for n in nlist:
  sim = []
  for i in range(n):
    rand = np.random.exponential(1.0/2, n)
    lam = 1.0 / np.mean(rand)
    sim.append(lam)

  stderr = RMSE(sim, 2)
  cdf = thinkstats2.Cdf(sim)
  ci = cdf.Percentile(10), cdf.Percentile(90)
  print('stderr', stderr)
  print('ci', ci)
  stderrlst.append(stderr)
  thinkplot.Cdf(cdf)
  thinkplot.Config(xlabel='estimate',
                  ylabel='CDF',
                  title='Sampling dist')
  thinkplot.Show()

thinkplot.Scatter(nlist,stderrlst)
thinkplot.Config(xlabel='Sample Size',
                ylabel='Standard Error',
                title = 'Standard Error Vs. Sample Size')
thinkplot.Show()
```
