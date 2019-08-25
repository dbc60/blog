---
title: "Effort Estimation"
date: 2019-08-10T08:35:31-04:00
draft: true
math: true
---

Scrum methodologies talk about using story points for estimating effort. That's all well and good, but how do we learn to make better estimates? It seems to me that we need a way to determine actual effort so it can be compared to the estimated effort. Can story points be used to record actual effort as well as estimated effort? If so, how?
<!--more-->

##################
Process Efficiency
##################

Process Efficiency is a relative metric on a scale from 0 - 100% that is used to do absolute comparisons. A 0% efficiency represents products or features that never go into production, where 100% means complete uninterrupted focus from start to end.

Process Efficiency is *Value Added Time / Total Lead Time*.

Two things must be measured by teams to calculate Process Efficiency.

#. The total time the story was in progress. This is the Cycle Time.
#. The total time the team was prohibited from adding value to the story. This is the Interruption Time.

The first metric is Cycle Time. Cycle Time represents the total amount of time spent on realizing the story. Cycle Time is measured in hours, and only working hours count. So, work starting on Friday at 4 PM and ending at Monday at 10 AM has a Cycle Time of 2 hours (assuming a 9 AM to 5 PM working days).

To calculate Cycle Time, teams must track of when they start work on the story and when it's done. Cycle time: The total time the story was in progress, measured in working hours. In other words, Cycle Time = Time Story Marked Done – Time Story Marked In Progress.

The second metric is Interruption Time. Interruption Time represents the sum of all the times that the team got interrupted from adding value to their story. Interruption Time is also measured in hours, and only working hours count, similar to Cycle Time.

To calculate Interruption Time, teams must keep track of when they are interrupted from adding value to the story, write down when that interruption started and write down when they can resume work again. Examples include, but are not limited to:

#. Meetings;
#. Manual Testing;
#. Manual Deployment;
#. Working on something else than the story;
#. Non Team members that prohibit the team from adding value (e.g. security checks).

#########################
Evidence Based Scheduling
#########################

This is a summary from Joel Spolsky's article on `Evidence-Based Scheduling`_ (EBS). His goal is to get at least an estimate of a realistic schedule, but the problem is developers don't like to make schedules. Scheduling is a pain in the butt, and nobody believes the schedule is realistic.

His solution is to gather historical timesheet data, and feed that back into your schedule. The result is a confidence distribution curve indicating a probability that you will ship on any given date.

***************
Break Down Work
***************

Break down your schedule into hours. No tasks should be longer than 16 hours. it forces you to figure out what you're going to do. If you pick tasks that will take days or weeks, you *haven't thought about what you are going to do* **in detail**. Step by step. You can't know how long it will take.

Setting a 16 hour maximum forces you to design the feature. If you don't have a detailed design, you haven't thought about the steps, and you will likely have to take additional, unanticipated action to realize said feature.

******************
Track Elapsed Time
******************

Don't try to account for interruptions, unpredictable bugs, and status meetings. Know one really knows how long it's going to take to do write the necessary code, never mind how much time will be sucked away by all those other non-coding time sinks.

Instead, keep timesheets. Keep track of how long you spend working on each task. That data can be compared against the estimate so you can generate a graph of actual hours vs estimated hours.

Each point on the chart is one completed task, with the estimated and actual times for that task. It's a running total added up as tasks are completed for that sprint and for all sprints over the entire release.

When you divide the estimate :math:`T_E` by the actual time :math:`T_A`, you get *velocity* :math:`V`, how fast the task was completed relative to the estimate. Over time, for each developer, you'll collect a history of velocities.

There are there are three kinds of estimators:

#. The Perfect Estimator who is always right.
#. The Bad Estimator who is all over the map. Given time, these should become more like the Common Estimator.
#. The Common Estimator who gets the scale wrong, but the relative estimates are right.

If there were a *Perfect Estimator*, who always gets every estimate exactly right, the velocity history would be :math:`\left\{1, 1, 1, \dots\right\}`. A *Bad eEstimator* has velocities all over the place, for example :math:`\left\{0.1, 0.5, 1.7, 0.2, 1.2, 0.9, 13.0\right\}`. Given time, these bad estimators will probably become a Common Estimator.

The Common Estimator's estimates are consistent with each other, but probably optimistic. Everything takes longer than expected, because the estimator didn't account for bug fixes, meetings, coffee breaks, and interruptions by anxious product, marketing, and sales executives. This estimator has very consistent velocities, but they are below 1.0. For example, :math:`\left\{0.6, 0.5, 0.6, 0.6, 0.5, 0.6, 0.7, 0.6\right\}`.

As estimators gain more experience, their estimating skill improve. Throw away any velocities older than, say, six months. Remember, each velocity is for tasks that take no longer than 16 hours, so you will have lots of data in any 6 month period.

