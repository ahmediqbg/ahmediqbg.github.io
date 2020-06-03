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

### Installation notes

1.  Don't check the box to download updates
2.  Don't download extra drivers/WiFi drivers
3.  Use defaults for partitioning options
4.  Take a snapshot when you log in
5.  Install Guest additions, then `sudo reboot now`.
6.  Run 'Setup' on the desktop.
7.  Choose 'Yes' for 'configure /etc/network/interfaces'.
8.  Choose `enp0s3` for the management interface, because this is the NAT-ed interface.
        
    ![](/static/images/2020-05-30-snort-intrusion-detection-rule-writing-and-pcap-analysis/management-interface-selection.png)
    
    `enp0s8` is the host-only interface, which will only be used for sniffing.
    
9.  Choose DHCP addressing for `enp0s3`.
10. Choose 'Yes' for 'Configure sniffing interfaces'.
11. Your changes should look like this:

    ![](/static/images/2020-05-30-snort-intrusion-detection-rule-writing-and-pcap-analysis/changes-to-network-setup.png)
    
    Click 'Yes' and reboot.

12. After rebooting, run setup again. Skip network config.
13. Select 'Evaluation Mode'.
14. `enp0s8` should be monitored as it is the host-only interface for sniffing.
15. Make a new user, wait for the install to finish, and then some dialog boxes will show up.
    Feel free to read them, they have some useful commands.