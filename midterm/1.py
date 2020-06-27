std_ret = ret.groupby(['permno','fyear']).ret.std().rename('std') # rename the series
ret['ret'] = ret['ret'] + 1 # add one to returns for calculating products
aret = ret.groupby(['permno','fyear']).ret.prod() - 1 # converting to annual returns
stock_return = pd.concat([aret,std_ret],axis=1).reset_index() # merging two dataset together