---
layout: post
title: "Why The A's Left Oakland"
---


#### An analysis of the attendance issues of the Oakland A's, and whether Oakland is capable of hosting a Major League team.

The Oakland Athletics' departure from the Bay Area has been attributed to low attendance. But was it really that simple? This analysis examines decades of attendance data and team performance to see how the A's compared to the rest of Major League Baseball.





    http://www.baseball-reference.com/teams/OAK/2024-schedule-scores.shtml


    /var/folders/tr/861tz2hd71n7n5t7kb5vpf1h0000gn/T/ipykernel_46892/2228732914.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      OAK_24_home["Year"] = 2024





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Tm</th>
      <th>Opp</th>
      <th>W/L</th>
      <th>R</th>
      <th>RA</th>
      <th>W-L</th>
      <th>Rank</th>
      <th>GB</th>
      <th>Time</th>
      <th>D/N</th>
      <th>Attendance</th>
      <th>cLI</th>
      <th>Streak</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Thursday, Mar 28</td>
      <td>OAK</td>
      <td>CLE</td>
      <td>L</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>0-1</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2:22</td>
      <td>N</td>
      <td>13522.0</td>
      <td>.99</td>
      <td>-1</td>
      <td>2024</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Friday, Mar 29</td>
      <td>OAK</td>
      <td>CLE</td>
      <td>L</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>0-2</td>
      <td>4.0</td>
      <td>1.5</td>
      <td>2:39</td>
      <td>N</td>
      <td>3837.0</td>
      <td>.95</td>
      <td>-2</td>
      <td>2024</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Saturday, Mar 30</td>
      <td>OAK</td>
      <td>CLE</td>
      <td>L</td>
      <td>3.0</td>
      <td>12.0</td>
      <td>0-3</td>
      <td>4.0</td>
      <td>2.5</td>
      <td>3:01</td>
      <td>D</td>
      <td>5425.0</td>
      <td>.87</td>
      <td>-3</td>
      <td>2024</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sunday, Mar 31</td>
      <td>OAK</td>
      <td>CLE</td>
      <td>W-wo</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>1-3</td>
      <td>4.0</td>
      <td>1.5</td>
      <td>2:30</td>
      <td>D</td>
      <td>4118.0</td>
      <td>.82</td>
      <td>1</td>
      <td>2024</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Monday, Apr 1</td>
      <td>OAK</td>
      <td>BOS</td>
      <td>L</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>1-4</td>
      <td>4.0</td>
      <td>2.5</td>
      <td>2:31</td>
      <td>N</td>
      <td>6618.0</td>
      <td>.87</td>
      <td>-1</td>
      <td>2024</td>
    </tr>
  </tbody>
</table>
</div>





    http://www.baseball-reference.com/teams/OAK/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2024-schedule-scores.shtml







