import re
import os
import sys
import matplotlib.pyplot as plt

rgx100 = re.compile('^<p>F100:0$')
rgx0 = re.compile('^<p>F101:\d+$')
rgxend = re.compile('^</p>$')

if "__main__" == __name__ and sys.argv[1:]:
    for htm in sys.argv[1:]:
      if not htm.endswith('.htm'): continue
      bn = os.path.basename(htm)
      with open(htm,'r') as fin:
        sinarr = list()
        for rawline in fin:
          toks = rawline.strip().split()
          if len(toks) < 4: continue
          if not (None is rgx100.match(toks[0])):
            scaling = toks[2]
            continue
          if None is rgx0.match(toks[0]): continue
          if None is rgxend.match(toks[-1]): continue
          sinarr.extend(map(float,toks[1:-1]))
        plt.plot(sinarr)
        plt.ylabel('SIN(X)')
        plt.xlabel('C5:1.ACC')
        plt.title('{0}:  scaling={1}'.format(bn,scaling))
        plt.show()
