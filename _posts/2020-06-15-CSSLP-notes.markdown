---
layout: post
title: "Certified Secure Software Lifecycle Professional (CSSLP) Notes"
date: 2020-06-15
categories: [programming, certification, security]
---

## TOC

* 
This will become a table of contents. Don't touch!  
{:toc}

## Preamble

This is a collection of notes I've taken for the CSSLP. Hopefully they
are useful to you as well!

<https://www.isc2.org/Certifications/CSSLP>

## Secure Software Concepts

### Core Concepts

- Main concept is about restricting user access

#### Confidentiality

- Keep info away from people who don't NEED to know it
- Secret info remains secret

- Must understand what data needs to be kept secret
- In order to do this, data must be classified, e.g.
  - Public
  - Available to everyone
  - Nonpublic
    - Restricted in some way
    - Who can access this data?

```
publicly disclosed? --> no --> disclosed by roles? --> no --> [restricted]
      |                                 |
     yes                               yes
      |                                 |
  [public]                        [confidential]
```

##### Data protection

- Confidentiality Controls
  - _Masking_: Deleting parts of data, i.e. removing first 12 digits of
    credit card
  - Secret writing
    - Covert (hidden among other data)  
      The placement of the data is itself hidden. May also include
      encryption/ciphers.
      - Steganography
      - Digital Watermarking
    - Overt (visible) The data we're protecting is in plain sight, but
      the method of decrypting/deciphering is not known to others.
      - Encryption
      - Hashing (i.e. passwords)

##### Where do we need confidentiality?

- In transit
  - Unprotected Networks
- In processing
  - Data in memory
- In storage
  - Data at rest

#### Integrity

Integrity means the data is protected from any unauthorized change.

Changes must be done by an authorized user. This means we need an
authorization scheme, and a way to determine that data is 'authentic',
to have proof that it was made by

```
minimal/no damage upon change? --> no --> significant damage? --> no --> critical damage
                |                                  |                            |
               yes                                yes                         [high]
                |                                  |
              [low]                            [medium]
```

- Ensure functionality
- Ensure accuracy
- Completeness and consistency (i.e. incomplete update)

##### Input validation

- Users inputting data accidentally
- Many types of accidental or intentional errors
- 'Injection flaw', i.e. SQLi
  - Compromise input of data OR entire system
- Input validation ensures data integrity

##### Parity Bit Checking

- Detects errors or changes made during transit
- An extra bit is added to a piece of data
  - It is `1` if the sum of `1`s in the data is odd, `0` if it's even.
- Fast to calculate, but...
- You can still change data to manipulate the parity check to be
  successful
  - ...all powers of 2 are even (except 2^0), flipping them doesn't
    change the parity.
    - Parity bits are essentially a copy of the last bit AFAICT.

```
0   1   0   0   0   1   1   0  [1] <--- 3 is odd, this parity
                                        bit is 1.
```

##### Cyclic Redundancy Checking (CRC)

- Uses parity bit checking for data integrity
- Good for integrity checking during transmission
- But, CRC can be recalculated and modified

- CRC calc uses 1 bit for polynomial
- Most polynomials are 16/32 bits
- This polynomial is used to calculate a checksum value that is added to
  the data
- More bits = more accuracy = harder to change the data in a way that
  cannot be detected by examining the checksum
- Altering the data results in a mismatch when recalculating the CRC

- CRC are based on cyclic ECC
- CRC =/= hash fn, but very similar in behavior

<https://eklitzke.org/crcs-vs-hash-functions>

##### Hashing

- A hash is a (generally) smaller value derived from performing a
  calculation on a large piece of data
- When putting the large data through a hash fn, the same hash is
  (almost always) going to be returned by the hash function
- `hash(coolio) -> 681`
- When my friend on their computer hashes `coolio`, they also get `681`
- Calculation 'cannot be reversed'
  - ...unless you try every possible input value (brute-force)
  - The ALGORITHM is a ONE-WAY algorithm...hashes CAN BE REVERSED, it's
    just that with strong hashes, this is unfeasible. Try using MD5
    password hashes if a nation-state wants to target you -- They might
    have 10000 GPUs.
- Can ensure confidentiality -- Transmitting a password hash only
  provides the other party _the means to validate a password_, not the
  password itself.
  - This is how NTLM (NT Lan Manager) auth works. Very insecure because
    of OTHER reasons though.
- Many different algos to make hashes
- 'digital fingerprinting'
  - A hash guarantees that the data is intact
  - A digital signature guarantees that the HASH AND DATA were provided
    by a specific entity
  - We know who made it, and that it is intact
  - Example: <http://releases.ubuntu.com/focal/MD5SUMS>
    <http://releases.ubuntu.com/focal/MD5SUMS.gpg>

