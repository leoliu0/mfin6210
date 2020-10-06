io['fyear'] = pd.to_datetime(io.rdate).dt.year

io = io.groupby(['cusip','fyear']).mean().reset_index()
