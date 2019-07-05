---
title: "Evidence-Based Software Engineering"
date: 2019-07-01T07:39:36-04:00
draft: true
categories: software development
tags: [ebse, spi]
---

> The aim of EBSE is to provide the means by which current best evidence from research can be integrated with practical experience and human values in the decision making process regarding the development and maintenance of software.
>
> --- Kitchenham et al., 2004 [^1]
<!--more-->

The goal of Evidence-Based Software Engineering (EBSE) is to help practioners and software menagers make better decisions about what technologies to employ on their projects. When I first came across references to the paper, Evidence-Based Software Engineering, I was enticed by the prospect of having a process for software developement that provides some reassurance that changes to that process actually improve it. I want to be able to authoritatively back up my decisions with good reasons and strong supporting evidence. What's more reassuring than being able to say "These changes I made are good. Here's the evidence."?

After reading about EBSE, it doesn't seem very different from the overall process of agile software development. It is similar to agile in that changes are monitored, there are periodic reviews not unlike sprints, and a postmortem at the end. The focus of EBSE is more narrow - first gather and evaluate information to create evidence as to whether a proposed change is likely to improve a process or product and then incorporate the new process or technology into current practice.

Also the questions are a little different. At work, at the end of each sprint, we run a retrospective meeting and address the questions:

- What should we start doing?
- What should we stop doing?
- What should we keep doing?

At the end of each product release cycle, we ask the same questions, but within the context of all the work that went into the release.

In EBSE, we are told to periodically run an After Action Review meeting and address the following questions:

- What was supposed to happen?
- What actually happened?
- Why were there differences?
- What did we learn?

At the end of a project, or each major portion of a project, EBSE tells us to run a postmortem analysis and answer these questions:

- What went so well that we want to repeat it?
- What was useful but could have gone better?
- What were the mistakes that we want to avoid for the future?
- What were the reasons for the successes or mistakes and what can we do about it?

What follows is the description of EBSE from Kitchenham et al., 2004 [^1] with a few of my own comments interspersed. I'm not advocating EBSE, I'm merely recording my understanding of it so I can reflect on it and our current practices at work. Maybe there's something here that can help us improve.

## Introduction to EBSE

EBSE is a five step process.

1. Converting a relevant problem or information need into an answerable question.
1. Searching the literature for the best available evidence to answer the question.
1. Critically appraising the evidence for its valiity, impact, and applicability.
1. Integrating the appraised evidence with practical experience and the values and circumstances of the customer to make decisions about practice.
1. Evaluating performance and seeking ways to improve it.

EBSE is not a standalone process. It provides mechanisms to support various parts of Software Process Improvment (SPI) [^2]. SPI involves several different steps:

1. Identifying a problem.
1. Proposing a technology or procedure to address that problem.
1. Evalutating the proposed technology in a pilot project.
1. If the technology is appropriate, adopting and implementing the technology.
1. Monitoring the organization after implmentation of the new technology.
1. Return to step 1.

EBSE is focused on finding and and appraising an appropriate technology for its suitability in a particular situation (SPI steps 2 & 3). This is where SPI is usually weak.

## 1. Asking an Answerable Question

What is the problem? If you're using SPI, you should be monitoring your projects, and so be in a position to identify problems with processes and products. If not, you can rely on the expertise of individuals. The Goal-Question-Metric (GQM) paradigm [^2], in which questions are derived from specific goals, can also be helpful.

I'm unclear about how to specify an answerable question. Kitchenhan says that a well forumlated question has three components (these are taken from the medical field, so they are worded in that context):

- The main intervention or action we are interested in.
- The context or specific situations of interest.
- The main outcomes or effects of interest.

Kitchenham notes that partitioning the question into "intervention", "context", and "effect" makes it easier to go from general problem descriptions to specific questions, and it makes it easier to think about what kind of information is needed to answer the question.

Kitchenham gives an example where the initial problem is in the form of a simple question, "Is pair programming useful?" According to the "shape" of a well formulated question, this question should be specified with more detail. It has the intervention, pair programming, but is missing a context and the desired outcome. If it were changed to "Does the use of pair programming lead to improved code quality when practiced by professional software developers?". Now it has intervention (pair programming), context (professional software developers), and a desired outcome (better code quality).

Kitchenham goes on to say that the question should be even more specific regarding the intervention. The example presumes a comparison with something, but it's not explicitly stated. Any estimation of an effect size involves either a comparison or an association. Here, we could have made it clear that we wanted to compare pair programming with “individual programming”. Alternatively, we could compare it with “partner programming” (i.e. the programmers work on different tasks on different computers, but they share the same physical office or workspace so that they are able to share ideas, thoughts, problems and so forth).

Similarly, the context could have been more specific. It could have included the nature of the software development organization, the skills and experience of the developers, and the software development environment being used.

If this question was asked within a company, I bet that level of detailed would be assumed to be based on the skills and experience of those who would be actually programming, and the development environments already in use. If such an in-house study were published, say, in a blog post, it might not include such detail.

Next, Kitchenham seems to shift context slightly by listing factors to consider (in the context of software engineering) when selecting an answerable question for consideration, as the subject was selecting a quesion from a pool of several questions, instead of creating an answerable question from a problem description.

The factors are:

- Which question is most important to our customers?
- Which question is most relevant to our situation?
- Which question is most interesting in the context of our business strategy?
- Which question is most likely to recur in our practice?
- Is the question possible to answer within the time we have available?

I guess, in the context of software engineering, it is assumed there will be multiple problems that need to be addressed. Getting to the problem that's most important to work on is then a two step process.