#### Availability

- Making sure data is available to users
- How valuable is the data?

```
minimal/no impact upon destruction? --> no --> significant impact? --> no --> critical impact
                |                                   |                               |
               yes                                 yes                          [critical]
                |                                   |
            [support]                          [essential]
```

- Low-value data is less critical and is 'more ok' to destroy
- Must ensure no disruption to operation because any interruption could
  make a piece of data unavailable
  - i.e. 'Products' database goes down, and 5,000 stores across America
    depend on that...millions of dollars per minute potentially lost
- Both data and RELATED systems must be protected
  - A breach in any RELATED system could compromise the data

##### Maximum Tolerable Downtime

- Must establish a 'Maximum Tolerable Downtime'
  - MOST systems CAN be down for some amount of time
    - Maybe not nuclear reactors, but bank sites CAN be offline for a
      few hours per day/week.
  - 2 days per week, or '99.9% uptime'
  - Many systems (esp 3rd party) have SLAs (service level agreement)
    that ensures a minimum.

##### Recovery Time Objective

- Must consider RTO when UNPLANNED downtime occurs
- RTO is the maximum amount of time that it takes to recover a system
  from a failure
- This is important when planning SLA lengths
- If we said RTO=1h, and a disaster happened, we should be back up and
  running within 1 hour.

* Targeted duration for recovery
* Explicitly state RTO in SLAs
* Consider this during recovery planning

* Determine the impact of unavailability
  - Can't take orders?
* Measure impact quantitatively and qualitatively
* The way an org uses data will change over time, so both current and
  new data must be considered.

#### Authentication and Authorization 1

- Many ways to authenticate
  - Anonymous
    - Not secure
    - No creds
    - Avoid using this method if you care about securing something
    - Unlinkability
      - You cannot tell WHO performed an action
  - 'Basic'
    - Base64 encoded creds sent over HTTP in every request
    - Basically plaintext creds (encoding is NOT encryption!!!)
      ...so...encrypt your traffic...or don't use this method.
    - Very widely used unfortunately, and common
  - Digest
    - Challenge/response
    - Only password hashes are transmitted
  - Integrated auth
    - Uses challenge-response
    - NTLM auth is integrated with Windows
    - Standalone vs Kerberos v5 auth
  - Client certs
    - Digital Certs
    - Internet/e-commerce
  - Forms
    - Web apps
      - Uname+pw gives the client a auth token to reuse (session token)
    - SSL should be used because uname+pw are transmitted over HTTP.
  - Token-based auth
    - Used with uname+pw
    - Once verified, token is issued
  - Smart Cards
    - Ownership-based auth
    - Creds stored on a microchip
    - Difficult to compromise
      - Needs the password and the smartcard as well
  - Biometrics
    - Unique physical characteristic of user (fingerprints, retina)
    - Can be expensive
    - Suffers from errors (rare though)
      - Type I (False Negative)
      - Type II (False Positive)
    - Detection is complex and errors happen

Forms and basic are different because forms are made by web devs and
basic auth is handled by the webserver software (sent in HTTP headers).

#### Authentication and Authorization 2

Authorization is the act of verifying an entity's permission to perform
an action on an object.

```

subject --- security server ---- permission granted? -- yes --> object access
                                          |
                                         no
                                         |
                                         X
```

- Discretionary Access Control (DAC)
  - Restricts access to object based on identity
  - The task of controlling permissions can be granted to anyone
  - DACs must Maintain an Access Control List (ACL) for the object that
    is getting accessed
    - When someone attempts to access the object, the ACL is checked to
      see if they or one of their groups has permissions to access the
      object.
    - For this to work, the subject (individual) needs to be
      authenticated by a secure server, and their role membership needs
      to be evaluated
      - That then needs to be compared to the ACL to see if they have
        access

* Nondiscretionary Access Control (NDAC)

  - Also controls authorization
  - NDAC is different from DAC because of who can manage the permissions
    - Only the admin or a small mgmt body can control permissions to an
      object
      - This control is systemwide and imposed on many subjects and
        objects
    - Can be installed on many OSes or configured in existing DAC
  - Offers a high degree of protection, but it restricts autonomy and
    involves a lot more administration

* Mandatory Access Control (MAC)

  - Is a form of NDAC
  - Restricts access based on information sensitivity
  - Privileges and formal authorization are still required to access
    objects
  - A single admin body is required to control access as MAC is born
    from NDAC
    - This body provides priviledge and authorization
  - Access is 'multilevel' as information sensitivity is different per
    classification
    - Top Secret data can be viewed by one group, Classified can be
      viewed by another.
  - Information must be PROPERLY CLASSIFIED in order for MAC to be
    useful as an Access Control scheme
  - A common implementation of this is to use Rules to assign the right
    data to the right classifications

