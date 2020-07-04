coverage = analyst.groupby(['cusip','fpedats'])['analys'].nunique().rename('analyst_coverage')
analyst_volatility = analyst.groupby(['cusip','fpedats'])['value'].std().rename('analyst_volatility')
analyst_median = analyst.groupby(['cusip','fpedats'])['value'].median().rename('analyst_median')