<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Tm</th>
      <th>Opp</th>
      <th>Home_Away</th>
      <th>W/L</th>
      <th>R</th>
      <th>RA</th>
      <th>W-L</th>
      <th>Rank</th>
      <th>GB</th>
      <th>D/N</th>
      <th>Attendance</th>
      <th>cLI</th>
      <th>Streak</th>
      <th>Year</th>
      <th>Wins</th>
      <th>Losses</th>
      <th>SeasonWins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Wednesday, Apr 17</td>
      <td>OAK</td>
      <td>BAL</td>
      <td>Home</td>
      <td>L</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>3-3</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>N</td>
      <td>50164.0</td>
      <td>2.24</td>
      <td>-1</td>
      <td>1968</td>
      <td>3</td>
      <td>3</td>
      <td>82</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday, Apr 18</td>
      <td>OAK</td>
      <td>BAL</td>
      <td>Home</td>
      <td>W-wo</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>4-3</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>N</td>
      <td>5304.0</td>
      <td>2.08</td>
      <td>1</td>
      <td>1968</td>
      <td>4</td>
      <td>3</td>
      <td>82</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday, Apr 19</td>
      <td>OAK</td>
      <td>WSA</td>
      <td>Home</td>
      <td>L</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>4-4</td>
      <td>4.0</td>
      <td>2.5</td>
      <td>N</td>
      <td>6251.0</td>
      <td>2.39</td>
      <td>-1</td>
      <td>1968</td>
      <td>4</td>
      <td>4</td>
      <td>82</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Saturday, Apr 20</td>
      <td>OAK</td>
      <td>WSA</td>
      <td>Home</td>
      <td>L</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>4-5</td>
      <td>7.0</td>
      <td>3.5</td>
      <td>D</td>
      <td>16407.0</td>
      <td>2.22</td>
      <td>-2</td>
      <td>1968</td>
      <td>4</td>
      <td>5</td>
      <td>82</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Sunday, Apr 21</td>
      <td>OAK</td>
      <td>WSA</td>
      <td>Home</td>
      <td>L</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>4-6</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>D</td>
      <td>10899.0</td>
      <td>1.95</td>
      <td>-3</td>
      <td>1968</td>
      <td>4</td>
      <td>6</td>
      <td>82</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Saturday, Sep 21</td>
      <td>OAK</td>
      <td>NYY</td>
      <td>Home</td>
      <td>L</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>67-88</td>
      <td>4.0</td>
      <td>18.0</td>
      <td>N</td>
      <td>33198.0</td>
      <td>.00</td>
      <td>-2</td>
      <td>2024</td>
      <td>67</td>
      <td>88</td>
      <td>69</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Sunday, Sep 22</td>
      <td>OAK</td>
      <td>NYY</td>
      <td>Home</td>
      <td>L</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>67-89</td>
      <td>4.0</td>
      <td>18.0</td>
      <td>D</td>
      <td>24663.0</td>
      <td>.00</td>
      <td>-3</td>
      <td>2024</td>
      <td>67</td>
      <td>89</td>
      <td>69</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Tuesday, Sep 24</td>
      <td>OAK</td>
      <td>TEX</td>
      <td>Home</td>
      <td>W-wo</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>68-89</td>
      <td>4.0</td>
      <td>17.5</td>
      <td>N</td>
      <td>30402.0</td>
      <td>.00</td>
      <td>1</td>
      <td>2024</td>
      <td>68</td>
      <td>89</td>
      <td>69</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Wednesday, Sep 25</td>
      <td>OAK</td>
      <td>TEX</td>
      <td>Home</td>
      <td>L</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>68-90</td>
      <td>4.0</td>
      <td>17.5</td>
      <td>N</td>
      <td>35270.0</td>
      <td>.00</td>
      <td>-1</td>
      <td>2024</td>
      <td>68</td>
      <td>90</td>
      <td>69</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Thursday, Sep 26</td>
      <td>OAK</td>
      <td>TEX</td>
      <td>Home</td>
      <td>W</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>69-90</td>
      <td>4.0</td>
      <td>17.0</td>
      <td>D</td>
      <td>46889.0</td>
      <td>.00</td>
      <td>1</td>
      <td>2024</td>
      <td>69</td>
      <td>90</td>
      <td>69</td>
    </tr>
  </tbody>
</table>
<p>4505 rows × 18 columns</p>
</div>








<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Tm</th>
      <th>Year</th>
      <th>Opp</th>
      <th>Date</th>
      <th>Weekday</th>
      <th>D/N</th>
      <th>Wins</th>
      <th>Losses</th>
      <th>Streak</th>
      <th>Rank</th>
      <th>GB</th>
      <th>W/L</th>
      <th>SeasonWins</th>
      <th>R</th>
      <th>RA</th>
      <th>cLI</th>
      <th>Attendance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>OAK</td>
      <td>1968</td>
      <td>BAL</td>
      <td>1968-04-17</td>
      <td>Wednesday</td>
      <td>N</td>
      <td>3</td>
      <td>3</td>
      <td>-1</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>L</td>
      <td>82</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>2.24</td>
      <td>50164.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>OAK</td>
      <td>1968</td>
      <td>BAL</td>
      <td>1968-04-18</td>
      <td>Thursday</td>
      <td>N</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>W</td>
      <td>82</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>2.08</td>
      <td>5304.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>OAK</td>
      <td>1968</td>
      <td>WSA</td>
      <td>1968-04-19</td>
      <td>Friday</td>
      <td>N</td>
      <td>4</td>
      <td>4</td>
      <td>-1</td>
      <td>4.0</td>
      <td>2.5</td>
      <td>L</td>
      <td>82</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>2.39</td>
      <td>6251.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>OAK</td>
      <td>1968</td>
      <td>WSA</td>
      <td>1968-04-20</td>
      <td>Saturday</td>
      <td>D</td>
      <td>4</td>
      <td>5</td>
      <td>-2</td>
      <td>7.0</td>
      <td>3.5</td>
      <td>L</td>
      <td>82</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>2.22</td>
      <td>16407.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>OAK</td>
      <td>1968</td>
      <td>WSA</td>
      <td>1968-04-21</td>
      <td>Sunday</td>
      <td>D</td>
      <td>4</td>
      <td>6</td>
      <td>-3</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>L</td>
      <td>82</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.95</td>
      <td>10899.0</td>
    </tr>
  </tbody>
