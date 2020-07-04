funda['ln_at'] = np.log(funda['at']+1)
funda['ln_at'].hist(bins=50)
# running the code again will produce the graph, compare it to your own graph to see if the distribution is normal