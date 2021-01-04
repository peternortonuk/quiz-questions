count = 100

dates = [
    'Fri 11 Feb 2078 00:05:21 +0400',
    'Mon 29 Dec 2064 03:33:48 -1100',
    'Wed 12 May 2269 23:22:15 -0500',
    'Tue 05 Oct 2269 02:12:07 -0200',
    'Sat 14 Sep 2126 00:36:44 +1400',
    'Wed 22 Jun 2050 23:18:57 -0100',
    'Sat 17 Sep 2107 18:52:42 +0530',
    'Wed 24 Apr 2199 15:00:11 -0900',
    'Sat 24 Aug 2080 00:35:31 +1030',
    'Mon 12 Jan 1998 01:22:02 -0700',
    'Thu 16 Jul 2026 06:28:56 -0930',
    'Sun 20 Apr 2149 00:02:39 -0400',
    'Sat 09 Jun 1979 12:33:03 +0200',
    'Sat 28 Dec 2120 16:55:13 +0500',
    'Thu 19 Sep 2199 10:47:49 +0330',
    'Sun 15 May 2016 02:21:14 +0630',
    'Sun 23 Nov 2110 22:33:19 -1100',
    'Sun 22 Oct 2141 05:14:53 +1100',
    'Tue 03 Mar 2065 08:11:36 -0700',
    'Mon 17 Jan 2163 01:56:54 +0300',
    'Thu 15 Aug 2069 05:42:18 -0930',
    'Fri 03 Aug 2227 17:53:10 -0430',
    'Fri 05 Nov 1999 05:15:31 -0430',
    'Thu 19 Jun 2155 23:27:54 -0600',
    'Wed 24 May 2079 00:19:55 -0500',
    'Wed 15 Aug 2277 09:50:14 -0900',
    'Thu 20 Oct 2140 04:28:27 +0330',
    'Thu 06 Mar 2104 23:00:38 -0430',
    'Sat 25 Mar 2169 04:20:31 +0800',
    'Sun 26 Jun 2107 16:51:54 +0300',
    'Sat 01 Apr 2090 06:40:55 +0900',
    'Sun 28 Jan 2283 11:34:27 +0545',
    'Sat 04 Aug 2238 13:24:34 -0700',
    'Fri 30 Sep 2005 23:39:08 +0300',
    'Thu 09 Jul 2105 02:11:50 +0900',
    'Tue 22 Mar 2146 00:37:27 -0700',
    'Fri 20 Mar 2015 10:10:16 -0500',
    'Mon 03 Feb 2138 23:23:23 +0930',
    'Thu 01 Jan 2105 11:21:13 +0500',
    'Mon 04 Oct 2117 01:49:25 -1100',
    'Tue 19 Jul 2061 17:15:10 -1000',
    'Mon 22 Apr 2250 10:04:43 +1100',
    'Mon 15 Jul 2058 00:43:43 +0400',
    'Sun 03 Aug 2132 11:02:09 +1030',
    'Fri 10 Jan 2138 02:13:59 -0400',
    'Tue 23 Mar 2083 06:59:22 -0300',
    'Sat 03 May 2206 23:02:53 -0430',
    'Thu 30 Aug 2068 03:17:00 -0800',
    'Tue 28 Jul 2246 19:08:25 +1030',
    'Tue 02 Jul 2193 04:39:00 +0000',
    'Fri 15 Feb 2228 15:43:23 +0900',
    'Tue 31 Jul 2018 13:13:28 +0930',
    'Sat 17 Nov 2204 07:53:40 +0800',
    'Sun 12 Nov 1978 13:02:43 -0300',
    'Wed 16 Nov 2157 07:56:31 +0800',
    'Fri 19 Mar 2049 14:18:58 -0430',
    'Sat 26 May 2227 17:18:53 +0100',
    'Tue 19 Nov 2024 13:11:14 +0930',
    'Fri 28 Apr 1972 10:08:34 -0500',
    'Tue 11 Aug 2178 03:34:41 -0900',
    'Sun 30 Jul 2147 14:56:43 +1400',
    'Fri 19 Jul 2171 15:56:03 +1100',
    'Thu 10 Mar 2168 22:15:22 +0000',
    'Mon 30 Jul 2159 07:54:24 +0200',
    'Mon 07 Dec 2257 06:40:47 -0100',
    'Sat 09 Jan 2140 17:18:29 +0500',
    'Tue 22 Sep 2189 18:33:00 +1300',
    'Wed 29 Sep 1971 18:10:00 -1100',
    'Fri 03 Jan 2076 05:17:07 +1000',
    'Sun 17 May 2071 15:51:09 -0600',
    'Fri 29 Nov 2250 05:12:44 +0200',
    'Wed 26 Apr 2248 05:28:52 -0700',
    'Fri 20 Oct 2254 08:16:14 +1030',
    'Sat 01 Jan 2281 17:23:04 +0545',
    'Wed 21 Jun 2243 11:15:57 -0800',
    'Sat 28 Apr 2131 05:15:09 +0630',
    'Wed 07 Sep 2163 21:17:42 -0700',
    'Tue 20 Aug 2171 14:39:48 -0600',
    'Mon 14 Jun 2060 07:07:47 -1200',
    'Wed 31 Mar 1971 15:38:38 +0530',
    'Sat 11 Nov 2062 20:20:09 +1200',
    'Tue 07 Jan 2081 18:42:21 +0430',
    'Sat 03 Apr 2269 09:57:27 -0430',
    'Sat 10 Jan 2201 18:39:13 +0545',
    'Fri 24 Feb 2136 09:48:49 +1100',
    'Tue 21 Mar 2062 10:10:16 +1200',
    'Sat 29 Jun 2137 20:49:04 +0430',
    'Sun 03 Oct 2252 19:34:08 -0200',
    'Fri 04 Jan 2069 10:30:15 -0200',
    'Tue 17 May 2214 01:48:33 +0000',
    'Fri 11 Mar 2016 21:13:54 -0100',
    'Fri 07 Mar 2228 21:01:13 +0300',
    'Tue 12 Apr 2231 15:38:00 +0200',
    'Sun 05 Jan 1992 07:37:10 -0500',
    'Tue 24 Apr 2198 16:14:38 +1300',
    'Tue 27 Feb 2018 10:46:47 -0500',
    'Sat 10 Apr 2280 22:54:22 -0900',
    'Fri 12 Jan 2080 08:56:55 +1000',
    'Fri 17 Nov 2276 15:42:42 +0400',
    'Thu 06 Nov 2070 10:05:08 +0700',
    'Mon 24 Oct 2191 04:55:27 +0300',  #########
    'Mon 12 Jan 2161 03:26:51 -0900',
    'Thu 24 Oct 1996 10:08:51 -0430',
    'Tue 03 Aug 2038 23:15:58 +0800',
    'Tue 31 Oct 2006 01:34:19 +0100',
    'Sat 23 Jun 2007 10:25:51 -1000',
    'Fri 03 Jul 2150 05:56:11 +0600',
    'Sat 29 Dec 2260 15:12:49 +0545',
    'Fri 03 Jul 2065 01:31:24 -0300',
    'Tue 14 Apr 2116 02:09:21 -0700',
    'Mon 25 Jul 2033 15:13:38 +0400',
    'Mon 11 Aug 2087 03:38:34 +1400',
    'Thu 28 Jun 2170 07:23:53 +0900',
    'Sun 29 Apr 2260 02:29:29 +1030',
    'Wed 02 Apr 2053 01:21:28 -0900',
    'Mon 31 Oct 2242 11:27:13 -0900',
    'Fri 29 Sep 2084 02:07:10 -1000',
    'Sun 04 May 2183 11:28:17 -0400',
    'Fri 12 Sep 2014 01:35:03 +0545',
    'Sat 23 Jan 2286 08:03:53 +0600',
    'Fri 28 Apr 2209 08:14:02 +0930',
    'Mon 03 Sep 2204 07:26:04 +0400',
    'Sat 17 Oct 2218 16:20:23 +0630',
    'Fri 10 Jul 2133 06:02:11 -0400',
    'Thu 24 Sep 2178 18:14:35 -0930',
    'Sun 16 Dec 2227 23:03:40 -1100',
    'Fri 20 Mar 1992 19:32:35 +0000',
    'Mon 16 Apr 2181 23:46:22 +1030',
    'Tue 21 May 2097 14:50:40 +0800',
    'Sat 06 Sep 2036 20:31:27 +0545',
    'Mon 20 Sep 2088 16:37:20 -0800',
    'Tue 26 Apr 2112 15:53:34 -0500',
    'Mon 02 Mar 2048 11:39:54 -0800',
    'Sat 06 Jul 2261 06:47:26 +1100',
    'Sat 22 Jan 1977 13:32:22 +1030',
    'Sat 24 Jan 2178 22:37:08 +0330',
    'Tue 12 Jun 2046 11:37:04 -0500',
    'Sat 21 May 2044 14:06:13 +1030',
    'Fri 12 Oct 2063 22:07:36 +1030',
    'Thu 05 Jan 1984 08:58:18 +0300',
    'Wed 18 Feb 2235 01:26:39 +1100',
    'Mon 01 May 2023 19:25:34 -1100',
    'Mon 20 Nov 2276 13:34:20 +0930',
    'Fri 15 Jun 2029 08:03:18 -1000',
    'Sat 31 Jan 2246 04:22:55 +0600',
    'Tue 26 Jul 2033 22:17:49 -0600',
    'Tue 02 Aug 1994 23:34:02 -0100',
    'Thu 12 Nov 2235 06:41:07 +1400',
    'Wed 25 May 2033 03:35:01 +0600',
    'Thu 25 Dec 2110 19:08:36 +0900',
    'Sun 15 Mar 2009 14:05:33 -0400',
    'Fri 13 Jun 1980 21:28:12 +1300',
    'Thu 18 Jun 2009 18:51:53 +1400',
    'Tue 25 Nov 2059 18:30:23 +1000',
    'Tue 18 Feb 2212 02:12:43 -0930',
    'Tue 06 Oct 2268 03:10:40 +0500',
    'Fri 09 Jul 2286 08:53:13 +0930',
    'Mon 26 Feb 2142 01:15:30 +0930',
    'Sun 09 Jan 2022 19:02:40 +1300',
    'Tue 12 Aug 2059 14:07:10 +0800',
    'Sat 08 Jul 2023 08:13:44 -1200',
    'Sun 12 Dec 2010 22:19:32 +0630',
    'Fri 01 Jul 2050 19:10:54 -0100',
    'Thu 10 Apr 2138 14:59:21 -0500',
    'Wed 25 Nov 2189 06:45:13 +0200',
    'Sat 22 Oct 2061 13:20:00 +0530',
    'Fri 22 Mar 1985 22:34:45 +0600',
    'Thu 19 Mar 2172 05:41:08 -0300',
    'Sat 25 Sep 1982 05:50:54 +0930',
    'Sun 21 Apr 2278 04:24:45 -1200',
    'Wed 05 Oct 2050 12:02:14 +0530',
    'Wed 30 Apr 2059 08:09:46 +1400',
    'Mon 09 Oct 2186 20:12:57 +0330',
    'Sat 29 Dec 2255 18:37:49 +0500',
    'Tue 15 Dec 2009 07:01:49 +1300',
    'Sat 14 Apr 2221 02:56:39 -0930',
    'Sun 29 Nov 1987 02:10:57 -0600',
    'Sat 25 Jun 2208 13:57:19 +0530',
    'Tue 26 Nov 2211 22:41:01 +0430',
    'Mon 01 Apr 2052 19:10:40 -0500',
    'Sun 07 Apr 2267 13:06:14 -0100',
    'Wed 22 Nov 2124 11:49:22 +0500',
    'Sun 16 Jun 2216 08:18:21 -0430',
    'Fri 13 Sep 1991 21:59:15 +0200',
    'Tue 17 May 1977 17:24:30 +0430',
    'Tue 08 Jan 2019 13:31:23 +0300',
    'Fri 10 Jul 2144 06:22:53 +0930',
    'Sat 10 Oct 1992 15:42:54 -0400',
    'Mon 21 Jun 2088 09:26:48 +0330',
    'Fri 26 Aug 2146 12:39:37 -0800',
    'Sun 23 Jun 2086 03:58:25 +1100',
    'Tue 24 Oct 2265 19:23:42 +0100',
    'Sat 25 Jun 2078 21:33:09 +0500',
    'Wed 14 Feb 2283 11:48:06 +0600',
    'Mon 29 Dec 2223 04:13:37 +0330',
    'Fri 26 Dec 2036 13:42:38 +1100',
    'Sat 06 Aug 2061 15:39:33 -1000',
    'Thu 20 Nov 2223 05:28:37 -1000',
    'Wed 29 Aug 2029 06:11:15 +0900',
    'Thu 11 Sep 2217 22:45:23 +0630', ]

