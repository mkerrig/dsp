[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
I think this was pretty straight forward, used examples I found in the existing code
 The means are:
* Actual: 1.02420515504
* Biased: 2.40367910066

```python
import math
import numpy as np

import nsfg
import thinkstats2
import thinkplot
import first

dct = thinkstats2.ReadStataDct('2002FemResp.dct')
df = dct.ReadFixedWidth('2002FemResp.dat.gz', compression='gzip', nrows=None)
pmf = thinkstats2.Pmf(df.numkdhh)
bias_pmf = pmf.Copy(label='biased')
for i, j in pmf.Items():
  bias_pmf.Mult(i, i)

bias_pmf.Normalize()
thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, bias_pmf])
print pmf.Mean()
print bias_pmf.Mean()

thinkplot.Show()



```


