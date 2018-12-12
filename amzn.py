import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import chartify

# data
NYC = pd.DataFrame([])
initRev = 10*10**9/20
NYC['Total Tax Revenue'] = [initRev + initRev*x for x in range(20)]
initSub = 1.525*10**9/10
NYC['Total Subsidy'] = [initSub + initSub*x for x in range(10)]+[0 for x in range(10)]
for i in range(10,20):
    NYC.iloc[i,1] = NYC.iloc[9,1]
initNet = NYC.iloc[9,0] - NYC.iloc[9, 1]
NYC['Net Tax Revenue'] = [NYC.iloc[i,0] - NYC.iloc[i,1] for i in range(20)]# +\
        #[initRev+initNet + initRev*x for x in range(10)]
VA = pd.DataFrame([])
initRev2 = 3.2*10**9/20
VA['Total Tax Revenue'] = [initRev2 + initRev2*x for x in range(20)]
initSub1 = 550*10**6/12
sub1 = [initSub1 + initSub1*x for x in range(12)]+[0 for x in range(8)]
for i in range(12,20):
    sub1[i] = sub1[11]
initSub2 = 23*10**6/15
sub2 = [initSub2 + initSub2*x for x in range(15)]+[0 for x in range(5)]
for i in range(15,20):
    sub2[i] = sub2[14]
VA['Total Subsidy'] = [sub1[i] + sub2[i] for i in range(20)]
initNet2 = VA.iloc[15,0] - VA.iloc[15, 1]
VA['Net Tax Revenue'] = [VA.iloc[i,0] - VA.iloc[i,1] for i in range(20)]

NYC = NYC/ 10**9
VA = VA / 10**9

# plotting 

fig, (ax1,ax2) = plt.subplots(1,2, sharey=True)
plt.suptitle("Amazon's New HQ Impact on NYC/VA")

ax1.set_ylabel("Billion Dollars")
ax1.set_xlabel("Year")
ax1.set_title("NYC")
t = np.arange(2019, 2039, 1)
ax1.plot(t, NYC['Total Subsidy'], 'r-', label='Total Subsidy')
ax1.plot(t, NYC['Total Tax Revenue'], 'g-', label='Total Tax Revenue')
ax1.plot(t, NYC['Net Tax Revenue'], 'b-', label='Net Tax Revenue')
ax1.grid(True)

ax2.set_title("VA")
ax2.set_ylabel("Billion Dollars")
ax2.set_xlabel("Year")
z = np.arange(2019, 2039, 1)
ax2.plot(z, VA['Total Subsidy'], 'r-', label='Total Subsidy')
ax2.plot(z, VA['Total Tax Revenue'], 'g-', label='Total Tax Revenue')
ax2.plot(z, VA['Net Tax Revenue'], 'b-', label='Net Tax Revenue')
ax2.grid(True)
ax2.legend(loc='upper right')
ax2.text(2035, -1.75, "Author: Geoff Langenderfer", fontsize = 5)

plt.show()
