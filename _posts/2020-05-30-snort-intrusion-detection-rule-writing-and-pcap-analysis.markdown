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

## Lab 1: Security Onion VM Setup

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

Here is the text from the dialog boxes:
    
    Security Onion Setup is now complete!
    
    Setup log can be found here:
    /var/log/nsm/sosetup.log
    
    You may view IDS alerts using Sguil, Squert, or Kibana (if enabled).
    
    Zeek logs can be found in Kibana (if enabled) and the following location:
    /nsm/zeek/
    
    You can check the status of your running services with the sostat utilites:
    
    'sudo sostat' will give you DETAILED information about your service status.
    
    'sudo sostat-quick' will give you a guided tour of the sostat output.
    
    'sudo sostat-redacted' will give you REDACTED information to share with our mailing list if you have questions.
    
    Rules downloaded by Pulledpork are stored in:
    /etc/nsm/rules/downloaded.rules
    
    Local rules can be added to:
    /etc/nsm/rules/local.rules
    
    You can have PulledPork modify the downloaded rules by modifying the files in:
    /etc/nsm/pulledpork/
    
    Rules will be updated every morning.
    
    You can manually update them by running:
    sudo rule-update
    
    Sensors can be tuned by modifying the files in:
    /etc/nsm/NAME-OF-SENSOR/
    
    Please note that the local ufw firewall has been locked down.
    
    It only allows connections to port 22.
    
    If you need to connect over any other port, then run:
    sudo so-allow
    
    If you have any questions or problems, please visit:
    https://securityonion.net
    
    There you'll find the following links:
    FAQ
    Documentation
    Mailing Lists
    IRC channel
    and more!
    
    If you're interested in training, professional services, or hardware appliances, please see:
    
    https://securityonionsolutions.com

### Post-setup

-   Update Security Onion with `sudo soup`. Then reboot.
-   NOTE: Remember that `sudo sostat` can be used for troubleshooting most things in SO (Security Onion).
-   `sudo nsm_sensor_ps-restart` will restart all SO services.
-   Common issue is that Squert doesn't show Snort alerts.
    -   Might be bad custom rules, Sguil service failing, or sniffing interface not processing packets.

### Testing Squert showing Snort alerts

-   Replay a malicious packet using `tcp_replay`:
    -   Run `locate zeus` to find the pcap.
    -   Run `sudo tcpreplay -l 20 -i enp0s8 -t /opt/samples/zeus-sample-1.pcap` to replay the pcap 20 times.
    -   Ignore the error messages.
    -   Double click 'Squert' on the desktop and login.
        You should see alerts indicating ZEUS Trojan activity.
    -   If you don't see these alerts, this is bad and you must troubleshoot.

## Lab 2: Boleto Malware Snort Rule Writing and PCAP analysis

- Go to <http://malware-traffic-analysis.net/> and download the pcap file from the 'YOUR HOLIDAY PRESENT' exercise.

TODO