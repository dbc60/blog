---
title: Miscellaneous Notes
date: 2016-03-16
draft: true
categories: notes
tags:
    - jekyll
    - finances
    - retirement
    - business
    - windows
---

The directory structure in your repository and the configuration of Jekyll and Compass are tied closely together.
<!--more-->

## Windows 10 Developer Mode
Developer Mode enables sideload apps, debugging apps, remote debugging, and remote debug discovery. To enable Developer Mode, go to settings, search for `Developer` and choose `Developer Mode` from the list of choices.

## Quick Access to Windows Control Panels
Create a new folder somewhere and name it `Control Panels.{ED7BA470-8E54-465E-825C-99712043E01C}` (use any name you want before the period). It will create a folder that contains links to categorized lists of all Windows control panel applets.

## UPS Backup Power
I have two CyberPower UPS boxes, model number [CST135XLU](https://www.cyberpowersystems.com/products/ups/pc-battery-backup/cst135xlu). One is a backup supply for my NAS computer running FreeNAS and the other is for my desktop, Lorax and Adelle's desktop, Maisie (192.168.1.151).

Connect a browser on Lorax to "http://localhost:3052/agent/system_summary" for current information about how the agent is running.

Note that Lorax has installed the Agent from the CyberPower Business Edition software, and it's also connected via a USB cable to the UPS. On the other hand, Maisie has installed the Client from the CyberPower Business Edition software. The Client communicates with the Agent so both machines get notified of power events.

Note that the Personal Edition of the software has no capability to manage multiple computers from one UPS, so I cannot use it.

My FreeNAS box has CyberPower [CST1300AL](https://www.cyberpowersystems.com/products/ups/pc-battery-backup/cst1300al) UPS connected to it on USB port ugen0.3. It's using the driver called "Cyber Power Systems ups 2 CP1350AVRLCD USB (usbhid-ups)" from the dropdown list. It seems to be working okay (as of March 19, 2016 - after pulling and re-inserting the USB cable). The Monitor User is upsone. I also set the Monitor Password to "powerpanel.encryption.key". I don't know if that was needed, although the initial password of "fixmepass" didn't look right. Regardless, I have peace-of-mind that my server has a functioning UPS.

### CST1300AL Specs
Overview:

- Capacity: 1300 VA / 810 W
- Topology: Line Interactive
- Waveform: Simulated Sine Wave
- Output: 120 VAC ± 5%
- Plug type & cord: NEMA 5-15P, 6 ft. cord
- Outlets: 8 surge-protected (4 surge, 4 surge + battery backup)
- Data line protection: Telephone, Network, Coaxial
- ENERGY STAR® qualified: Yes
- Warranty: 3 year
- Connected Equipment Guarantee: $500,000

Details:

- General
    - UPS Topology	Line Interactive
    - Energy Saving	GreenPower UPS™ Bypass Technology
    - ENERGY STAR® Qualified	Yes
- Input
    - Voltage	90Vac - 140Vac
    - Frequency	60Hz ± 3Hz
    - Plug Type	NEMA 5-15P
    - Cord Length	6'
- Output
    - VA	1,300
    - Watts	810
    - On Battery Voltage	120Vac ± 5%
    - On Battery Frequency	60Hz ± 1%
    - On Battery Waveform	Simulated Sine Wave
    - Outlet Type	NEMA 5-15R
    - Outlets - Total	8
    - Outlets - Battery & Surge Protected	4
    - Outlets - Surge-Only Protected	4
    - Outlets - Widely Spaced	1
    - Overload Protection	Internal circuitry limiting / circuit breaker
- Battery
    - Runtime at Half Load (min)	10
    - Runtime at Full Load (min)	3
    - Battery Type	Sealed Lead-Acid
    - Battery Size	12V/7AH
    - Battery Quantity	2
    - User Replaceable	Yes
    - Typical Recharge Time	8 Hours
- Surge Protection & Filtering
    - Surge Suppression	1,500 Joules
    - Phone Protection RJ11	1-In, 1-Out
    - Coax Protection RG6	1-In, 1-Out
    - EMI/RFI Filtration	Yes
- Management & Communications
    - HID Compliant USB Port	Yes
    - Cable Management	USB Cable
    - LED Indicators
    	- Power On
        - Wiring Fault
    - Audible Alarms
    	- On Battery
        - Low Battery
        - Overload
    - Software	PowerPanel® Personal Edition
- Physical
    - Dimensions - W×H×D (in)	4 × 9.75 × 13.25 inches
    - Weight (lbs)	22.2 lbs
- Environmental
    - Operating Temperature	32 °F to 104 °F / 0 °C to 40 °C
    - Operating Humidity	0% - 80% RH non-condensing
- Certifications
    - Safety
    	- UL1778
        - cUL
        - FCC DOC Class B
    - Environmental	RoHS Compliant
- Warranty
    - Product Warranty	3 Years Limited
    - Connected Equipment Guarantee	Lifetime
    - CEG Amount	$500,000

### CST135XLU Specs
Overview:

- Capacity: 1350 VA / 810 W
- Topology: Line Interactive
- Waveform: Simulated Sine Wave
- Output: 120 VAC ± 5%
- Plug type & cord: NEMA 5-15P, 6 ft. cord
- Outlets: 10 (5 surge, 5 surge + battery backup)
- USB charge ports: 2 (2.1A shared)
- Data line protection: Telephone, Network, Coaxial
- Management software: PowerPanel® Personal Edition
- ENERGY STAR® qualified: Yes
- Warranty: 3 year
- Connected Equipment Guarantee: $500,000

Details:

- General
    - UPS Topology	Line Interactive
    - Energy Saving	GreenPower UPS™ Bypass Technology
    - ENERGY STAR® Qualified	Yes
- Input
    - Voltage	Nominal 120V
    - Frequency	60Hz ± 3Hz
    - Input Voltage Range	90Vac - 142VAC
    - Plug Type	NEMA 5-15P
    - Plug Style	Right Angle, 45 Degree Offset Right
    - Cord Length	6'
- Output
    - VA	1,300
    - Watts	810
    - Automatic Voltage Regulation	Boost 1 +10%
    - On Battery Voltage	120Vac ± 5%
    - On Battery Frequency	60Hz ± 1%
    - On Battery Waveform	Simulated Sine Wave
    - Outlet Type	NEMA 5-15R
    - Outlets - Total	10
    - Outlets - Battery & Surge Protected	5
    - Outlets - Surge-Only Protected	5
    - USB Charge Port - Total	2
    - USB Charging Amperage	2.1A (shared)
    - Rated Power Factor	0.623
    - Overload Protection	Internal circuitry limiting / circuit breaker
    - Transfer Time	4ms
- Battery
    - Runtime at Half Load (min)	10
    - Runtime at Full Load (min)	2
    - Battery Type	Sealed Lead-Acid
    - Battery Size	12V/7AH
    - Hot-Swappable	No
    - Replacement Battery	RB1270X2C
    - Battery Quantity	2
    - User Replaceable	Yes
    - Typical Recharge Time	8 Hours
- Surge Protection & Filtering
    - Surge Suppression	1,500 J
    - Phone RJ11 / Ethernet RJ45	1-In, 1-Out (Combo)
    - Coax Protection RG6	1-In, 1-Out
    - EMI/RFI Filtration	Yes
- Management & Communications
    - Multifunction LCD Panel Displays:
        - Current/Load Level
        - Runtime
        - Battery Level
        - AVR In Use
        - Battery In Use
        - Input Voltage
        - Output Voltage
        - Output Frequency
        - Overload
        - Wiring Fault
        - Silent Mode
    - HID Compliant USB Port	Yes
    - Serial Port	Yes
    - Cable Management	USB Cable
    - LED Indicators
    	- Power On
        - Wiring Fault
    - Audible Alarms
    	- On Battery
        - Low Battery
        - Overload
    - Software	PowerPanel® Personal Edition
- Physical
    - Form Factor	Mini-Tower
    - Dimensions - W x H x D (in)	3.9 x 9.7 x 10.2 inches
    - Weight (lbs)	23.0 lbs
- Environmental
    - Operating Temperature	32 °F to 104 °F / 0 °C to 40 °C
    - Operating Humidity	0% - 90% non-condensing
    - Storage Temperature	5°F to 113°F / -15°C to 45 °C
    - Maximum Operating Elevation	10,000 ft / 3,000 m
    - Maximum Storage Elevation	50,000 ft / 15,000 m
- Certifications
    - Safety
    	- UL1778
    	- cUL 107
    	- FCC DOC Class B
    - Environmental	RoHS Compliant
- Warranty
    - Product Warranty	3 Years Limited
    - Connected Equipment Guarantee	Lifetime
    - CEG Amount	$500,000

## Jekyll and Compass
It's important to tell Jekyll to exclude the Compass configuration file and the bundler Gemfile and Gemfile.lock files. Include the following in your `_config.yml` file:

```
## Exclude these files from your production _site
exclude:      [
                'config.rb',
                'Gemfile',
                'Gemfile.lock',
              ]
```

Configuring Compass is simple. You just need to tell it where the Sass files are and where it should place the resulting .css files. Here's an example configuration file.

```
require 'compass/import-once/activate'
## Require any additional compass plugins here.

## Set this to the root of your project when deployed:
http_path = "/"
css_dir = "css"
sass_dir = "_sass"
images_dir = "img"
javascripts_dir = "js"
```

This is the directory structure that I'm starting with.

```
|-- .git/
|-- .sass-cache/
|-- _drafts/
|-- _includes/
|-- _layouts/
|-- _plugins/
|-- _posts/
|-- _sass/
|-- _site/
|-- css/
|-- fonts/
|-- img/
|-- js/
|-- .gitignore
|-- _config.yml
|-- 404.md
|-- about.md
|-- archive.md
|-- config.rb
|-- css-sampler.md
|-- favicon.ico
|-- feed.xml
|-- Gemfile
|-- Gemfile.lock
|-- humans.txt
|-- index.html
|-- LICENSE.md
|-- NOTES.MD
|-- README.md
|-- robots.txt
```

There is a lot of things to learn to get a blog setup.

- Jekyll configuration
- Organize Jekyll layouts, include files, drafts, posts and static pages.
- Markdown
- YAML
- Liquid templates
- How to structure the HTML layout to make it easy to style
- Write CSS/SCSS to style the HTML
- Compass configuration
- A goot Git workflow
- Bundler to keep the gems up-to-date

I think that should cover the basics. I learned that the pygments highlighter is built in Python, but isn't used in Jekyll 3.0 (rouge is the default highlighter going forward). Once GitHub updates their gem to use Jekyll 3.0, I don't think I'll have to be concerned with Python for this blog. Until then, I might have to become more familiar with it.

## The Pursuit of Happiness Gels in the Imagination
But action needs to be taken in the real world.

I wonder if the reason I have so many non-fiction books waiting to be read is that I'm looking for the thrill of living in a world I'm not willing to create. I have books on game programming, drawing, sketching, animation, project management, organizing, clutter reduction, investing and other topics. Even among those I have read, they don't do me much good unless I act upon them.

The Wondermark comic No. 1204, [The Cargo Cult of Adulthood](http://wondermark.com/c1204/), contrasts buying stuff with buying experiences. The chain of thought starts with buying a movie ticket to get a few hours of being in a dramatized world. Similarly, buying a lottery ticket buys a few days of dreaming there's a chance of becoming a millionaire.

Similarly, buying stuff can transport us into a fun, but imaginary world. Things like workout clothes, cookbooks, and self-help stuff, says David Malki, the author of Wondermark, are the tickets of admission to the fun imaginary worlds of being fit, eating well and having a good life.

So, these things we buy are just fodder for the imagination unless some action is taken in the real world. While I told myself I could be anything I wanted to be, what I really need to do is to make some choices, exclude those things I have no time for or are less interesting to me than others and focus on what I'm good at and those activities and things I find most interesting. Create something new, or clean up something old to make it useful and accessible and then actually put it to use. Those things, and take care of the daily requirements of life - get the mundane chores done, too.

## Quick Test of Footnote-like Presentation

<p>W3C Footnotes in HTML5 <sup><a href="#fn1" id="r1" class="has-footnote">1</a></sup></p>

<section>
    <p id="fn1" class="marginnote">
        <label>
            <a href="#r1">1. </a>
        </label>
        <a href="https://www.w3.org/TR/html5/common-idioms.html#footnotes">
            HTML5 Footnotes
        </a>
    </p>
</section>

## Aspects of Application Development

### General Development
- Using libraries to get stuff done vs. building your own.
- Build Tools and Environments.
- Test Tools and Environments.
- Team Communication (email, IM, voice chat, message boards like Flowdock)
    - [Slack](https://slack.com/is)
    - [Flowdock](https://www.flowdock.com/)
    - [HipChat](https://www.hipchat.com/)
    - Yammer
    - Jira
    - Trello
    - [Quip](https://quip.com/) for documents in the cloud.

### Client/Server Development
- Service Discovery
- Authentication, Authorization and Roles
    - Users.
    - Hosts. The machines should authenticate, so they can be sure they are connecting to real services, and not hosts trying to spoof them and penetrate the network.
- Event Logging and History.
- Deployment.

### Game Development
- Features
    - Ladder Matches
    - Capture the Flag
    - Tournament Games
    - Vehicles
    - Weather
    - Time of Day/Night
    - Team Voice Chat
- 3D/2D/Perspective Display

## Interior Decorating
From http://www.stevenwilliamskitchens.com/10-ways-to-make-your-home-look-elegant-on-a-budget/

1. Crown Molding - Details Matter
    - wide crown molding (plastic, paintable)
    - baseboard
    - high baseboard
    - ceiling beams
    - columns
    - ceiling medallions
    - chair rails
2. Paint - Color Matters
3. Pillows - Comfort & Elegance
4. Window Treatments
5. Hardware Finishes - Opt for Unique
    - drawer pulls
    - knobs
6. Lighting Makes a Difference
7. Hardwood is Preferred over Carpet
8. Accessorize
    - Picture frames
    - Mirrors
    - Tables
9. Furniture
10. Housekeeping - Clean and Uncluttered

## 20 Habbits That May Be Holding You Back From Being a Millionaire
These habbits a cribbed from [this article](https://www.entrepreneur.com/article/284367) in Entrepreneur Magazine.

1. Sleeping-in. It's better to wake-up early to do things like more work, catch-up on the news, respond to emails or exercise without giving up too much family time.
2. Neglecting your health.
3. Not reading. Invest time and effort to expand knowledge, keep up with news and trends in your industry, learn from inspirational biographies and remain relevant.
4. Relying on one source of income. The wealthy have several streams of income. This means [side hustling](https://due.com/blog/side-hustling-101-pick-just-one-get-paid-premium/) to pay-off debt, set aside for your retirement and invest.
5. Not setting a budget. Set one and stick to it. Start cutting unnecessary expenses and speak to an advisor to get back on-track.
6. Spending carelessly. Subsidizing your standard of living with accumulated debt means you will have no money for retirement, for your kids' college, or for pursuing opportunities that present themselves.
7. Not paying attention to small costs. Small costs, such as a $4 cup of coffee every day, or an annual gym membership you never use will add up quickly.
8. Hanging out with the wrong crowd. Replace toxic and negative people in your life with those who are optimistic, driven and supportive. It will help you succeed in life when you surround yourself with people like this.
9. Procrastination. If you want to get out of financial stagnation, then you need to start taking action as soon as possible. Even if it's just sitting down with a financial professional to go over your budget, it's a great place to start.
10. Drinking and gambling. Financial success takes time, initiative and requires relentless effort. Those who gamble are deluded into thinking there is a shortcut to success. Furthermore, excessively driinking alcohol prevents you from achieving millionaire status since it harms your memory, ability to think clearly and your health.
11. Watching too much television. Zig Ziglar once said, “Rich people have small TVs and big libraries, and poor people have small libraries and big TVs.” The rich would rather read, exercise or educate themselves rather than waste time watching TV. "Making productive use of time is a hallmark of self-made millionaires," says Thomas Corley (the author of "Change Your Habits, Change Your Life: Strategies that Transformed 177 Average People into Self-Made Millionaires"). "Wasting time is a hallmark of poor people."
12. Not finding a mentor. [Find a mentor](https://due.com/blog/why-even-introverts-need-mentors/) so you can learn from their successes and mistakes. While you can go out and hire a mentor, they are all around you. It could be the advice from a college professor, your parents or even from Elon Musk by following him on social media or reading his biography.
13. Staying in your comfort zone. The pursuit of wealth requires that you take risks. It's not until you take that leap that you'll find financial success.
14. Not asking questions. Guessing your way through will lead to failure and poor decisions. If you're uncertain about an investment or business idea, don't hesitate to ask for feedback and advice.
15. Being consumed by failure. Failing is awful, but don't let that hold you down. Take those risks, and if you fail, learn from your mistakes and move forward.
16. Not setting daily goals. Write down your daily goals first thing in the morning. Use them for inspiration and to guide you to push yourself each and every day to achieve those goals. It helps to prioritize them by most important to least. For example, instead of chasing down several $100 past due invoices, focus on the one or two $1,500 invoices.
17. Thinking negatively. Long-term success is more likely when you have a positive mental outlook. Some of the [most common negative thoughts](https://due.com/blog/5-mental-preconceptions-keep-excellence/) we have and must overcome are:
    - Self-doubt. Training, education and a mentor can change this.
    - Not believing your goals can be achieved. Focusing on achieving those daiily goals and work your way up.
    - Having poor grades. Grades and learning disabilities don't determine your success. Richard Branson overcame dyslexia, and is a huge success.
    - The competition is too tough. The worst scenario is you have to pivot.
    - No focus. A healthy lifestyle and setting daily goals can keep you focused.
18. Not collecting assets. Assets are things like a profitable business, a growing stock portfolio or investing in the right piece of real estate. Your car and shiny toys are _liabilities_ robbing you of future wealth. Focus on things that will make you money in the long term.
19. Making excuses. It's easy to make excuses when you are trying to understand why you're buried in debt and don't have a six-figure income. Don't worry about saving when you're drowning in debt. Pay off that debt first, then you can start saving and investing. If you don't make enough money, then find another source of income like selling stuff online or delivering pizzas. That won't solve all of your problems, but it's a start in getting rid of those excuses.
20. Not following the 70/30 Rule. Jim Rohn, one of the country's leading authority figures in business, [has a simple formula for accumulating wealth](http://www.success.com/article/rohn-3-money-habits-that-separate-the-rich-from-the-poor). "After you pay your fair share of taxes, learn to live on 70 percent of your after-tax income. These are the necessities and luxuries you spend money on." After that, "it's important to look at how you allocate your remaining 30 percent." He suggests giving a third to charity, a third toward capital investments and the final third should be put in savings. You won't notice anything at first, but after five years or so and the difference becomes pronounced. After ten years, the differences are dramatic.

## Starting a Side Gig
Here are five tips for [starting a side gig](https://due.com/blog/6-tips-for-starting-a-side-gig-while-working-a-job/) while working a "regular" job.

1. Know the rules of starting a side gig while working. It's important to understand expectations related to work and your side gig. If you start a side gig, you need to [do so in an ethical manner](http://plantingmoneyseeds.com/start-a-home-business-on-the-side-with-ethical-moonlighting/). There might be rules in your employment contract against starting a business that could compete with your employer. Don't work on it during company time or use company resources.
2. Know why you're starting a side gig. What are your goals? Your approach to starting your side gig will depend on whether you just want to make a little extra money on the side, or if you want to quit your day job at some point.
3. Set daily goals and tasks for your business. After you know what needs to be done, you need to set daily goals for business activities, whether it's writing one article, crafting one email, or fine-tuning your website. Follow through on the tasks if you want your side gig to be successful.
4. Stay positive. It can be tough to stay positive when you are tired or when you have setbacks. You want to stay positive at your day job, as well as feel positive about your side gig.
5. Prepare your finances. When starting a side gig, you need to think about your finances. You need to have a [plan for your finances](https://due.com/blog/3-financial-realities-to-address-before/) whether you expect to become self-employed or you just want to make enough to fund your travel goals or boost your retirement savings.
