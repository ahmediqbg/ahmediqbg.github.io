---
layout: post
title:  "Snort Intrusion Detection, Rule Writing, and PCAP Analysis"
date:   2020-05-30
categories: [network, security]
---

## The course

The course this post is based off of is Snort Intrusion Detection, Rule Writing, and PCAP Analysis by Jesse Kurrus.

## Tools

-   OSes
    -   Kali
    -   Windows 7
    -   [Security Onion](https://github.com/Security-Onion-Solutions/security-onion/blob/master/Verify_ISO.md)
-   Snort IDS
-   Squirt


### Snort Resources

-   [Snort Users Manual](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/)
-   [Snort Rule Writing Manual](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node27.html)
-   [Infosec Institute Snort Rule Writing Overview](http://resources.infosecinstitute.com/snort-rules-workshop-part-one/#gref)
-   [Emerging Threats Snort Rules](https://rules.emergingthreats.net/open/snort-2.9.0/rules/)
-   [Snort Community and Blog Network](https://snort.org/community)
-   [Security Onion Google Group](https://groups.google.com/forum/#!forum/security-onion)

## Security Onion VM

Some specific network settings should be used to allow capturing of packets.

![](/static/images/2020-05-30-snort-intrusion-detection-rule-writing-and-pcap-analysis/vm-network-interfaces.PNG)
![](/static/images/2020-05-30-snort-intrusion-detection-rule-writing-and-pcap-analysis/sec-onion-vm-network-settings-1.PNG)
![](/static/images/2020-05-30-snort-intrusion-detection-rule-writing-and-pcap-analysis/sec-onion-vm-network-settings-2.PNG)
