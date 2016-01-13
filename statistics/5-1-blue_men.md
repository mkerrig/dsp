[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


0.342094682946 or 34.2% of men are in this range

```python
import scipy.stats
mu = 178
sigma = 7.7
d = scipy.stats.norm(loc=mu, scale=sigma)
five10 = d.cdf(177.8)
six1 = d.cdf(185.4)
print six1-five10

```
