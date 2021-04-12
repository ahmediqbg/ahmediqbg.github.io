---
title: Projects
---

## OSINT Dashboard: "Bowser"

This is a group project that invovled creating a dashboard to gather open-source intelligence.

Our group chose to monitor the imageboard ["4chan"](https://en.wikipedia.org/wiki/4chan) for racism, hate speech, terrorist keywords, and a handful of other categories that may be useful to law enforcement or governments.

- [You can view the GitHub repository for this project by clicking here.](https://github.com/HenryFBP/ITMS448-osint-dashboard-Bowser)
- [You can view a presentation on our project by clicking here.](https://github.com/HenryFBP/ITMS448-osint-dashboard-Bowser/blob/master/ITMS448%20OSINT%20Dashboard%20-%20Bowser%20-%20Final%20Presentation.pdf)

<img src="https://github.com/HenryFBP/ITMS448-osint-dashboard-Bowser/raw/master/.screenshots/screen1.png"/>

<img src="https://github.com/HenryFBP/ITMS448-osint-dashboard-Bowser/raw/master/.screenshots/screen2.png"/>

<img src="https://github.com/HenryFBP/ITMS448-osint-dashboard-Bowser/raw/master/.screenshots/screen3.png"/>

This project was 1 frontend Node.js application that consumed 1 backend Python web API.

My role was backend developer. I helped lead a few junior devs who worked on some data analysis and contributed to the backend.

I was responsible for making most of the Python backend, writing test cases, writing CI/CD, and setting up development/testing workflows for all of the other developers.

I also helped set up data analysis tools for data analysts on my team, and you can [view the tools here](https://github.com/HenryFBP/ITMS448-osint-dashboard-Bowser/tree/master/data-analysis) or view our presentation for some interesting graphs produced by our analysts.

The end result is a powerful tool for searching hundreds or thousands of posts from the imageboard, using text analysis to determine if any posts contain information of interest. Also, anybody can download and try the project out. The documentation is sufficient for anyone to figure out how to self-host and can work on Windows, Linux, and OSX.

## Using Big Data Analytics & Visualization: Improving Preparedness & Responsiveness to Fire Emergencies & Other Disasters

This is an Inter-professional Project (IPRO) that took place at Illinois Institute of Technology that involved creating a suite of tools which aided the American Red Cross of Chicago in detecting, analyzing, and responding to fire-related disasters that people report on Twitter in the Chicago-land area.

The Git repository associated with this IPRO is below.

<https://github.com/HenryFBP/IPRO497-Analytics-Team/>

There is also a package on the Python Package Index (PyPI).

<https://pypi.org/project/twitter-fire-scraper/>

This is a useful Git guide I wrote for my teammates.

<https://github.com/HenryFBP/IPRO497-Analytics-Team/blob/master/Documents/How%20to%20contribute%20to%20this%20project.pdf>

### Whitepaper

[You can read the whitepaper produced for this project by clicking here.](/files/IPRO%20-%20Improving%20Incident%20Response%20of%20the%20American%20Red%20Cross%20in%20the%20Greater%20Chicago%20Area%20by%20Using%20Text%20Classification%20of%20Posts%20From%20Twitter.pdf)

### Awards

We won both Dean's Choice and Best in Track for a total of two awards.

<img src="/images/awards-tfs.jpg" width="1175">

## OPAC Library Reference PC Replacement

During my work at OBPL as a librarian, I was involved with a program to replace about 6 or so computers that were very
old. The only purpose these new computers would serve would be to provide access to a book catalogue website, nothing else.

### Guides

<!-- TODO: FIX overflow on some of the ```code blocks``` in the MD files! -->

-   Backing up and restoring
    [(MD)](/files/opac-documentation/BACKING_UP_AND_RESTORING.txt)
    [(PDF)](/files/opac-documentation/BACKING_UP_AND_RESTORING.pdf)

-   Booting into Linux
    [(MD)](/files/opac-documentation/BOOTING_INTO_LINUX.txt)
    [(PDF)](/files/opac-documentation/BOOTING_INTO_LINUX.pdf)

-   Configuration directories
    [(MD)](/files/opac-documentation/CONFIGURATION_DIRECTORIES.txt)
    [(PDF)](/files/opac-documentation/CONFIGURATION_DIRECTORIES.pdf)

-   Making a new Linux flash drive
    [(MD)](/files/opac-documentation/MAKING_A_NEW_LINUX_FLASH_DRIVE.txt)
    [(PDF)](/files/opac-documentation/MAKING_A_NEW_LINUX_FLASH_DRIVE.pdf)

-   Power user tips
    [(MD)](/files/opac-documentation/POWER_USER_TIPS.txt)
    [(PDF)](/files/opac-documentation/POWER_USER_TIPS.pdf)

-   Whitelisting new domains
    [(MD)](/files/opac-documentation/WHITELISTING_NEW_DOMAINS.txt)
    [(PDF)](/files/opac-documentation/WHITELISTING_NEW_DOMAINS.pdf)


## Arduino Soil Tester
This was a small project undertaken for a club that I went to in Highschool called "Dirt Actualizers." The project consisted of a breadboard, an arduino, 3 wires, and 2 resistors. It was a very simple soil moisture sensor that worked by pulsing AC through its probes and measuring the average of readings. It just has to be calibrated on its lowest (open circuit) and highest (probes touching) bounds, and it's ready to sense moisture!

The software written was just as simple - I repeatedly ran analogRead() on one of the probe ends and ran a switch-case for the value to see how many LEDs to light up. Very easy and small.

## Mathematica ASCII Compression Algorithm

Over the summer, I enrolled in an IIT Mathematica course where I coded an ASCII compression algorithm that took 256 of the most common duplets of characters in an ASCII file and compressed them into a file containing a dictionary followed by compressed data.

## Desktop-in-a-suitcase
This is a project that involved building a portable desktop in a suitcase my freshman semester.

First, three rectangular holes were cut in an aluminum briefcase, one in the lower-left and the other two in the top-middle and top-right.

All of the components were put on multiple custom-designed laser-cut slabs of plastic and screwed onto various locations on the plastic plates.

The power supply was flipped upside-down and placed in the lower-left section of the case, and bolted there.

The graphics card was rotated 90 degrees to the left and three custom mounting plates were constructed for it.

The first two plates sat at the top and bottom of the card, and held it over the motherboard.

The third was to fill space so that the screws on the bottom did not press into the card.

The PCIE-16x cable for the graphics card had to be connected to an extension cable, similar to one for a bitcoin mining rig.

A power supply cable for a screen driver for an LCD panel was soldered to the GROUND and 5V leads of a molex connector attached to the power supply, making the power for the screen self-contained.

A USB header to USB port to wifi dongle supplies wireless, and there is a free-hanging SSD for boot and other files.