* Role-based Access Controls (RBAC)
  - Focus on the job role/function that a person is in to be able to
    assign permissions to objects
  - The role a person is placed in will determine how much trust you are
    giving them
    - i.e. `User 5 -> Store Manager Role` will grant User 5 all the
      permissions that the `Store Manager Role` has
  - Users -or- services can be given Roles
  - Underlying access is granted based on Roles
    - RBAC works with the other AC models and simplifies management
  - This model (RBAC) can work with DAC, NDAC, and MAC

#### Accounting (Auditing)

- Measure activity that happens on a system
  - Who changed what, who accessed what
  - Keep historical access records
  - Records can be used to detect anomalies
  - Records can assist us if we have problems

##### Logging

Audit logs must be stored, and enough resources must be allocated to
create, store, and review logs.

- Resources
  - Create
  - Store
  - View

- Log files alone do not create security
- All critical transactions should be logged

###### Logging requirements

- Who is performing the action
- What action is being performed
- Where is this action being performed
- When was the action performed

#### Non-repudiation

Non-repudiation is being able to prove that a person IS THE ENTITY that
performed an action.

i.e. It is impossible for them to 'repudiate' (deny) that they 'took a  
cookie from jar 28 at 9am on Monday'

If a change happens in an information system, we need to be able to  
apply corrective action to the right person!

- Audit logs must capture enough data (who, where, when, what)

##### Identification

The identification mechanism (aka auth mech) needs to be accurate so  
that someone can't impersonate another user and circumvent  
non-repudiation.

Uname+pw CAN BE IMPERSONATED if someone gets the password of another  
user... All we 'know' at that point is that SOMEONE who knows
`steveba:p@$$w0rd!` logged in at 1am on Friday, not necessarily Steve
Ballmer.

Adding something like a retina scanner requires you to physically be in
possession of the eyeball to authenticate, so you'd need Steve's eye to
log in, which may be harder than getting his credentials.

The easier it is for someone to bypass an authentication mechanism, the
easier it is for the OWNER of a potentially compromised account to
REPUDIATE (deny) any action performed using their account.

"Hey, it wasn't me! My login got stolen"!

versus

"Hey, it wasn't me! My eyeball got stolen"!

- After logon, audit logs must record what actions are performed by who
- Identification of the user will only be as good as the auth system we
  are using

##### Requirements

- Accounting requires a lot of extra space and resources
- Consider security requirements carefully instead of logging to the
  finest level by default
  - Security Requirements
    - Subjects
    - Objects
    - Events
- Complete non-repudiation needs:
  - Logging all actions, subjects, etc
  - LARGE amount of data
  - Likely unnecessary
    - Should focus on critical data

There may be OTHER EVENTS that you need to log in order to protect
critical data -- Things that are not directly related to critical data.

An example of this is somebody who creates a new user and adds them to a
new security group, which could allow a nonpriviledged user to gain
access to critical data by using a different account.

All changes to security groups and users should be logged, as well as
access to data.

### Security Design Principles

These are key components to maximize software security against  
disruption and attacks.

#### Least Privilege

- Fundamental approach
- Minimal access rights
  - Minimum amount of time
- Useful for administering a system
- Limits harm if something is compromised

This is a fundamental approach to security.

Essentially, grant the MINIMUM amount of privileges to accomplish a task.
No more is given.

For a person, this means they get the absolute minimum perms and time to do a task.

Example: An admin's only job is to take and maintain backups. They should be able to back up the 
system, and nothing more.

Least Privilege is a good technique because it minimizes the potential for harm if a person,
credential, system, or anything else were to be compromised.

Often times, data loss is actually due to user error, not malicious intent. LP minimizes this.

##### Need to Know

- Military sec rule
- Limits disclosure of info
- Increased confidentialiy
- Mitigates Risk

Least Priviledge also means that disclosure of data is only given to people
who NEED ACCESS to the data.

This is a basic military security rule and it helps to limit the spread of critical info.

- Who NEEDS to work with this data?
  - versus 'who is ENTITLED to this data', which spreads more info than necessary

This increases confidentiality of the data, which mitigates risk, as LESS PEOPLE 
have access to the data.

##### Modular programming

- Software design technique
- Software is broken into submodules
- Every module has ONE job/operation

Software design can benefit from Least Privilege.

Modular programming breaks a program down into submodules.

Each module can have some least privilege applied to it.

Software becomes easier to:
- Read
- Reuse
- Maintain
- Troubleshoot

##### Non-admin accounts

Using nonadmin accounts, we can implement least privilege.

