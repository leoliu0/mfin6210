df['cusip'] = df['cusip'].str[:8]
analyst = analyst.rename({'fpedats':'datadate'},axis=1)