</table>
</div>








    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_8_0.png)
    





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_9_0.png)
    





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_10_0.png)
    


To understand Oakland's attendance in context, we need to compare it to the rest of the league.





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_12_0.png)
    





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_13_0.png)
    





Even when accounting for league-wide trends, Oakland's attendance consistently ranked among the worst in baseball. Despite competitive seasons, the A's rarely climbed above the bottom tier.




    Failed for ARI in 1968: Season cannot be before first year of a team's existence
    Failed for ARI in 1969: Season cannot be before first year of a team's existence
    Failed for ARI in 1970: Season cannot be before first year of a team's existence
    Failed for ARI in 1971: Season cannot be before first year of a team's existence
    Failed for ARI in 1972: Season cannot be before first year of a team's existence
    Failed for ARI in 1973: Season cannot be before first year of a team's existence
    Failed for ARI in 1974: Season cannot be before first year of a team's existence
    Failed for ARI in 1975: Season cannot be before first year of a team's existence
    Failed for ARI in 1976: Season cannot be before first year of a team's existence
    Failed for ARI in 1977: Season cannot be before first year of a team's existence
    Failed for ARI in 1978: Season cannot be before first year of a team's existence
    Failed for ARI in 1979: Season cannot be before first year of a team's existence
    Failed for ARI in 1980: Season cannot be before first year of a team's existence
    Failed for ARI in 1981: Season cannot be before first year of a team's existence
    Failed for ARI in 1982: Season cannot be before first year of a team's existence
    Failed for ARI in 1983: Season cannot be before first year of a team's existence
    Failed for ARI in 1984: Season cannot be before first year of a team's existence
    Failed for ARI in 1985: Season cannot be before first year of a team's existence
    Failed for ARI in 1986: Season cannot be before first year of a team's existence
    Failed for ARI in 1987: Season cannot be before first year of a team's existence
    Failed for ARI in 1988: Season cannot be before first year of a team's existence
    Failed for ARI in 1989: Season cannot be before first year of a team's existence
    Failed for ARI in 1990: Season cannot be before first year of a team's existence
    Failed for ARI in 1991: Season cannot be before first year of a team's existence
    Failed for ARI in 1992: Season cannot be before first year of a team's existence
    Failed for ARI in 1993: Season cannot be before first year of a team's existence
    Failed for ARI in 1994: Season cannot be before first year of a team's existence
    Failed for ARI in 1995: Season cannot be before first year of a team's existence
    Failed for ARI in 1996: Season cannot be before first year of a team's existence
    Failed for ARI in 1997: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/ARI/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ARI/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/ATL/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BAL/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/BOS/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHC/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CHW/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CIN/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/CLE/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/1968-schedule-scores.shtml
    Failed for COL in 1968: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1969-schedule-scores.shtml
    Failed for COL in 1969: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1970-schedule-scores.shtml
    Failed for COL in 1970: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1971-schedule-scores.shtml
    Failed for COL in 1971: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1972-schedule-scores.shtml
    Failed for COL in 1972: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1973-schedule-scores.shtml
    Failed for COL in 1973: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1974-schedule-scores.shtml
    Failed for COL in 1974: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1975-schedule-scores.shtml
    Failed for COL in 1975: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1976-schedule-scores.shtml
    Failed for COL in 1976: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1977-schedule-scores.shtml
    Failed for COL in 1977: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1978-schedule-scores.shtml
    Failed for COL in 1978: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1979-schedule-scores.shtml
    Failed for COL in 1979: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1980-schedule-scores.shtml
    Failed for COL in 1980: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1981-schedule-scores.shtml
    Failed for COL in 1981: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1982-schedule-scores.shtml
    Failed for COL in 1982: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1983-schedule-scores.shtml
    Failed for COL in 1983: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1984-schedule-scores.shtml
    Failed for COL in 1984: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1985-schedule-scores.shtml
    Failed for COL in 1985: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1986-schedule-scores.shtml
    Failed for COL in 1986: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1987-schedule-scores.shtml
    Failed for COL in 1987: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1988-schedule-scores.shtml
    Failed for COL in 1988: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1989-schedule-scores.shtml
    Failed for COL in 1989: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1990-schedule-scores.shtml
    Failed for COL in 1990: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1991-schedule-scores.shtml
    Failed for COL in 1991: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1992-schedule-scores.shtml
    Failed for COL in 1992: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/COL/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/COL/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/DET/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/HOU/2024-schedule-scores.shtml
    Failed for KCR in 1968: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/KCR/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/KCR/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/1968-schedule-scores.shtml
    Failed for LAA in 1968: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1969-schedule-scores.shtml
    Failed for LAA in 1969: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1970-schedule-scores.shtml
    Failed for LAA in 1970: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1971-schedule-scores.shtml
    Failed for LAA in 1971: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1972-schedule-scores.shtml
    Failed for LAA in 1972: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1973-schedule-scores.shtml
    Failed for LAA in 1973: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1974-schedule-scores.shtml
    Failed for LAA in 1974: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1975-schedule-scores.shtml
    Failed for LAA in 1975: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1976-schedule-scores.shtml
    Failed for LAA in 1976: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1977-schedule-scores.shtml
    Failed for LAA in 1977: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1978-schedule-scores.shtml
    Failed for LAA in 1978: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1979-schedule-scores.shtml
    Failed for LAA in 1979: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1980-schedule-scores.shtml
    Failed for LAA in 1980: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1981-schedule-scores.shtml
    Failed for LAA in 1981: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1982-schedule-scores.shtml
    Failed for LAA in 1982: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1983-schedule-scores.shtml
    Failed for LAA in 1983: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1984-schedule-scores.shtml
    Failed for LAA in 1984: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1985-schedule-scores.shtml
    Failed for LAA in 1985: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1986-schedule-scores.shtml
    Failed for LAA in 1986: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1987-schedule-scores.shtml
    Failed for LAA in 1987: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1988-schedule-scores.shtml
    Failed for LAA in 1988: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1989-schedule-scores.shtml
    Failed for LAA in 1989: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1990-schedule-scores.shtml
    Failed for LAA in 1990: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1991-schedule-scores.shtml
    Failed for LAA in 1991: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1992-schedule-scores.shtml
    Failed for LAA in 1992: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1993-schedule-scores.shtml
    Failed for LAA in 1993: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1994-schedule-scores.shtml
    Failed for LAA in 1994: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1995-schedule-scores.shtml
    Failed for LAA in 1995: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1996-schedule-scores.shtml
    Failed for LAA in 1996: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1997-schedule-scores.shtml
    Failed for LAA in 1997: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1998-schedule-scores.shtml
    Failed for LAA in 1998: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/1999-schedule-scores.shtml
    Failed for LAA in 1999: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/2000-schedule-scores.shtml
    Failed for LAA in 2000: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/2001-schedule-scores.shtml
    Failed for LAA in 2001: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/2002-schedule-scores.shtml
    Failed for LAA in 2002: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/2003-schedule-scores.shtml
    Failed for LAA in 2003: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/2004-schedule-scores.shtml
    Failed for LAA in 2004: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/LAA/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAA/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/LAD/2024-schedule-scores.shtml
    Failed for MIA in 1968: Season cannot be before first year of a team's existence
    Failed for MIA in 1969: Season cannot be before first year of a team's existence
    Failed for MIA in 1970: Season cannot be before first year of a team's existence
    Failed for MIA in 1971: Season cannot be before first year of a team's existence
    Failed for MIA in 1972: Season cannot be before first year of a team's existence
    Failed for MIA in 1973: Season cannot be before first year of a team's existence
    Failed for MIA in 1974: Season cannot be before first year of a team's existence
    Failed for MIA in 1975: Season cannot be before first year of a team's existence
    Failed for MIA in 1976: Season cannot be before first year of a team's existence
    Failed for MIA in 1977: Season cannot be before first year of a team's existence
    Failed for MIA in 1978: Season cannot be before first year of a team's existence
    Failed for MIA in 1979: Season cannot be before first year of a team's existence
    Failed for MIA in 1980: Season cannot be before first year of a team's existence
    Failed for MIA in 1981: Season cannot be before first year of a team's existence
    Failed for MIA in 1982: Season cannot be before first year of a team's existence
    Failed for MIA in 1983: Season cannot be before first year of a team's existence
    Failed for MIA in 1984: Season cannot be before first year of a team's existence
    Failed for MIA in 1985: Season cannot be before first year of a team's existence
    Failed for MIA in 1986: Season cannot be before first year of a team's existence
    Failed for MIA in 1987: Season cannot be before first year of a team's existence
    Failed for MIA in 1988: Season cannot be before first year of a team's existence
    Failed for MIA in 1989: Season cannot be before first year of a team's existence
    Failed for MIA in 1990: Season cannot be before first year of a team's existence
    Failed for MIA in 1991: Season cannot be before first year of a team's existence
    Failed for MIA in 1992: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/MIA/1993-schedule-scores.shtml
    Failed for MIA in 1993: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/1994-schedule-scores.shtml
    Failed for MIA in 1994: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/1995-schedule-scores.shtml
    Failed for MIA in 1995: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/1996-schedule-scores.shtml
    Failed for MIA in 1996: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/1997-schedule-scores.shtml
    Failed for MIA in 1997: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/1998-schedule-scores.shtml
    Failed for MIA in 1998: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/1999-schedule-scores.shtml
    Failed for MIA in 1999: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2000-schedule-scores.shtml
    Failed for MIA in 2000: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2001-schedule-scores.shtml
    Failed for MIA in 2001: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2002-schedule-scores.shtml
    Failed for MIA in 2002: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2003-schedule-scores.shtml
    Failed for MIA in 2003: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2004-schedule-scores.shtml
    Failed for MIA in 2004: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2005-schedule-scores.shtml
    Failed for MIA in 2005: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2006-schedule-scores.shtml
    Failed for MIA in 2006: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2007-schedule-scores.shtml
    Failed for MIA in 2007: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2008-schedule-scores.shtml
    Failed for MIA in 2008: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2009-schedule-scores.shtml
    Failed for MIA in 2009: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2010-schedule-scores.shtml
    Failed for MIA in 2010: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2011-schedule-scores.shtml
    Failed for MIA in 2011: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIA/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIA/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1968-schedule-scores.shtml
    Failed for MIL in 1968: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIL/1969-schedule-scores.shtml
    Failed for MIL in 1969: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/MIL/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIL/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/MIN/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYM/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/NYY/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/OAK/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PHI/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/PIT/2024-schedule-scores.shtml
    Failed for SDP in 1968: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/SDP/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1982-schedule-scores.shtml
    Failed for SDP in 1982: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SDP/1983-schedule-scores.shtml
    Failed for SDP in 1983: HTTPSConnectionPool(host='www.baseball-reference.com', port=443): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SDP/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1992-schedule-scores.shtml
    Failed for SDP in 1992: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SDP/1993-schedule-scores.shtml
    Failed for SDP in 1993: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/SDP/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2006-schedule-scores.shtml
    Failed for SDP in 2006: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SDP/2007-schedule-scores.shtml
    Failed for SDP in 2007: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/SDP/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SDP/2024-schedule-scores.shtml
    Failed for SEA in 1968: Season cannot be before first year of a team's existence
    Failed for SEA in 1969: Season cannot be before first year of a team's existence
    Failed for SEA in 1970: Season cannot be before first year of a team's existence
    Failed for SEA in 1971: Season cannot be before first year of a team's existence
    Failed for SEA in 1972: Season cannot be before first year of a team's existence
    Failed for SEA in 1973: Season cannot be before first year of a team's existence
    Failed for SEA in 1974: Season cannot be before first year of a team's existence
    Failed for SEA in 1975: Season cannot be before first year of a team's existence
    Failed for SEA in 1976: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/SEA/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2003-schedule-scores.shtml
    Failed for SEA in 2003: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SEA/2004-schedule-scores.shtml
    Failed for SEA in 2004: HTTPSConnectionPool(host='www.baseball-reference.com', port=443): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SEA/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2009-schedule-scores.shtml
    Failed for SEA in 2009: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SEA/2010-schedule-scores.shtml
    Failed for SEA in 2010: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/SEA/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2012-schedule-scores.shtml
    Failed for SEA in 2012: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SEA/2013-schedule-scores.shtml
    Failed for SEA in 2013: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/SEA/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SEA/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/1999-schedule-scores.shtml
    Failed for SFG in 1999: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SFG/2000-schedule-scores.shtml
    Failed for SFG in 2000: HTTPSConnectionPool(host='www.baseball-reference.com', port=443): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/SFG/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/SFG/2024-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1968-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1969-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1970-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1971-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1972-schedule-scores.shtml
    Failed for STL in 1972: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/STL/1973-schedule-scores.shtml
    Failed for STL in 1973: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/STL/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/STL/2022-schedule-scores.shtml
    Failed for STL in 2022: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/STL/2023-schedule-scores.shtml
    Failed for STL in 2023: HTTPSConnectionPool(host='www.baseball-reference.com', port=443): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/STL/2024-schedule-scores.shtml
    Failed for TBR in 1968: Season cannot be before first year of a team's existence
    Failed for TBR in 1969: Season cannot be before first year of a team's existence
    Failed for TBR in 1970: Season cannot be before first year of a team's existence
    Failed for TBR in 1971: Season cannot be before first year of a team's existence
    Failed for TBR in 1972: Season cannot be before first year of a team's existence
    Failed for TBR in 1973: Season cannot be before first year of a team's existence
    Failed for TBR in 1974: Season cannot be before first year of a team's existence
    Failed for TBR in 1975: Season cannot be before first year of a team's existence
    Failed for TBR in 1976: Season cannot be before first year of a team's existence
    Failed for TBR in 1977: Season cannot be before first year of a team's existence
    Failed for TBR in 1978: Season cannot be before first year of a team's existence
    Failed for TBR in 1979: Season cannot be before first year of a team's existence
    Failed for TBR in 1980: Season cannot be before first year of a team's existence
    Failed for TBR in 1981: Season cannot be before first year of a team's existence
    Failed for TBR in 1982: Season cannot be before first year of a team's existence
    Failed for TBR in 1983: Season cannot be before first year of a team's existence
    Failed for TBR in 1984: Season cannot be before first year of a team's existence
    Failed for TBR in 1985: Season cannot be before first year of a team's existence
    Failed for TBR in 1986: Season cannot be before first year of a team's existence
    Failed for TBR in 1987: Season cannot be before first year of a team's existence
    Failed for TBR in 1988: Season cannot be before first year of a team's existence
    Failed for TBR in 1989: Season cannot be before first year of a team's existence
    Failed for TBR in 1990: Season cannot be before first year of a team's existence
    Failed for TBR in 1991: Season cannot be before first year of a team's existence
    Failed for TBR in 1992: Season cannot be before first year of a team's existence
    Failed for TBR in 1993: Season cannot be before first year of a team's existence
    Failed for TBR in 1994: Season cannot be before first year of a team's existence
    Failed for TBR in 1995: Season cannot be before first year of a team's existence
    Failed for TBR in 1996: Season cannot be before first year of a team's existence
    Failed for TBR in 1997: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/TBR/1998-schedule-scores.shtml
    Failed for TBR in 1998: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/1999-schedule-scores.shtml
    Failed for TBR in 1999: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2000-schedule-scores.shtml
    Failed for TBR in 2000: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2001-schedule-scores.shtml
    Failed for TBR in 2001: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2002-schedule-scores.shtml
    Failed for TBR in 2002: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2003-schedule-scores.shtml
    Failed for TBR in 2003: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2004-schedule-scores.shtml
    Failed for TBR in 2004: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2005-schedule-scores.shtml
    Failed for TBR in 2005: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2006-schedule-scores.shtml
    Failed for TBR in 2006: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2007-schedule-scores.shtml
    Failed for TBR in 2007: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/TBR/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2012-schedule-scores.shtml
    Failed for TBR in 2012: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/TBR/2013-schedule-scores.shtml
    Failed for TBR in 2013: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/TBR/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2015-schedule-scores.shtml
    Failed for TBR in 2015: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/TBR/2016-schedule-scores.shtml
    Failed for TBR in 2016: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/TBR/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TBR/2024-schedule-scores.shtml
    Failed for TEX in 1968: Season cannot be before first year of a team's existence
    Failed for TEX in 1969: Season cannot be before first year of a team's existence
    Failed for TEX in 1970: Season cannot be before first year of a team's existence
    Failed for TEX in 1971: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/TEX/1972-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1973-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1974-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1975-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1976-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2008-schedule-scores.shtml
    Failed for TEX in 2008: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/TEX/2009-schedule-scores.shtml
    Failed for TEX in 2009: HTTPSConnectionPool(host='www.baseball-reference.com', port=443): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/TEX/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2016-schedule-scores.shtml
    Failed for TEX in 2016: HTTPConnectionPool(host='www.baseball-reference.com', port=80): Read timed out. (read timeout=None)
    http://www.baseball-reference.com/teams/TEX/2017-schedule-scores.shtml
    Failed for TEX in 2017: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
    http://www.baseball-reference.com/teams/TEX/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TEX/2024-schedule-scores.shtml
    Failed for TOR in 1968: Season cannot be before first year of a team's existence
    Failed for TOR in 1969: Season cannot be before first year of a team's existence
    Failed for TOR in 1970: Season cannot be before first year of a team's existence
    Failed for TOR in 1971: Season cannot be before first year of a team's existence
    Failed for TOR in 1972: Season cannot be before first year of a team's existence
    Failed for TOR in 1973: Season cannot be before first year of a team's existence
    Failed for TOR in 1974: Season cannot be before first year of a team's existence
    Failed for TOR in 1975: Season cannot be before first year of a team's existence
    Failed for TOR in 1976: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/TOR/1977-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1978-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1979-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1980-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1981-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1982-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1983-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1984-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1985-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1986-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1987-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1988-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1989-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1990-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1991-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1992-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1993-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1994-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1995-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1996-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1997-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1998-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/1999-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2000-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2001-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2002-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2003-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2004-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/TOR/2024-schedule-scores.shtml
    Failed for WSN in 1968: Season cannot be before first year of a team's existence
    http://www.baseball-reference.com/teams/WSN/1969-schedule-scores.shtml
    Failed for WSN in 1969: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1970-schedule-scores.shtml
    Failed for WSN in 1970: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1971-schedule-scores.shtml
    Failed for WSN in 1971: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1972-schedule-scores.shtml
    Failed for WSN in 1972: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1973-schedule-scores.shtml
    Failed for WSN in 1973: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1974-schedule-scores.shtml
    Failed for WSN in 1974: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1975-schedule-scores.shtml
    Failed for WSN in 1975: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1976-schedule-scores.shtml
    Failed for WSN in 1976: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1977-schedule-scores.shtml
    Failed for WSN in 1977: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1978-schedule-scores.shtml
    Failed for WSN in 1978: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1979-schedule-scores.shtml
    Failed for WSN in 1979: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1980-schedule-scores.shtml
    Failed for WSN in 1980: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1981-schedule-scores.shtml
    Failed for WSN in 1981: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1982-schedule-scores.shtml
    Failed for WSN in 1982: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1983-schedule-scores.shtml
    Failed for WSN in 1983: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1984-schedule-scores.shtml
    Failed for WSN in 1984: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1985-schedule-scores.shtml
    Failed for WSN in 1985: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1986-schedule-scores.shtml
    Failed for WSN in 1986: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1987-schedule-scores.shtml
    Failed for WSN in 1987: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1988-schedule-scores.shtml
    Failed for WSN in 1988: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1989-schedule-scores.shtml
    Failed for WSN in 1989: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1990-schedule-scores.shtml
    Failed for WSN in 1990: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1991-schedule-scores.shtml
    Failed for WSN in 1991: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1992-schedule-scores.shtml
    Failed for WSN in 1992: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1993-schedule-scores.shtml
    Failed for WSN in 1993: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1994-schedule-scores.shtml
    Failed for WSN in 1994: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1995-schedule-scores.shtml
    Failed for WSN in 1995: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1996-schedule-scores.shtml
    Failed for WSN in 1996: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1997-schedule-scores.shtml
    Failed for WSN in 1997: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1998-schedule-scores.shtml
    Failed for WSN in 1998: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/1999-schedule-scores.shtml
    Failed for WSN in 1999: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/2000-schedule-scores.shtml
    Failed for WSN in 2000: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/2001-schedule-scores.shtml
    Failed for WSN in 2001: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/2002-schedule-scores.shtml
    Failed for WSN in 2002: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/2003-schedule-scores.shtml
    Failed for WSN in 2003: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/2004-schedule-scores.shtml
    Failed for WSN in 2004: Data cannot be retrieved for this team/year combo. Please verify that your team abbreviation is accurate and that the team existed during the season you are searching for.
    http://www.baseball-reference.com/teams/WSN/2005-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2006-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2007-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2008-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2009-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2010-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2011-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2012-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2013-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2014-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2015-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2016-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2017-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2018-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2019-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2020-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2021-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2022-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2023-schedule-scores.shtml
    http://www.baseball-reference.com/teams/WSN/2024-schedule-scores.shtml





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Tm</th>
      <th>Year</th>
      <th>Opp</th>
      <th>Date</th>
      <th>Weekday</th>
      <th>D/N</th>
      <th>Wins</th>
      <th>Losses</th>
      <th>Streak</th>
      <th>Rank</th>
      <th>GB</th>
      <th>W/L</th>
      <th>SeasonWins</th>
      <th>R</th>
      <th>RA</th>
      <th>cLI</th>
      <th>Attendance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>113913</th>
      <td>WSN</td>
      <td>2024</td>
      <td>KCR</td>
      <td>2024-09-25</td>
      <td>Wednesday</td>
      <td>N</td>
      <td>69</td>
      <td>89</td>
      <td>-3.0</td>
      <td>4.0</td>
      <td>24.5</td>
      <td>L</td>
      <td>71</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>.00</td>
      <td>16670.0</td>
    </tr>
    <tr>
      <th>113914</th>
      <td>WSN</td>
      <td>2024</td>
      <td>KCR</td>
      <td>2024-09-26</td>
      <td>Thursday</td>
      <td>D</td>
      <td>69</td>
      <td>90</td>
      <td>-4.0</td>
      <td>4.0</td>
      <td>25.0</td>
      <td>L</td>
      <td>71</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>.00</td>
      <td>14357.0</td>
    </tr>
    <tr>
      <th>113915</th>
      <td>WSN</td>
      <td>2024</td>
      <td>PHI</td>
      <td>2024-09-27</td>
      <td>Friday</td>
      <td>N</td>
      <td>70</td>
      <td>90</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>24.0</td>
      <td>W</td>
      <td>71</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>.00</td>
      <td>31796.0</td>
    </tr>
    <tr>
      <th>113916</th>
      <td>WSN</td>
      <td>2024</td>
      <td>PHI</td>
      <td>2024-09-28</td>
      <td>Saturday</td>
      <td>D</td>
      <td>71</td>
      <td>90</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>23.0</td>
      <td>W</td>
      <td>71</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>.00</td>
      <td>38135.0</td>
    </tr>
    <tr>
      <th>113917</th>
      <td>WSN</td>
      <td>2024</td>
      <td>PHI</td>
      <td>2024-09-29</td>
      <td>Sunday</td>
      <td>D</td>
      <td>71</td>
      <td>91</td>
      <td>-1.0</td>
      <td>4.0</td>
      <td>24.0</td>
      <td>L</td>
      <td>71</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>.00</td>
      <td>26729.0</td>
    </tr>
  </tbody>
