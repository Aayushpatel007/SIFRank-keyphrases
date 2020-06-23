# SIFRank-keyphrases
An easy to set up and use  "SIFRank: A New Baseline for Unsupervised Keyphrase Extraction Based on Pre-trained Language Model" using Docker and Flask on GPU as well as CPU.

Original Repository:

https://github.com/sunyilgdx/SIFRank

Usage:

FOR GPU:

```
docker pull aayushpatel007/sifrank-keyphrases

```

For CPU usage:

```
docker pull aayushpatel007/sifrank-keyphrases -1 

```

API:

```
http:\\server_ip:5000\sifrank
POST:
{
'text' : ' ',
'N': 10 , #Number of keyphrases
'Sifrankplus' ,1 # Use SIFRank+ if yes ==1 and no ==01
}
```

```

@article{DBLP:journals/access/SunQZWZ20,
  author    = {Yi Sun and
               Hangping Qiu and
               Yu Zheng and
               Zhongwei Wang and
               Chaoran Zhang},
  title     = {SIFRank: {A} New Baseline for Unsupervised Keyphrase Extraction Based
               on Pre-Trained Language Model},
  journal   = {{IEEE} Access},
  volume    = {8},
  pages     = {10896--10906},
  year      = {2020},
  url       = {https://doi.org/10.1109/ACCESS.2020.2965087},
  doi       = {10.1109/ACCESS.2020.2965087},
  timestamp = {Fri, 07 Feb 2020 12:04:22 +0100},
  biburl    = {https://dblp.org/rec/journals/access/SunQZWZ20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

```
