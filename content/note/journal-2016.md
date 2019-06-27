---
title: 2016 Journal
date: 2016-09-21T06:12:00-04:00
draft: true
categories: note
---

Notes and Thoughts of 2016.

## Thrusday, December 22
I need to put this kind of thing in a function. It's code that keeps trying to get a job done until it gets done. It uses a linear backoff strategy to prevent itself from working too hard and chewing up the CPU or other resources.

```cpp
    while (curlCode_ != CURLE_OK && keep_trying_to_register) {
        LOG(gLogger, warning)
            << "Agent not registered yet. Code: " << curlCode_
            << ". Retrying in " << retry_interval << "ms";
        DWORD event = WaitForSingleObject(connect_sio_interrupt_event_,
                                          retry_interval);
        switch (event) {
        case WAIT_TIMEOUT:
            // retry the connection
            curlCode_ = CurlURLToString(conn, query.c_str(), buffer, errorBuffer);
            if (CURLE_OK == curlCode_) {
                LOG(gLogger, trace) << "Curl buffer: \"" << buffer << "\"";
                mConfiguration->parseServerResponse(buffer);
                if (mConfiguration->isRegistered()) {
                    LOG(gLogger, info) << "Acquired configuration info.";
                    registryWriteConfigurationData();
                } else {
                    LOG(gLogger, error) << "Unable to parse configuration info.";
                    // Need an error code for JSON not being parsable
                    curlCode_ = CURLE_PARTIAL_FILE;
                }
            } else {
                LOG(gLogger, trace) << "Curl Error Buffer: \"" << errorBuffer << "\"";
            }
            if (retry_interval < max_wait_) {
                // lame linear backoff
                retry_interval += min_wait_;
            }
            break;
        case WAIT_OBJECT_0:
            // interrupted. Stop trying to register
            keep_trying_to_register = false;
            LOG(gLogger, info) << "No longer trying to register the agent.";
            break;
        default:
            // something odd occurred
            DWORD last_error = GetLastError();
            keep_trying_to_register = false;
            LOG(gLogger, error)
                << "An unexpected event happened: " << last_error;
            break;
        }
    }
```

That code is in the comms service. I need something similar in the FIM service. Right now, the FIM service is trying to do two different things in one thread. First, it's trying to monitor an `Event` from the comms service that tells it when another policy is available. It attempts to poll the event. If it's not set, it waits for the minifilter to tell it that data is awaiting. That will never happen, because the default rule built into the driver does *nothing*.

What's needed are two separate threads; one to monitor each event. Also, if the FIM service starts before comms, then it will try to open the policy event before comms has created it. This thread will have to have two stages. The first will spin, with some kind of backoff strategy, and try to open the policy event.

Once it succeeds, the thread will move on to the second stage. This stage waits on the event until it is set by the comms service. When it wakes up, it will read and package the new policy and forward the package to the minifilter. Finally, it resets the event and waits for it to be set again.

The second thread just waits for the driver to notify the service of FIM events waiting to be processed. Here too, the thread waits forever on the event (no timeout). This is a pure event-driven design. No polling, which should result in minimal CPU usage.

Both of these threads will need a stop-event, so the service's `stop()` function can wake them. When they wake up due to the stop-event, they will log that fact and terminate.

