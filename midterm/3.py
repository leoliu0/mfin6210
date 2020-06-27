directors['fyear'] = pd.to_datetime(directors['meetingdate'])
directors['fyear'] = directors['fyear'].map(lambda s:s.year if s.month>=7 else s.year-1)