- Minimal set of rights
- Avoid a 'sysadmin' account existing (root, SA, admin, etc)
- Reduces risk

#### Separation of Duties

SoD means we NEED more than 1 person to complete a task.

- No single 1 person can fully abuse a system
- <https://en.wikipedia.org/wiki/Two-man_rule>
- Never give 1 person full control over a system
- Important in critical business areas
- Checks and balances

##### Software

- Common in software components
  - Ensure system checks and balances are performed
- Multiple conditions must be met before an operation can complete
  - i.e.
    - Does the user have permissions to invoke an operation?
    - (if the software is modular) Is the model requesting the operation allow to make that request?
    - Are the correct security protocols, like encrypted comms, in place?
- SoD in Software says that these checks and balances must be completed by different parts or modules
  within software, so each component is fully responsible for its own task
  - Each module has 1 job and must do it well, which minimizes risk to other components
- Code must be reviewed and tested to ensure each module performs properly
  - The code author MUST NOT review their own code. 
    This could allow them to insert malware into their code easily.
    - A different set of eyes will reduce bias and mistakes introduced by 1 person.

#### Defense in Depth

- One of the oldest security principles.
- Layering security controls to provide multiple defenses
- One single vulnerability will not result in a compromise
- Strong external network and a weak internal network...bad!
  - One hapless employee with a virus on their laptop can defeat the strong external defenses.
- Not just 1 strong firewall will protect you.
- Layers should be DIFFERENT.

##### Diversity

- Security layers should be heterogenous
- Mix protection
  - i.e. Input validation AND stored procs
- Wider range of security
- Deterrent and mitigation of risks
  - Effort to breach a system is a great way to make it a PITA to penetrate

#### Fail-Safe, aka Fail-Secure

- Systems should fail to a 'safe state'
  - A state that will not allow it to be compromised (at all, or further)
    - Don't do a memory dump!
    - Reboot > Login as Admin
  - Vehicle crash detection
    - Door unlocked
    - Engine stopped
  - Suppose a user attempts to log into a system
    - Bad password:
      - Error says "Login Failed" and not "Bad Password"
      <!-- - **It's Just Good InfoSec Bro &tm;**  -->
      - "Login Failed" is nondescript, IDK if the uname or pw is invalid.


- Rapid recovery upon failure
  - Failover server/module
    - i.e. <https://success.docker.com/article/dr-failover-strategy>
- Resiliency
  - Confidentiality
  - Integrity
  - Availability

- Fail-safe is part of the SD^3 initiative
  - Secure by design
  - Secure by deployment
  - Secure by default
    - \*Should be secured during every point in deployment
    - \*No default passwords
    - \*No extra default features

#### Economy of Mechanism

EoM is a phrase used when trying to implement functionality while keeping the implementation as simple as possible, but still trying to maintain the functionality.

- Usability vs Security
  - Generally opposing forces within an org or software system
  - Add a lock to a door on a room
    - Now everyone who needs access has extra steps
    - Takes time to lock/unlock the door
    - Admin duties now exist regarding assigning keys or changing the lock
    - Applying EoM to this example will have us use RFID cards instead of keys as they are
      easier to manage and are more convenient for users.
        - We still have the desired effect but the IMPLEMENTATION is different

Sometimes, more features are crappy hacks built on existing systems. This creates a more complex system that could hide security holes.

- Avoid unnecessary complexity
- KIS,S
- Operational ease of use with simplicity
- Fewer inconsistency

##### Requirements Traceability Matrix

EoM can be hard to understand and harder to implement.

A RTM can help you understand it.

- Generated during the requirements gathering phase of a project
- RTM is a document that tracks the requirements of software and
  matches it to the implementation components
  - This lets us compare what is being created and how it covers the requirements of the project
  - We can use this during the development phase to track and manage software functionality
  - Prevents inclusion of unnecessary functionality

Example: <http://doliquid.com/wp-content/uploads/2017/12/requirements-traceability-matrix-template-best-business-template-regarding-requirements-traceability-matrix-template.png>

#### Complete Mediation

- Access requests must be verified EVERY TIME someone accesses a system
  - Lots of systems actually don't do this

1.  Log into website
2.  Do something
3.  Must log in again
  1.  Each request is A&A (authenticated and authorized) individually
4.  This is a Gigantic PITA Bread

More practical approach is to use a Smart Card for authentication

- User needs to keep card inserted, not type `P@%$$w0rd` 2315 times.
- Authorization is NEVER circumvented
- Verify every single request
- This model enforces systemwide access control
  - When a user authenticates, the same authentication happens to the same 
    user account at each stage of the process
    - This means each component needs to use the same authentication mechanism.

This greatly reduces the possibility of a system exploit as any exploit would be forced to re-auth.

