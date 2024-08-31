import scipy.stats

outlook = 4/12
temperature = scipy.stats.norm(72.9697,5.2304).pdf(65)
humidity = scipy.stats.norm(78.8395,9.8023).pdf(70)
wind = 4/11
prioriYes = 0.63
PYes = outlook * temperature * humidity * wind * prioriYes

outlook = 3/8
temperature = scipy.stats.norm(74.8364,7.384).pdf(65)
humidity = scipy.stats.norm(86.1111,9.2424).pdf(70)
wind = 4/7
prioriNo = 1 - prioriYes
PNo = outlook * temperature * humidity * wind * prioriNo

print(PYes/(PYes + PNo))
print(PNo/(PYes + PNo))