## Monday, November 14th
I feel inspired by a blogger whose pseudonym is [eevee](https://eev.ee/). He quit his job at Yelp in 2015 and has been living off his own work since then. He does have some advantages in the living-frugally department. He was able to pay off his house using some "old stock", and had a very well-paying job before he left. So, I'm guessing that he was able to sock away a reasonable sum.

What's inspiring is that he's used his free time to write a lot of blog posts (he says 43 in all consisting of over 160,000 words), and do several side projects. He must have a good following, because he earns several hundred dollars a month via [Patreon](https://www.patreon.com/eevee). His side projects include setting up websites for himself, his partner and for some of his projects. I'd like to be able to do that.

He writes a lot of code in Python, from what I can tell, but also dabbles in other languages. I need to learn more languages, but not for the sake of learning them. I need real projects.

There are games I'd like to create, there's a backup tool I need to finish. I need to write the components and keep doing them. Work toward the goal of completing these things. I know C and C++ fairly well. I think I need to start pulling together components to make my projects sing.

One of the killers of a web comic is taking a hiatus. I think the same is true for a blog or any public media. Noone follows my blog, mostly because I haven't said anything there on a regular basis.

## Wednesday, November 9th
I woke up this morning to find that Donald Trump is our president elect. I feel really awful about it. America has become a spectacle.

Our national anthem declares America as "the land of the free and the home of the brave." While we don't always live up to that ideal, it's something we strive for. It's something we are all proud of. Now we've elected as our next president a person who bullies people. He's denigrated those with disabilities. He abuses women. He spreads fear and hate based on race and religion, and wraps it in spectacle. Is that it? It can't be "real" if fear and hate are wrapped in the spectacle of a circus sideshow? Is that how we came to this day?

Life moves on. While Donald Trump is a horrible person, and his accension to the Office of the President of the United States is emminent, I have immediate and personal matters (like family and work) to which I must attend. It still pisses me off that he will be able to pick at least one, and as many as three, Supreme Court justices. His decision(s) will effect the country for decades to come (possibly the rest of my life).

## Monday, November 7th
I read and article on [design principles](https://blog.marvelapp.com/design-principles-reducing-cognitive-load/) for reducing cognitive load. The article is focused on web design, but these principles and a few others seem to apply to other areas of design.

It starts out by listing the properties that cause cognitive load.

1. Too many choices.
1. Too much thought required.
1. Lack of clarity.

These properties also add to cognitive load:

1. Too much information.
1. Multichannel redundancy (for example, reading something to someone as they try to read similar text).
1. Implicit information, that is, forcing people to guess what is being said. It turns a simple thing into a riddle.
1. Lack of consistency. When something is designed in a way that's different from the rest of the "system", one will tend to guess why it's different. When it turns out to be the same as other components, it means users must keep more than one way to do a task in their working memory.

The author lists a few methods for reducing cognitive load.

1. Avoid unnecessary elements (simplicity). THese include excessive colors, imagery, design flourishes (like floating social network icons), or layouts that don't add value. Just don't overvalue this principle at the cost of clarity.
1. Leverage common design patterns. Though he doesn't list any he references his favorite sources at [Design Patterns on CodePen](http://codepen.io/patterns/) and [Blueprint Archives on Codrops](http://tympanus.net/codrops/category/blueprints/)
1. Eliminate unnecessary tasks. Set editable defaults and leverage previously entered information to reduce the effort needed to accomplish the current task. He suggests [anticipatory design](https://www.fastcodesign.com/3045039/the-next-big-thing-in-design-fewer-choices) to take this principle a step further.
1. Minimize choices. It reduces the amount of working memory one needs to use. If working memory is overtaxed with too many choices, it can lead to [decision paralysis](http://uxmyths.com/post/712569752/myth-more-choices-and-features-result-in-higher-satisfac).
1. Display choices as a group. Don't split choices into separage groups nor hide any of the choices so users can figure out what alternatives are available to them. If choices are presented as, for example, a decision tree, then users will never be aware of available alternatives that have been filtered out by previous decisions.
1. Strive for readability. It's not enough to make content legible, it must be [readable](http://alistapart.com/article/how-we-read). This means using typography appropriate for the content and easy to read.

## Friday, October 7th
Installed bash on Windows:

```
C:\Users\Doug>bash
-- Beta feature --
This will install Ubuntu on Windows, distributed by Canonical
and licensed under its terms available here:
https://aka.ms/uowterms

Type "y" to continue: y
Downloading from the Windows Store... 100%
Extracting filesystem, this will take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: doug
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Installation successful!
The environment will start momentarily...
Documentation is available at:  https://aka.ms/wsldocs
doug@CUTHBERTSON:/mnt/c/Users/Doug$
```

Installing git on Ubuntu/bash on Windows:

```
doug@CUTHBERTSON:/mnt/c/Users/Doug/Notes$ git status
The program 'git' is currently not installed. You can install it by typing:
sudo apt-get install git
doug@CUTHBERTSON:/mnt/c/Users/Doug/Notes$ sudo apt-get install git
sudo: unable to resolve host CUTHBERTSON
[sudo] password for doug:
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libfreetype6 os-prober
Use 'apt-get autoremove' to remove them.
The following extra packages will be installed:
  git-man liberror-perl
Suggested packages:
  git-daemon-run git-daemon-sysvinit git-doc git-el git-email git-gui gitk
  gitweb git-arch git-bzr git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  git git-man liberror-perl
0 upgraded, 3 newly installed, 0 to remove and 17 not upgraded.
Need to get 3,306 kB of archives.
After this operation, 21.9 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://archive.ubuntu.com/ubuntu/ trusty/main liberror-perl all 0.17-1.1 [21.1 kB]
Get:2 http://archive.ubuntu.com/ubuntu/ trusty-updates/main git-man all 1:1.9.1-1ubuntu0.3 [699 kB]
Get:3 http://archive.ubuntu.com/ubuntu/ trusty-updates/main git amd64 1:1.9.1-1ubuntu0.3 [2,586 kB]
Fetched 3,306 kB in 4s (769 kB/s)
Selecting previously unselected package liberror-perl.
(Reading database ... 25651 files and directories currently installed.)
Preparing to unpack .../liberror-perl_0.17-1.1_all.deb ...
Unpacking liberror-perl (0.17-1.1) ...
Selecting previously unselected package git-man.
Preparing to unpack .../git-man_1%3a1.9.1-1ubuntu0.3_all.deb ...
Unpacking git-man (1:1.9.1-1ubuntu0.3) ...
Selecting previously unselected package git.
Preparing to unpack .../git_1%3a1.9.1-1ubuntu0.3_amd64.deb ...
Unpacking git (1:1.9.1-1ubuntu0.3) ...
Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
Setting up liberror-perl (0.17-1.1) ...
Setting up git-man (1:1.9.1-1ubuntu0.3) ...
Setting up git (1:1.9.1-1ubuntu0.3) ...
doug@CUTHBERTSON:/mnt/c/Users/Doug/Notes$ git status
On branch master
Your branch is ahead of 'origin/master' by 7 commits.
  (use "git push" to publish your local commits)

nothing to commit, working directory clean
doug@CUTHBERTSON:/mnt/c/Users/Doug/Notes$
```

### Life
I texted my Sister to let her know her toaster oven will arrive via UPS by the end of the day on Monday.

Adelle is planning stuffed zucchini for dinner tonight.

## Wednesday, October 5th
Random notes.

### Music to Lose
Here's a list of songs that I must remove from iTunes and my phone:

- [ ] Siempre Por Siempre by Justo Lamas (Spanish)
- [ ] That's When I'll Stop Loving You, by N'Sync (yuck)
- [ ] Bring Him Home, by Gary Morris (Valjean) (rap?)
- [ ] Este Corazon by RBD (Spanish)
- [ ] One Mic by Nas (rap)
- [ ] Anything by Notorious B.I.G., Linkin Park or Public Enemy (rap)
- [ ] Joseph and the Amazing Technicolor Dreamcoat, and anything by Andrew Loyld Weber. (boring)
- [ ] Hey Sexy Lady, by Shaggy. (rap)
- [ ] Umbrella, by Rhiana (anything by Rhiana) (rap)
- [ ] El Verano Es Lo Mejor, by Justo Lamas (Spanish)
- [ ] I Need Love, by LL Cool J (rap)
- [ ] Aun Hay Algo, by RBD (Spanish)
- [ ] Shut Up, by Black Eyed Peas (rap)

### Quotes
> “Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun. Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.”
> -- Douglas Adams, The Hitchhiker's Guide to the Galaxy.

## Thursday, September 22nd

I stayed up late last night to order a new toaster oven for my sister. It's a Westinghouse ordered from Amazon. It should arrive by Monday, the 26th. I'll get a tracking number once I'm online again.

Today was eventful. Other than the office party at 5pm, I got the HCK tests running. This time, there are 21 separate test that could take as long as 29 hours. That's a lot longer than what I expected. The last time I ran the HCK it had only two tests which took all of 15 minutes to run. I didn't think we added _that_ much to the minifilter, so I'm wondering if I missed something last time and might still be missing something this time.

Coop had a great win today. He figured out how to stop Visual Studio from trying to test-sign the minifilter. Now we can do it in a script and not worry about signing on the build machine. We'll have to work out how to test-sign, so we can continue to make demo/test builds. Production signing can now take place on a separate machine. This is really good progress.

What's left to do?

- [ ] HCK tests and signing. We have to get a Microsoft-signed driver.
- [ ] Event-based gathering of FIM events instead of polling
- [ ] Version management. We somehow have to define some scripts or data files to control the version number.
- [x] I can remove my Jenkins build, since Coop fixed test-signing.
- [ ] We need a way to test-sign packages for, you know, testing...
- [x] Test the lowercase rule ID and verify that it allows alerts.
- [ ] Figure out why my driver builds (or installs) cause `pnputil -e` to report the driver has an unknown driver-class. Is it the OS configuration? A problem with signing (possibly, since the `signed by` field doesn't report anything on the "bad" systems, but reports "unknown" on the "good" systems)? Something else?

## Wednesday, September 21st

Today is my sister Lynn's birthday. She is 58 years old.

I have found that keeping a separate file for daily, weekly and monthly to-do lists consumes a lot of extra time just to move information around. I'm going try going to a running journal. Perhaps I can organize it with sections to keep the days, weeks and months in some kind of order. I'd like to keep single files for goals, plans, projects (or at least a single overview of projects, with separate files for each project), to-do lists, and finally, this journal. Just create one for the whole year.

This journal can be organized in reverse chronological order, so the latest stuff is always at the top. I'm not sure which category or categories this belongs in. It's probably fine to put it in the _notes_ category for now. If I find I need it visible elsewhere, I can add those categores to the YAML front matter.

How shall the to-do list be organized? I could make a single checklist and just keep adding to it as things come up. What if I want to have deadlines (or at least goals for completion dates), or track when they were added, completed and how much time has elapsed? Those goals are beyond what this simple log can do, but my current method helped me to see what still had to be done.

I suppose I could have sections to act as swimlanes in a Kanban board - Backlog, WIP or Current, Waiting For or Blocked By, and Completed. Each task could be annotated with the date it was added to the Backlog. When completed, it could also be annotated with its completion date.

Generally, Kanban items have a priority associated with them, too. Priority 0 means handle immediately. Add another three or four levels to distinguish between what's really imporant and what can be done later, if at all. In fact, there should be a swimlane for adding new items where they will be triaged. After triage, add them to the backlog or directly to WIP if they are a high priority.