##### Caching

- Using CM is not common
  - jsessionid, anyone?


- Caching greatly speeds up software
  - Increase to security risk
    - Auth bypass
    - juicy session token gets stolen (session hijack)
    - MiTM
    - Replay attack
- The longer creds are cached, the greater this window of opportunity is.

#### Open Design

...AKA 

"security through obscurity S.U.C.K.S. and your crappy custom XOR 'encryption' protocol is a pile of duct tape and cardboard and would be torn to shreds by any hacker who found out it was being used"

Open design is the act of making a system and publicly releasing the source code.

- Depending on the secrecy of your design is a bad idea
  - Enables backdoors, poor testing, and shallow defenses

This enforces the idea that implementation details should be independent of design

- Looking at you, hardcoded password/server name/connection string/IP address
  - These would not be included in the design, and thus the shared source code

This permits craploads of people to review the software. And because there are no embedded passwords/ips/etc, the act of reviewing the software will not compromise any defenses.
- Public bug issues
  - Faster resolution
  - HOWEVER, public bugs become PUBLIC KNOWLEDGE immediately
    - 0days :3

Because of the bug problem, OD is not a universally accepted practice.

##### OD Crypto

Crypto is one of the best examples of OD in practice.

Crypto is Math that cannot have ANY flaws or it will crumble.