</table>
</div>






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





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_18_0.png)
    







<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Tm</th>
      <th>Year</th>
      <th>SeasonWins</th>
      <th>Attendance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ARI</td>
      <td>2000</td>
      <td>85</td>
      <td>36324.086420</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ARI</td>
      <td>2001</td>
      <td>92</td>
      <td>33775.567901</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ARI</td>
      <td>2002</td>
      <td>98</td>
      <td>39493.518519</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ARI</td>
      <td>2003</td>
      <td>84</td>
      <td>34636.320988</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ARI</td>
      <td>2004</td>
      <td>51</td>
      <td>31105.679012</td>
    </tr>
  </tbody>
</table>
</div>



The most telling finding: when plotting attendance against wins, Oakland consistently falls below the trend line. Even during 90+ win seasons, attendance lagged behind teams with similar records.





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_21_0.png)
    





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_22_0.png)
    


The numbers are clear: even during successful seasons, Oakland's attendance ranked among the worst in baseball. When compared to teams with similar win totals, the A's consistently underperformed. The attendance problem wasn't just about losing — it was a deeper issue with the market's support for the team.

*All data sourced from Baseball-Reference.com via pybaseball*





    
![png](/assets/images/2025-5-30-Athletics_files/2025-5-30-Athletics_24_0.png)
    

