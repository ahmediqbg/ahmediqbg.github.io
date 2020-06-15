---
layout: post
title:  "Certified Secure Software Lifecycle Professional (CSSLP) Notes"
date:   2020-06-15
categories: [programming, certification, security]
---

## TOC
* This will become a table of contents. Don't touch!
{:toc}

## Preamble
This is a collection of notes I've taken for the CSSLP.
Hopefully they are useful to you as well!

<https://www.isc2.org/Certifications/CSSLP>

## Secure Software Concepts

-   Main concept is about restricting user access

### Confidentiality

-   Keep info away from people who don't NEED to know it
-   Secret info remains secret

-   Must understand what data needs to be kept secret
-   In order to do this, data must be classified, e.g.
    -    Public
        -   Available to everyone
    -   Nonpublic
        -   Restricted in some way
        -   Who can access this data?
 
``` 
publicly disclosed? --> no --> disclosed by roles? --> no --> [restricted]
      |                                 |
     yes                               yes
      |                                 |
  [public]                        [confidential]
```

#### Data protection

-   Confidentiality Controls
    -   *Masking*
        Deleting parts of data, i.e. removing first 12 digits of credit card
    -   Secret writing
        -   Covert (hidden among other data)
            The placement of the data is itself hidden. May also include encryption/ciphers.
            -   Steganography
            -   Digital Watermarking
        -   Overt (visible)
            The data we're protecting is in plain sight, but the method of decrypting/deciphering is not known to others.
            -   Encryption
            -   Hashing (i.e. passwords)

#### Where do we need confidentiality?
-   In transit
    -   Unprotected Networks
-   In processing
    -   Data in memory
-   In storage
    -   Data at rest
    
### Integrity

Integrity means the data is protected from any unauthorized change.

Changes must be done by an authorized user.
This means we need an authorization scheme, and a way to determine that data is 'authentic', to have proof that

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

#### Input validation

-   Users inputting data accidentally
-   Many types of accidental or intentional errors
-   'Injection flaw', i.e. SQLi
    -   Compromise input of data OR entire system
-   Input validation ensures data integrity

#### Parity Bit Checking

-   Detects errors or changes made during transit
-   An extra bit is added to a piece of data
    -   It is `1` if the data is odd/even, `0` if it's the other choice.
-   Fast to calculate, but...
-   You can still change data to manipulate the parity check to be successful
    -   ...all powers of 2 are even (except 2^0), flipping them doesn't change the parity.
        -   Parity bits are essentially a copy of the last bit AFAICT.

```
    1   1   0   0   0   1   1   0
    ^
    |
 parity
   bit
```

#### Cyclic Redundancy Checking (CRC)

-   Uses parity bit checking for data integrity
-   Good for integrity checking during transmission
-   But, CRC can be recalculated and modified

-   CRC calc uses 1 bit for polynomial
-   Most polynomials are 16/32 bits
-   This polynomial is used to calculate a checksum value that is added to the data
-   More bits = more accuracy = harder to change the data in a way that cannot be detected by examining the checksum
-   Altering the data results in a mismatch when recalculating the CRC

-   CRC are based on cyclic ECC
-   CRC =/= hash fn, but very similar in behavior

<https://eklitzke.org/crcs-vs-hash-functions>

#### Hashing

-   A hash is a (generally) smaller value derived from performing a calculation on a large piece of data
-   When putting the large data through a hash fn, the same hash is (almost always) going to be returned by the hash 
    function
-   `hash(coolio) -> 681`
-   When my friend on their computer hashes `coolio`, they also get `681`
-   Calculation 'cannot be reversed'
    -   ...unless you try every possible input value (brute-force)
    -   The ALGORITHM is a ONE-WAY algorithm...hashes CAN BE REVERSED, it's just that with
        strong hashes, this is unfeasible. Try using MD5 password hashes if a nation-state wants to target you
        -- They might have 10000 GPUs.