There are loads of crypto algs, some have been blown to bits (i.e. DES's keys are too short) but others are good (i.e. AES)

<https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle>

"A cryptosystem must be secure even if everything about the system except the key is known."

or,

"Assume the enemy knows the system".

This is an antithesis to "'security' through obscurity", which has been proven to breed awful \(in\)security.

Example: OD was NOT applied to the Content Scramble System to encode DVDs in the 90s.

<https://www.cs.cmu.edu/~dst/DeCSS/Kesden/>

They relied on a SECRET ALGO that was exploited because it was weak.

##### Moral

Do not rely on the mechanisms that you deploy to be secret.

Secrecy does NOT bring security.

Public scrutiny fixes issues faster than without.

#### Least Common Mechanism

Restricting multiple users from sharing the same "mechanism", i.e. a common component in a system.

If 2 users both access the same app on the same server, then the 2 users have multiple mechanisms in common like:

- Web server
- Application
- Network comms

This means one user can accidentally or maliciously access the private data of the other user.

LCM (Least Common Mechanism) refers to separating these environments as much as practically possible to separate data and controls.

- Sharing opens channels to transmit information
- To implement LCM principle, common mechanisms must not be shared
- Mechanisms that must be separated:
  - More than 1 user or process
  - Different levels of privilege

Example:

1 normal user, 1 manager user.

If we add mgmt functionality to an app that both users use, then the normal user might gain mgmt functions.

If we apply the PoLCM (principle of LCM), then we might want to make 2 different applications.

Session hijacking highlights why the PoLCM is important: It would mitigate it greatly.

- Web server is shared
- Network is shared
- Hundreds of users pass a session token back and forth
- Might be admins/mgrs using the same web server as normal users

#### Psychological Acceptability

Psychological Acceptability is abut recognizing that humans are involved when working with computer security.

This can be hard as all people behave differently.

Ex: Long and complex passwords are more likely to be written down near the computer, and therefore this requirement, while technically secure,
may effectively decrease password security, and piss off users.

Security mechanisms should not make resources more difficult to access. Each layer of difficulty will only encourage users to circumvent them.

Security mechanisms should be transparent, but are rarely transparent.

Complexity of configuration also may lead to insecure software. The harder it is to configure software, the easier it is to misconfigure.
- Configuration should be as easy and intuitive as possible.

Outputs must provide understandable errors.
- No privileged information should be given.
  - 'incorrect creds' vs 'incorrect password'
- Properly described incorrect parameters or errors.

#### Weakest Link

The Weakest Link is the most easily compromised point of a piece of software.

The WL (Weakest Link) is how resilient the software is against a hacker.

The hardest part is actually identifying the WL. Many admins who respond to breaches had no idea the hole existed in the first place. They probably don't monitor or audit either.

It's also important to consider what results in the LARGEST vulnerability (a combination of scope of impact once breached PLUS ease of performance of vulnerability)

- What software components could be breached?
  - Code
  - Services
  - Interfaces

A common mistake orgs make is ONLY focusing on user interfaces and ignoring other possible routes of exploit, like backend services or hackers editing code.

ANY type of break in the weakest link means a breach. WL is a component that CANNOT be compromised -- Some can, and don't impact much of other systems.

#### Leveraging Existing Components

Adding new functionality or writing new code can introduce security vulnerabilities.

Existing components should be used/reused to ensure attack surfaces are not increased, assuming the existing components have already been audited for vulnerabilities.

Q: Do we introduce the functionality as a separate component, or as a change to an existing component?

A: We need to balance EoM (Economy of Mechanism), which is about keeping things simple, with adding new functionality as a new component.

If adding new functionality to the system is MORE COMPLEX than modifying an existing component, we should do the simplest thing! And vice versa.

Keep in mind that any changes to an existing component should be audited.

For example, databases should be leveraged instead of rewriting the database system.

As always, changes bring security issues, and pro/con assessments must be made.

### Privacy

#### The Privacy Principle

Privacy is about controlling the information about something -- Allowing the user to control how information is shared.

This is an important topic and often controlled by law.

- Who is it shared with?
- Why?
- How will it be transferred or used by the 3rd party?

"Traceable sharing" is a way for a user to share information with another party, but it possible to track where the information was divulged.

- ex: Credit card purchase on a site
- We can also verify it is used correctly

Unfortunately, a lot of the time, we can't know how the third party is using the data -- It isn't traceable. We are just trusting them.

##### Data Disposition

Data Disposition is the long-term use of data.

ex: Credit card purchase.
- Do we retain their address? CC#?
  - We are obligated to administer their data according to our policies

If the data that we store is compromised, we will become liable, or lose customers (or piss them off!)

*cough* EquiFax *cough*

Also, using customer data in a test environment is a bad idea:
- Discloses it to all your devs
- Duplicates it across an entirely new system, 'doubling risk'
- Test environments are generally less secure
- Data should be anonymized first
  - Name, address, CC# should be replaced with random data.

#### Privacy Considerations/Privacy Policy

A Privacy Policy is a high-level document that details the following about private information:

- Collection
- Use
- Transfer
- Storage

This document is used to identify what information needs to be safeguarded, how, and the details.

It can also be a guide for employees.

Part of a Privacy Policy is to have a Privacy Disclosure Statement, a public version of the privacy policy, so external parties can understand how data is used and protected.

##### Identifiable Information/PII

Identifiable Information (II/PII) is information that could be used to identify a person.

- Name
- DoB
- Birthplace
- Address
- TIN/SSN/NIN
- Motor Vehicle/Driver's License
- Genetic info/face/prints
- IP Address

It doesn't take a lot of info for data to be considered PII.

###### Protected Health Information

(PHI)

- Demographic data
- Biometrics
- Medical History
- Test data

This area of data is protected by HIPAA/HITECH Acts.

Storing info under this category MUST be protected according to legal mandates.

##### Breaches

Since you are storing PII, you must monitor for breaches.

Lots of companies only take action AFTER a breach is detected, or even worse, never find out a breach occurred because there was so little monitoring.

Security controls must be put in place to:

- Detect a breach
  - What happened
  - How did it happen
  - What data was compromised
  - Will involve logging and auditing

Data should be encrypted so that data cannot be read w/o decryption, which could take years or more.

Some legislation dictates long term data protection guidelines.

#### Protection Principles

In Europe, the EUDPD, or European Union Data Protection Directive, dictates how data is protected.

- Any data collected can only be used for approved purposes as dictated by the owner of the data
- Destroyed after a period of time or rendered nonidentifiable
- Data should not be processed, unless:
  - Usage is transparent (user gives consent to processing)
  - Purpose of processing is legitimate
  - The level of data collected is proportional (appropriate) to its purpose.
    - Helps stop orgs from collecting unnecessary data

#### Safe Harbor

Due to the EU/US differences in data laws, a set of "Safe Harbor" rules were made.

Data can be transferred from Europe -> US, GIVEN THAT:
- Notice
  - Customers must be informed of how their data is collected and used
- Choice
  - Customers can opt out of the transfer or sharing if they choose to
- Onward Transfer
  - Data can only be transferred to third parties who follow data protection principles
- Security
  - Reasonable efforts must be made to protect the data
- Data Integrity
  - Only the data that is required is transferred, and it's used for the purpose it was collected for.
- Access
  - Customers can access their information and correct/delete it.
- Enforcement
  - There's an effective way to enforce these principles

### Risk, Governance, and Compliance

#### Regulations and Compliance

##### Federal Information Security Management Act (FISMA)

This act governs the security of Federal Information Systems and ensures that periodic risk assessments are completed.

- Policies and procedures are in place to mitigate assessed risks
- All subordinate levels (facility access, information systems, etc.) have appropriate security planning
- Staff are properly trained
- Policies are periodically tested and evaluated to ensure their correctness
- Remedial processes are in place to...
  - Implement, document, and evaluate remedial actions
- Planning is done
  - Disaster recovery
  - Etc

###### Identification

Classifying data is IMPORTANT to apply the right level of security to data.

FISMA asked NIST to determine the standards for classifying data within federal agencies.

- Standards
- Guidelines that govern what classification is applied to what data
- Minimum security requirements for each classification

Result of this: NIST made FIPS 199, FIPS 200 publications.

<https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf>

<https://csrc.nist.gov/csrc/media/publications/fips/200/final/documents/fips-200-final-march.pdf>

##### Sarbanes-Oxley (SOX)

SOX is an act that governs corporate financial practices in reporting.

- Created in 2002 after a bunch of corporate financial scandals
- Includes:
  - Public Company Accounting Oversight Boards
  - Enhanced Financial Disclosure and Reporting
  - Corporate and Criminal Fraud Accountability
  - Corporate Tax Returns

SOX includes requirements for recordkeeping and reporting of financial data.

Any system that maintains this type of data must comply with SOX.

##### Health Insurance Portability and Accountability Act (HIPAA)

- Governs the security and privacy of health information

It also governs any org that collects health information.

- Final Security Rule
  - Categories:
    - Protection of transmitted data
    - Data at rest
    - Physical protection
    - Administrative procedures
  - Standards
    - Administrative
    - Technical
    - Physical safeguards
- Final Privacy Rule:
  - An entity (like a healthcare provider) can use any information disclosed to it for its own treatment, payment, and healthcare operations within the organization.
  - Covers issues like notification to patients, prohibiting sale of PII, passing health info to researchers (and how), etc.

##### PCI Data Security Standard (PCI DSS)/Payment Processing

Payment processing is also regulated, through a standard called the PCI DSS.

This standard is used by the PCI (Visa, Mastercard) for the protection of cardholder data and transaction protection when processing transactions like credit card payments

The PCI DSS is broken down into a lot of areas that govern building and maintaining secure networks.
- Build and maintain secure networks/systems
- Protect cardholder data
- Maintain a vulnerability management program
  - Antivirus
- Implement strong access control measures
- Regularly monitor and test networks
- Maintain an Information Security Policy

The DSS is applied to all parties involved in processing.

- Merchants
- Processors
- Acquirers
- Card issuers
- Service providers
- Anyone else who stores, processes, transmits cardholder data.

Credit card fraud is very common, so these regulations make sense.

#### Legal

##### Patents

A patent is a set of exclusive rights granted by a government to an inventor or assignee.

These rights are granted for a specific period of time and are to protect the inventor's rights, so noone else can claim it was their invention like selling it w/o the patent owner's permission.

Patent law varies between countries and can be complex.
- What is patentable?
- How long can it exist?

To get a patent, the owner of the work will need to apply for a patent with the government.

##### Copyrighting

This is another way to protect IP rights.

- Gives a creator of original work the exclusive rights to it.
- Copyrights are applied to any expressible form of an idea or information that is substantive and discrete.
  - Covers
    - Creative
    - Intellectual
    - Artistic

Different from a patent because patents usually don't cover ideas, but focus more on inventions.

Copyrights are governed internationally through the Berne convention.
- Countries that are a part of the convention must recognize each other's copyrights

Depending on the country, copyrights are automatic or must be applied for.

For countries part of the Berne convention, copyrights are automatic. However, you must be able to prove that the work was created by the owner and WHEN it was created.

If an owner of a work thinks their work was copied, in most countries, it is up to the owner to pursue it in court.

##### Trademarks

A trademark is an identifiable quality used to identify products or services from an organization.

This is usually used to protect an org's brand. Logos are usually trademarked.

Trademarks can be made via...
- Common law
- Registration
  - Registration provides the owner a lot more legal protection and the ability to recover more damages if they are incurred

Internationally, trademarks are managed through the World Intellectual Property Organization.

##### Trade Secrets

These protect a secret for a specific amount of time.

- Very tightly controlled
- Offer a lot of protection
- Usually food
  - ...szechuan sauce!!!!
  - Coca Cola

This is difficult to use in Software though: If another party develops similar software INDEPENDENTLY, it is no longer a trade secret.
Example: Using a shopping cart on an ecommerce site.

##### Warranty

This is a protection of a consumer that ensures a product or service will work as advertised, or else they are reimbursed in some way.

- Minimum legal protection for consumers
- Protection:
  - Quality
    - No poor quality
  - Safety
  - Performance (performs as advertised)
  - Durability
  - Defects

Software generally comes with NO warranties...

This means that if you buy software with security holes, there may be no recourse for the consumer to pursue the software retailer for damages...

#### Standards

Standards are not necessarily the most common way of doing something.

Standards are a defined level of activity, usually measured by a third party! A third party must be able to say if you meet a standard or not.

Benefits:
- Can compare 2 organizations
- Can promote interoperability

##### International Organization for Standardization (ISO)

- Founded in 1947

ISO develops and publishes international standards that ensure products are safe, quality, and reliable.

There are over 19,500 standards published for tech, food, and health.

##### National Institute of Standards and Technology (NIST)

- US based
- Develops tech, measurements, and standards that align with the US economy
- Federal Information Processing Standards (FIPS)
  - Governs all nonmilitary gov't agencies and gov't contractors when specified as part of their contract
  - Crypto
  - Personal ident verification for feds + contractors
  - NIST SP 800 series
    - Research and guidelines on securing information systems
  - SAFECode
    - Non-profit, not related to NIST
    - Identify and promote best practices in software dev

#### Risk Mgmt

- Many models exist to model risk
- We'll look at a general model

Risk mgmt's goal is to assess and mitigate anything that could cause harm to the project or deliverables.

- Manage risk in general
- Manage risk through project phases

##### Step 1: Asset Identification

This is where we identify and classify all assets.

- Identify and classify
  - Assets
  - Systems
  - Processes

A common mistake is to only focus on assets we want to protect instead of ALL of our assets. When we do this, we miss protecting "noncritical" assets whose compromise may lead to larger issues later on.

Risks can be weighed by considering:
- Damage to business
- Damage to people
- Financial risks
- Etc

Scoring each factor helps you objectively determine where your priorities should be.

Then, prioritize assets.

Financial costs (lawsuits included) generally are weighted more.

We also need to evaluate the information criticality of the data. This refers to how critical the data is to the business.

For example, if someone loses access to some data, does the rest of business stop?

##### Step 2: Threat Assessment

- Identify threats
- Identify vulnerabilities
  - Exploitable vulns can be used to gain access to all sorts of things, so focus on them.
  - Vulns can climb 'priority ladders' to gain access to higher priority assets
    - Risk priorities must reflect this
- Threat = harm to an asset
  - 'Threat' includes...
    - Incorrect data entry
    - Insider threat

##### Step 3: Impact Determination and Quantification

What's is impact the loss/compromise of an asset would have?

- Determination of loss
  - Tangible (easier to quantify)
    - Financial loss
    - Physical damage
  - Intangible (harder to quantify, but do it anyways)
    - Reputation damage

##### Step 4: Control Design and Evaluation

What controls are needed to mitigate the risks and/or reduce the vulnerabilities?

Controls are countermeasures introduced to reduce/eliminate the risks.

- Controls
  - Actions
  - Devices
  - Procedures

They can be additional action that occur, physical/logical devices, or procedures that address specific risks.

For example, a website that lets you buy stuff with your credit card has the risk of credit card fraud.

One countermeasure could be additional security checks to mitigate that risk.

##### Step 5: Residual Risk Management

This step exists because risk cannot be fully eliminated from a system, and we need to accept that fact.

These remaining risks are called 'residual risks'.

We need to understand these risks to identify and introduce controls along the way to reduce these risks.

- Consider multiple controls to reduce risk

### Software Development Methodologies

#### Waterfall

```

Requirements \
             v
            Design \
                   v
                  Implementation \
                                 v
                                Verification \
                                             v
                                            Maintenance
```

This methodology is the first and most common development methodology.

It's based on a sequential set of phases that govern what's done in each phase.

It is the most used because it's the best known (and old AF.)

It came from the manufacturing process and is simple but NOT adaptive, which is a problem for software projects as requirements are known to change a lot.

Because of this, we need to repeat a lot of work to introduce new requirements.

Waterfalls therefore have the highest risk for increased time and cost.

##### Phase 1: Requirements

All of the requirements of the software are determined and presented as a deliverable.

Requirements are either:
- Functional
  - Describes the function of the system
- Nonfunctional
  - Describes the rest of the requirements that are related but don't fall under the functionality of the system
  - Restrictions are an example of a nonfunctional requirement

These requirements are passed to the next phase.

##### Phase 2: Design

In this phase, software architects blueprint the design of the software.

The "External Functionality" is how the software interacts with the outside world.

- External Functionality
  - Input
  - Output
  - Constraints

- Internal design
  - Algorithms
  - Data structure
  - Internal Routines

At the end of this phase, you should have clear documentation, which is the blueprint to move to the third phase.

##### Phase 3: Implementation

##### Phase 4: Verification

##### Phase 5: Maintenance

#### Agile

### Summary (?delete?)

#### todo, section

### Practice

## Secure Software Requirements

## Secure Software Design

## Secure Software Implementation and Coding

## Secure Software Testing

## Software Acceptance, Deployment, Operations, Maintenance, and Disposal

## Supply Chain and Software Acquisition

