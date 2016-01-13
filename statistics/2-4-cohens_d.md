[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Cohen d -0.0886729270726
I pretty much just followed the format in first.py and the replaced the variables with totalwgt_lb from the pregnancy length
####################################################################################################################################
from __future__ import print_function
```python
import math
import numpy as np

import nsfg
import thinkstats2
import thinkplot
import first

live, firsts, others = first.MakeFrames()
d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print('Cohen d', d)
```


