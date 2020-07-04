boardsize = directors.groupby(['cusip','fyear'])['director_detail_id'].nunique().rename('boardsize')
independence = directors.groupby(['cusip','fyear'])['independence'].sum()