results = [
    413962293,
    12527392,
    2405413067,
    2890723049,
    2607054209,
    3873960223,
    4467057730,
    5785903595,
    975400894,
    3088568718,
    4984873852,
    4910960543,
    6255495019,
    1155677269,
    1948516117,
    6085008512,
    7347800726,
    1284474337,
    3877627387,
    402560892,
    5956487373,
    2336874506,
    1729368877,
    4344509753,
    1674705565,
    6612548395,
    7132261857,
    3428975253,
    6390707859,
    6509798767,
    756446360,
    271873258,
    3720885738,
    6878823780,
    146093158,
    81787432,
    826897910,
    3539104248,
    250878126,
    2815203549,
    573025932,
    2153093594,
    2332975113,
    3637372504,
    4587110298,
    6689677639,
    7550499650,
    5685074871,
    6319155447,
    6501717454,
    971270916,
    1318293427,
    20375492,
    3486792698,
    1602477477,
    1705458296,
    2834933736,
    5982545145,
    3111276067,
    8563472030,
    146690278,
    2690840892,
    1553408345,
    5966588627,
    1915632253,
    744581774,
    6732374852,
    6343200286,
    65019651,
    2517284358,
    6683673665,
    7808176862,
    6706260306,
    7613885225,
    2448362015,
    907407441,
    1591673910,
    1787135277,
    4555726663,
    1186185870,
    396678252,
    2769896907,
    4042212913,
    5900918783,
    9327384231,
    270301052,
    2184353692,
    6668936690,
    6960557782,
    5038048821,
    4492826212,
    7092636546,
    1314221813,
    4788637799,
    1835966569,
    5659377917,
    6457756497,
    5901285659,
    5121236944,
    5933847848, ]

date_pairs = [(dates[i], dates[i+1]) for i in range(0, len(dates), 2)]
test_cases = zip(date_pairs, results)

"""
    test_case1 = 'Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000', 25200
    test_case2 = 'Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000', 88200
    test_cases = test_case1, test_case2
"""