When you start tracking time, or when you have a new developer with no track record, assume the worst. Give them a fake history with a wide range of velocities, but just for a short period of time. Once they've accumulated a half-dozen or so real data points (about one two-week sprint), throw away the fake history.

*******************
Simulate the Future
*******************

Don't just add up estimates to get a single ship date. Use the Monte Carlo method to simulate many possible futures. The plan is to randomly select a velocity from the developers historical velocities and calculate a probable-actual time for each estimate. That will give us 1 probable future for the completion of those tasks. Repeat this process 100 times and the result is 100 possible completion dates, each with a 1% probability of being true.

Since :math:`V = T_E/T_A`, we can calculate a probable-actual time (:math:`T_P`) by dividing the estimate (:math:`T_E`) by a randomly selected velocity (:math:`V_R`):

.. math::

    T_P = T_E/V_R

Here's one sample future:

+------------------------------------------+------+------+------+------+------+--------+
| Value                                    |  T1  |  T2  |  T3  |  T4  |  T5  | Total  |
+==========================================+======+======+======+======+======+========+
| Estimate (:math:`T_E`)                   |  4   | 8    |  2   | 8    |  16  |        |
+------------------------------------------+------+------+------+------+------+--------+
| Randomly Selected Velocity (:math:`V_R`) |  0.6 | 0.5  |  0.6 | 0.6  |  0.5 |        |
+------------------------------------------+------+------+------+------+------+--------+
| Probable Actual (:math:`T_P=T_E/V_R`)    |  6.7 | 16   |  3.3 | 13.3 |  32  | 71.3   |
+------------------------------------------+------+------+------+------+------+--------+

For our mythical perfect estimator, all velocities are 1. Dividing by 1 has no effect, so all rounds of the simulation give the same ship date, and that ship date has a probability of 100%.

The bad estimator's velocities are all over the map. A velocity of 0.1 is just as likely as 13.0. Each round is going to produce a very different result. The probability distribution curve will be very shallow, showing an equal chance of shipping tomorrow or in the far future. It tells you that you shouldn't have confidence in the predicted shipping dates.

The common estimator has a lot of velocities close to each other. When you divide the estimate by these velocities (all between 0 and 1), you increase the amount of time a task will take. In one iteration, an 8-hour task might take 13 hours; in another it might take 15 hours. That compensates for the estimators perpetual optimism. It compensates precisely, based exactly on the developer's actual, proven, historical optimism. When you run each round of the simulation, you'll get similar results, because all the historical velocities are pretty close. You'll then have a narrow range of ship dates.

In each round of the Monte Carlo simulation, you'll have to convert the hourly data to calendar data, which means taking into account each developer's work schedule, vacations, holidays, etc. You will then have to see, for each round, which developer is finishing last. That is when the whole team is done.

********************
Simple Time Tracking
********************

You don't have to track each interruption. It turns out you can keep the clock running on whatever task you were doing when the interruption occurred. The velocities for each task (:math:`E/A`) will compensate for the interruptions.

*****************************
Actively Manage Your Projects
*****************************

Sort features into different priorities. It will make it easier to see how much it would help the schedule if you could cut the lower priority features. For example, use 7 priority levels:

#. Urgent
#. High
#. Important
#. Medium
#. Moderate
#. Low
#. Don't Fix

If you put the features into a spreadsheet, you should be able to see the ship dates with a given probability (like the 50% ship dates) versus cumulative features by priority. Something like:

+---------------+---------------+
| Priority      | 50% Ship Date |
+===============+===============+
| 1 - Urgent    | 2019.09.09    |
+---------------+---------------+
| 2 - High      | 2019.09.30    |
+---------------+---------------+
| 3 - Important | 2019.10.22    |
+---------------+---------------+
| 4 - Medium    | 2019.11.11    |
+---------------+---------------+
| 5 - Moderate  | 2019.12.10    |
+---------------+---------------+
| 6 - Low       | 2020.01.20    |
+---------------+---------------+
| 7 - Don't Fix | 2020.02.10    |
+---------------+---------------+

*********************
Combating Scope Creep
*********************

There will be times when you add features that weren't planned for ahead of time. Build in some buffer time to the original schedule to allow for:

- New feature ideas
- Responding to the competition
- Integration
- Debugging time
- Adding unit tests
- Usability testing
- Beta tests

If you run out of buffer, your ship dates will start slipping. In that case, take a snapshot of the ship date confidence every night. The x-axis is the date when the calculation was done. The y-axis is the estimated ship date. Plot three estimated ship dates: the 95% probability date, the 50% probability date, and the 5% probability date. The closer the curves are to one another, the narrower the range of possible ship dates.

