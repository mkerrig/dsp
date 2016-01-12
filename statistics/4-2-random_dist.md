[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)
The distribution is uniform, the CDF produced a near straight line, the PMF was however not very useful

```python
import random
import thinkstats2
import thinkplot
#PMF
val = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(val)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()
#CDF
cdf = thinkstats2.Cdf(val)
thinkplot.Cdf(cdf)
thinkplot.Show()

```