-   Can ensure confidentiality -- Transmitting a password hash only provides the other party *the means to validate a 
    password*, not the password itself.
    -   This is how NTLM (NT Lan Manager) auth works. Very insecure because of OTHER reasons though.
-   Many different algos to make hashes
-   'digital fingerprinting'
    -   A hash guarantees that the data is intact
    -   A digital signature guarantees that the HASH AND DATA were provided by a specific entity
    -   We know who made it, and that it is intact
    -   Example: 
        <http://releases.ubuntu.com/focal/MD5SUMS>
        <http://releases.ubuntu.com/focal/MD5SUMS.gpg>



### Availability

-   Making sure data is available to users
-   How valuable is the data?


```
minimal/no impact upon destruction? --> no --> significant impact? --> no --> critical impact
                |                                   |                               |
               yes                                 yes                          [critical]
                |                                   |                            
            [support]                          [essential]
```

-   Low-value data is less critical and is 'more ok' to destroy
-   Must ensure no disruption to operation because any interruption could make a piece of data unavailable
    -   i.e. 'Products' database goes down, and 5,000 stores across America depend on that...millions of dollars per 
        minute potentially lost
-   Both data and RELATED systems must be protected
    -   A breach in any RELATED system could compromise the data


#### Maximum Tolerable Downtime
-   Must establish a 'Maximum Tolerable Downtime'
    -   MOST systems CAN be down for some amount of time
        -   Maybe not nuclear reactors, but bank sites CAN be offline for a few hours per day/week.
    -   2 days per week, or '99.9% uptime'
    -   Many systems (esp 3rd party) have SLAs (service level agreement) that ensures
        a minimum.

#### Recovery Time Objective

-   Must consider RTO when UNPLANNED downtime occurs
-   RTO is the maximum amount of time that it takes to recover a system from a failure
-   This is important when planning SLA lengths
-   If we said RTO=1h, and a disaster happened, we should be back up and running within 1 hour.


-   Targeted duration for recovery
-   Explicitly state RTO in SLAs
-   Consider this during recovery planning

-   Determine the impact of unavailability
    -   Can't take orders?
-   Measure impact quantitatively and qualitatively
-   The way an org uses data will change over time, so both current and new data must be considered.

### Authentication and Authorization 1

-   Many ways to authenticate
    -   Anonymous
        -   Not secure
        -   No creds
        -   Avoid using this method if you care about securing something
        -   Unlinkability
            -   You cannot tell WHO performed an action
    -   'Basic'
        -   Base64 encoded creds sent over HTTP in every request
        -   Basically plaintext creds (encoding is NOT encryption!!!) ...so...encrypt your traffic...or don't use this method.
        -   Very widely used unfortunately, and common
    -   Digest
        -   Challenge/response
        -   Only password hashes are transmitted
    -   Integrated auth
        -   Uses challenge-response
        -   NTLM auth is integrated with Windows
        -   Standalone vs Kerberos v5 auth
    -   Client certs
        -   Digital Certs
        -   Internet/e-commerce
    -   Forms
        -   Web apps
            -   Uname+pw gives the client a auth token to reuse (session token)
        -   SSL should be used because uname+pw are transmitted over HTTP.
    -   Token-based auth
        -   Used with uname+pw
        -   Once verified, token is issued
    -   Smart Cards
        -   Ownership-based auth
        -   Creds stored on a microchip
        -   Difficult to compromise
            -   Needs the password and the smartcard as well
    -   Biometrics
        -   Unique physical characteristic of user (fingerprints, retina)
        -   Can be expensive
        -   Suffers from errors (rare though)
            -   Type I (False Negative)
            -   Type II (False Positive)
        -   Detection is complex and errors happen

Forms and basic are different because forms are made by web devs and basic auth is handled by the webserver software (sent in HTTP headers).

### Authentication and Authorization 2



### Accounting