If you see ship date getting later (rising on the y-axis), it's continuing to slip. If it’s getting later by more than one day per day, you’re adding work faster than you’re completing work, and you’ll never be done.

On the other hand, if the ship date confidence distribution is getting tighter (the curves are converging), you are converging on a date.

****************
Other Guidelines
****************

#. Only the programmer doing the work can create the estimate.
#. Fix bugs as you find them, and charge the time back to the original task. You can't schedule a bug fix in advance. When bugs are found in new code, charging the bug-fix time back to the original task helps EBS predict the time to get *fully debugged* code, not just working code.
#. Don't let managers badger developers into shorter estimates.
#. A schedule is a box of wood blocks. If you have a bunch of wood blocks, and you can’t fit them into a box, you have two choices: get a bigger box, or remove some blocks. If you wanted to ship in six months, but you have twelve months on the schedule, you are either going to have to delay shipping, or find some features to delete.

################################
Estimated vs Actual Story Points
################################

I'd like to apply EBS to story points. I'm not sure what that means in its entirety. At the very least, I think it means we have to decide what the *actual* story points were. Todd Sedano's article, `Estimated vs Actual Story Points`_ provides some guidance on how to do that.

When assigning points to tasks, all developers voted. They went with the majority point value. If there were significant splits in the voting, the team would have a discussion. This results in the *estimated story points* (:math:`T_E`).

I have a couple of concerns with that process. First, is the influence of stronger personalities or senior vs junior developers. Perhaps Planning Poker could be applied here to minimize that influence.

My other concern is that the developer whose going to do the work isn't doing the estimating. We like to assign points during our grooming meeting, when we go through the backlog to make tickets ready for work. We assign tickets to developers during sprint kickoff. Perhaps, the story points should be re-evaluated when the ticket is assigned, but that runs into the problem of the developer being influenced by the initial point value.

Concerns aside, when each task is done, the developer who worked on the ticket needs to assign *actual story points*. How can actual story points be assigned? They are relative - they don't map directly to hours, for example.

I suppose we could adjust the estimated story points up or down depending on the developer's feeling that the task was harder or easier than expected. A 3-point task that turn out to be trivial could be assigned 1 *actual* story point, while a 5-point task that turned out to be more difficult could be assigned 8, 13, or more *actual* story points depending on the *real* difficulty.

Developers could assign actual story points after they've passed QA test. QA could reassign the ticket to the original developer, who assigns actual story points and then sets the status to `Done`.

Does that step need to be done? Each sprint we estimate the number of story points we think we can accomplish (:math:`S_E`). At the end of our sprint, Jira records total points completed (:math:`S_C`). The velocity chart stinks. It just shows those two values. I'd like to see their ratio plotted over time, say :math:`V_A = S_C/S_E`, where :math:`V_A` is the actual velocity:

.. math::

    V_A = S_C / S_E

Now we can simulate the future. We can calculate a probable number of completed story points (:math:`S_P`) for future sprints as the number of estimated story points (:math:`S_E`) timex a velocity randomly selected from the history of velocities (:math:`V_R`):

.. math::

    S_P = S_E \times V_R

Repeat that simulation 100 times, so each result has a 1% chance of being the actual result. We can then get a probability distribution and standard deviation of the likelihood of completing a set amount of work over a number of sprints.

##################
Use Array Formulas
##################

.. note::

  An array formula enables the display of values returned into multiple rows and/or columns and the use of non-array functions with arrays. In other words, whereas a normal formula outputs a single value, an array formula outputs a range of cells.

Imagine we have this dataset, showing the quantity and item cost for four products:

.. table:: Sample Table
    :widths: auto

    ===========  ===== ========= =====
         A         B       C       D
    ===========  ===== ========= =====
    Product       Qty   Cost, $
    Product A       2        10
    Product B       3        15
    Product C       5        25
    Product D       3        12
    ===========  ===== ========= =====

If we want to calculate the total cost of all four products, we could add a formula in column D that multiplies B and C, and then add a sum at the bottom of column D.

Array formulas enable us to skip this step and get the answer all at once. In this case, the formula is: :math:`=\text{ArrayFormula}(\text{SUM}(B2:B5 \times C2:C5))`.

.. note::

  This calculation could also be done with the SUMPRODUCT formula, which takes array values as inputs, multiplies them and adds them together: :math:`=SUMPRODUCT(B2:B5 , C2:C5)`.


#########
Resources
#########

- `Evidence-Based Scheduling`_
- `Estimated vs Actual Story Points`_

.. _evidence-based scheduling: https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/
.. _estimated vs actual story points: http://sedano.org/toddsedano/2015/05/11/estimated-vs-actual-story-points.html