1. The first step is to turn each problem an answerable question by defining the three components of a well formulated question: intervention, context, and effect.
1. Second, consider the factors above to choose which question to answer next.

Kitchenham summarizes this section by stating the main challenge is to convert a problem into a question that is specific enough to be answered, but not so precise that we can't find evidence to answer it.

## 2. Find the Best Evidence

Once we have a good quesion to answer, we need to find the best evidence with which we can answer it. There are several sources we can use. For example,

- talk to customers or users of the software.
- ask a colleague or a subject matter expert.
- we can use what we learned in course work, seminars, or other learning environments.
- search for evidence in research-based studies (reports, articles, and other documents).

While all of these sources can be useful, research-based evidence is Kitchenham's main focus. It is difficult because there are thousands of software-related publications. Kitchenham recommends using online electronic databases, and reading a select few publications to have a general overview of the latest developments within software engineering.

Kitchenham's recommened reading list to keep abreast of the latest developments in software engineeing includes:

- Communications of the ACM
- IEEE Computer
- IEEE Software
- IT Professional

The list of searchable databases is:

- [IEEE Xplore](http://ieeexplore.ieee.org)
- [ACM Digital Library](http://www.acm.org/dl)
- [ISI Web of Science](http://isiknowledge.com)
- [EBSCOhost ESJ](http://ejournals.ebsco.com)
- [CiteSeer](http://citeseer.nj.nee.com)

## 3. Critically Appraising the Evidence

The focus here is to evaluate, say, an article, for relevance rather than whether it meets measures of scientific quality or rigor.

Also, in the field of software engineering there are fewer studies conducted with scientific rigor. Thus, we should have a way to evaluate the quality of each study. Kitchenham provides a checklist of factors to consider when evaluating the trustworthiness of a study:

1. Is there any vested interest?
   - Who sponsored the study?
   - Do the researchers have any vested interest in the results?
1. Is the evidence valid?
   - Was the design of the study appropriate to anwer the question?
   - How were the tasks, subjects, and setting selected?
   - What data was collected and what were the methods for collecting the data?
   - Which methods of data analysis were used and were they appropriate?
1. Is the evidence important?
   - What were the results?
   - Are the results credible and, if so, how accurate are they?
   - What conclusions were drawn and are they justified by the results?
   - Are the results of practical significance as well as of statistical significance?
1. Can the evidence be used in practice?
   - Are the findings of the study transferable to other industrial settings?
   - Were all important outcom measures evaluated in the study?
   - Does the study provide guidelines for practice based on the results?
   - Are teh guidelines well described and easy to use?
   - Will the benefits of using the guidelines outweight the costs?
1. Is the evidence in this study consistent with the evidence in other available studies?
   - Are there good reasons for any apparent inconsistencies?
   - Have the reasons for any disagrreements been investigated?

## 4. Applying the Evidence

Here Kitchenham puts up a strawman to assert EBSE needs to be integrated with process improvement by providing the scientific basis for change. The arguement is it is often difficult to integrate evidence into practice. How evidence is applied depends on the specific technology (methods, tools, technique, practice) being evaluated. It may require support from project and senior managers. Even techniques that can be put into practice by individual developers have little impact unless they lead to organizational-wide process change.

The conclusion is EBSI provides the scientific basis for undertaking specific process changes, while SPI manages the process of introducing new technology.

## 5. Evaluating Performance

The final step is to reflect on our personal use of EBSE and confirm that the process change has worked as expected. Oddly, the goal isn't to reflect on how well the new technology has solved the original problem. Rather, it is to consider how well we performed each step in the EBSE process and how we can improve our use of EBSE.

I'm probably misreading the intent of the article, because this sounds like a cult. We don't question the efficacy of EBSE. We assume it _is_ the right process and are told to seek means to further incorporate it into current practices. Maybe there should be a project to first determine if EBSE can or should be incorporated into current practices.

I kind of like that idea. Turn EBSE on itself. Gather evidence that supports or challenges the efficacy of EBSE for various development environments, and give EBSE a whirl.

Kitchenham does refer back to SPI and state we also need to evaluate the effectiveness of the process change. Evaluations, however, should be held during the project and not wait until the end. Periodic meetings, called After Action Reviews, should be held to answer these questions:

- What was supposed to happen?
- What actually happened?
- Why were there differences?
- What did we learn?

Kitchenham cautions us not to over react to a bad result. Don't abandon a new method unless there are strong grounds to believe the bad result is intrinsic to the method itself. Likewise, a good result doesn't mean that further monitoring is unnecessary.

Finally, execute a postmortem analysis when a project, or major part of it, is completed. It is similar to an After Action Review, but is deeper. It aims to capture insights for future projects by answering the following questions:

- What went so well that we want to repeat it?
- What was useful but could have gone better?
- What were the mistakes that we want to avoid for the future?
- What were the reasons for the successes or mistakes and what can we do about it?

The main result from a postmortem analysis is evidence regarding the specific process or technology used. Such evidence might be used to improve guidelines, checklists, development models, and a general understanding of what works and what doesn't work in projects in our own organizations.

[^1]: KITCHENHAM, B.A., DYBÅ, T., AND JØRGENSEN, M. Evidence-based Software Engineering, Proceedings of the 26th International Conference on Software Engineering (ICSE 2004), Edinburgh, Scotland, 23-28 May, 2004.

[^2]: BASILI, V.R. AND CALDIERA, G. Improve Software Quality by Reusing Knowledge and Experience, Sloan Management Review, 37(1):55-64, Fall 1995.
