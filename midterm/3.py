ceos = executive.loc[executive['ceoann'] == 'CEO']
ceos = ceos.drop_duplicates(['gvkey','fyear'])