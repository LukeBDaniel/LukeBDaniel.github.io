---
layout: post
title: "Why The A's Left Oakland"
date: 2025-05-30
---


#### An analysis of the attendance issues of the Oakland A's, and whether Oakland is capable of hosting a Major League team.

The Oakland Athletics' departure from the Bay Area has been attributed to low attendance. But was it really that simple? This analysis examines decades of attendance data and team performance to see how the A's compared to the rest of Major League Baseball.




















    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_8_0.png)
    




    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_8_1.png)
    







    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_9_0.png)
    




    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_9_1.png)
    







    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_10_0.png)
    




    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_10_1.png)
    


To understand Oakland's attendance in context, we need to compare it to the rest of the league.







    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_12_0.png)
    




    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_12_1.png)
    







    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_13_0.png)
    




    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_13_1.png)
    





Even when accounting for league-wide trends, Oakland's attendance consistently ranked among the worst in baseball. Despite competitive seasons, the A's rarely climbed above the bottom tier.






    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Input In [12], in <cell line: 12>()
         14 for year in range(1968, 2025):
         15     try:
    ---> 16         temp = mlb.schedule_and_record(year, team)
         17         temp["Year"] = year
         18         temp = temp[['Date', 'Tm', 'Opp', 'Home_Away', 'W/L', 'R', 'RA', 'W-L',
         19                      'Rank', 'GB', 'D/N', 'Attendance', 'cLI', 'Streak', 'Year']]


    File ~/opt/anaconda3/lib/python3.9/site-packages/pybaseball/cache/cache.py:58, in df_cache.__call__.<locals>._cached(*args, **kwargs)
         55 result = self._safe_load_func_cache(func_data)
         57 if result is None:
    ---> 58     result = func(*args, **kwargs)
         59     if len(result) > 0:
         60         self._safe_save_func_cache(func_data, result)


    File ~/opt/anaconda3/lib/python3.9/site-packages/pybaseball/team_results.py:129, in schedule_and_record(season, team)
        126 if season > datetime.now().year:
        127     raise ValueError('Season cannot be after current year')
    --> 129 soup = get_soup(season, team)
        130 table = get_table(soup, team)
        131 table = process_win_streak(table)


    File ~/opt/anaconda3/lib/python3.9/site-packages/pybaseball/team_results.py:23, in get_soup(season, team)
         21 url = "http://www.baseball-reference.com/teams/{}/{}-schedule-scores.shtml".format(team, season)
         22 print(url)
    ---> 23 s = session.get(url).content
         24 return BeautifulSoup(s, "lxml")


    File ~/opt/anaconda3/lib/python3.9/site-packages/pybaseball/datasources/bref.py:30, in BRefSession.get(self, url, **kwargs)
         28     sleep_length = (60 / self.max_requests_per_minute) - delta.total_seconds()
         29     if sleep_length > 0:
    ---> 30         sleep(sleep_length)
         32 self.last_request = datetime.datetime.now()
         34 return self.session.get(url, **kwargs)


    KeyboardInterrupt: 





    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Input In [17], in <cell line: 1>()
    ----> 1 sns.boxplot(data=all_teams, x='Tm', y='Attendance', order = all_teams.groupby('Tm')['Attendance'].mean().sort_values(ascending = False).index)
          2 plt.title('Attendance Distribution by Team')
          3 plt.xticks(rotation=90)


    File ~/opt/anaconda3/lib/python3.9/site-packages/pandas/core/frame.py:7721, in DataFrame.groupby(self, by, axis, level, as_index, sort, group_keys, squeeze, observed, dropna)
       7716 axis = self._get_axis_number(axis)
       7718 # https://github.com/python/mypy/issues/7642
       7719 # error: Argument "squeeze" to "DataFrameGroupBy" has incompatible type
       7720 # "Union[bool, NoDefault]"; expected "bool"
    -> 7721 return DataFrameGroupBy(
       7722     obj=self,
       7723     keys=by,
       7724     axis=axis,
       7725     level=level,
       7726     as_index=as_index,
       7727     sort=sort,
       7728     group_keys=group_keys,
       7729     squeeze=squeeze,  # type: ignore[arg-type]
       7730     observed=observed,
       7731     dropna=dropna,
       7732 )


    File ~/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/groupby.py:882, in GroupBy.__init__(self, obj, keys, axis, level, grouper, exclusions, selection, as_index, sort, group_keys, squeeze, observed, mutated, dropna)
        879 if grouper is None:
        880     from pandas.core.groupby.grouper import get_grouper
    --> 882     grouper, exclusions, obj = get_grouper(
        883         obj,
        884         keys,
        885         axis=axis,
        886         level=level,
        887         sort=sort,
        888         observed=observed,
        889         mutated=self.mutated,
        890         dropna=self.dropna,
        891     )
        893 self.obj = obj
        894 self.axis = obj._get_axis_number(axis)


    File ~/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/grouper.py:882, in get_grouper(obj, key, axis, level, sort, observed, mutated, validate, dropna)
        880         in_axis, level, gpr = False, gpr, None
        881     else:
    --> 882         raise KeyError(gpr)
        883 elif isinstance(gpr, Grouper) and gpr.key is not None:
        884     # Add key to exclusions
        885     exclusions.add(gpr.key)


    KeyError: 'Tm'





    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_18_0.png)
    










The most telling finding: when plotting attendance against wins, Oakland consistently falls below the trend line. Even during 90+ win seasons, attendance lagged behind teams with similar records.





    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_21_0.png)
    





    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_22_0.png)
    


The numbers are clear: even during successful seasons, Oakland's attendance ranked among the worst in baseball. When compared to teams with similar win totals, the A's consistently underperformed. The attendance problem wasn't just about losing — it was a deeper issue with the market's support for the team.

*All data sourced from Baseball-Reference.com via pybaseball*





    
![png](/assets/images/2025-5-30-Athletics/2025-5-30-Athletics_24_0.png)
    

