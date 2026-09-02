---
title: "Sqlite Performance"
date: 2026-09-02T07:56:06-04:00
2026: ["09"]
tags: [sqlite]
# Featured image (optional)
# featuredImage: ""
# featuredImageDescription: "Descriptive alt text for screen readers"
# featuredCopyright: ""
---
This is just a short note about how I learned that SQLite performance can be improved by using the write-ahead log (WAL) instead of the default rollback journal, and one transaction per test suite instead of one per test case. Basically, WAL makes a huge difference. One transaction per test suite instead of one per test case provides an additional improvement, though no where near what WAL does.
<!--more-->

I originally designed Faultline for testing code written in C. Test results are recorded in an SQLite database. My local copy of [the repo](https://github.com/dbc60/faultline) used to be on a SSD, and I hardly noticed how much longer test runs were taking to complete as I added test suites and other code to support C++ code. Sadly, the SSD started failing, so I moved the repo to a HDD and noticed tests were taking significantly longer to complete. I know HDDs are much slower than SSDs, but the additional time per test run seemed out of proportion with the move.

Long story short, I learned that setting the synchronization mode in SQLite to WAL to override the default of using a rollback journal is a huge time saver. Also setting up the results database with one transaction per test suite, instead of one per test case, provides additional improvement.

Faultline currently has 562 test cases spread over 25 test suites. When built with no WAL and one transaction per test case, it took about 21 seconds to run all of the tests and about 53 seconds total time to run the tests and update the results database.

I replaced one transaction per test case with one per test suite and it still took about 21 seconds to run the tests, but the total run time was reduced to about 23 seconds.

Running with WAL only, test time was just over 7 seconds and a little more than 8 seconds total per run. With both WAL and one transaction per test suite, it now takes just under 7 seconds to run the tests and a little less than 8 seconds total run time.

| Configuration                        | Test Time (sec) | Total Time (sec) |
| ------------------------------------ | ---------------:| ----------------:|
| Baseline                             |            21.0 |             53.0 |
| One Transaction per Test Suite       |            21.0 |             23.0 |
| WAL only                             |             7.0 |              8.0 |
| WAL & One Transaction per Test Suite |             6.7 |              7.6 |

While one transaction per test suite saves a significant amount of time updating the database while using the rollback journal, WAL makes a huge difference regardless of whether there's one transaction per test case, or one per test suite.
