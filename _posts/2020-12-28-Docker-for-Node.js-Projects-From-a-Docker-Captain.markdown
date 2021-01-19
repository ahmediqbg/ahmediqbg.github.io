---
layout: post
title: "Docker for Node.js Projects From a Docker Captain"
date: 2020-12-28
categories: [docker, programming, security]
---


## TOC

From <https://www.udemy.com/course/docker-mastery-for-nodejs/>.

Code/work in <http://github.com/HenryFBP/Docker-for-Node.js-Projects-From-a-Docker-Captain.git>.

* 
This will become a table of contents. Don't touch!  
{:toc}

## Section 2: Docker Compose Basics

    sudo apt install docker docker-compose nodejs npm

### Links

-   <https://docs.docker.com/compose/>
-   <https://github.com/docker/toolbox/releases>
-   <https://docs.docker.com/compose/compose-file/>
-   <https://github.com/BretFisher/ama/issues/8>
-   <https://docs.docker.com/compose/compose-file/compose-versioning/>
-   <https://github.com/docker/docker.github.io/pull/7593>

### Why compose?

-   CLI is designed around dev workflows
-   Not really designed for production
-   `docker-compose` CLI talks to docker daemon and can be a substitute for the `docker` CLI itself
-   `docker-compose` takes long-ass commands with 20+ flags and puts them into YAML files
-   "Let's not create more scripts, but make a tool that automates workflow in a declarative way"
-   Use the `docker-compose` for dev't but not for deployment, that should be done with `docker` command.
-   Do not use `docker-compose` in prod. Swarm/K8s should be used instead.

### Compose File Format

-   Not industry standard
-   Unique to `docker-compose`
-   Designed to describe 1 or more containers/networks/volumes; etc and those are called "services"
-   Can layer sets of YAML files, use templates, variables, and even more
-   Good idea to stick with single default/simple `docker-compose.yml` file initially
-   (see <https://github.com/HenryFBP/Docker-for-Node.js-Projects-From-a-Docker-Captain/blob/master/docker-mastery-for-nodejs-assignments/sample-01/docker-compose.yml>)
-   On line 6, the `.` means build the folder that `docker-compose.yml` is currently residing in.
-   Line 7/8, ports is a list of ports that are published/processed by docker
-   Note: Docker v3 does NOT replace v2. If you're just focusing on docker-compose locally, there's no reason to use v3. v3 is focused on multi-node server orchestration like secrets etc. v2 is focused on single-node dev workflow. v2 has unique features not found in v3.

### Docker-Compose CLI

-   `docker-compose` cli is designed around developer happiness.
-   Many IDEs support it but don't rely on it. Understand CLI.
-   'batteries included, but swappable' is docker's idea
    -   A lot of things come default OOTB. Well documented but not obvious. You can always change stuff.
-   CLI and YAML versions differ, cliv2 NOT equals to yamlv2
-   `docker-compose up`
    -   "run everything"
        -   "`clone blah; cd blah; docker-compose up"`
    -   Build/pull image(s) if missing
    -   Create volume/network container(s)
    -   Start container(s) in foreground (-d to detach, usually want to do this)
    -   When you run `docker-compose up` the first time, it may build images for you, but it's not always going to rebuild those images every time something changes. If you want to rebuild images every time, you add the `--build` command.
-   `docker-compose down`
    -   "Stop and delete network/containers"
    -   "Leave data alone"
    -   Will not delete volume data. This is a core feature of Docker. You can delete volumes with `-v`. 
-   Many of these commands have "service" options at the end
    -   You type the command, and then a name of a service from the compose file (service name), and that command will be specific for just that service.
-   `build`, just rebuild
-   `stop`, stop and don't delete
-   `ps`, list "services"
-   `push`, push to registry (you must name the images properly)
-   `logs` same as docker CLI
-   `exec` same as docker CLI

### Assignment: Compose CLI basics

- <https://asciinema.org/a/dOn9WE4X4KvYP7r4g07RcPtf4>
- <https://github.com/HenryFBP/Docker-for-Node.js-Projects-From-a-Docker-Captain/blob/master/assignments/compose-cli-basics/recording.cast>

## Section 3: Node Dockerfile Best Practice Basics

### Dockerfile Best Practice Basics

#### COPY vs ADD

- Use COPY and not ADD most of the time.
- COPY and ADD essentially do the same thing but ADD does a lot more. Default to COPY.

#### npm and yarn

-   npm/yarn are not necessary to install, you can usually use the one that comes with node.
-   Also it doesn't matter if you use npm or yarn.
-   Make sure you always clean up extra stuff (`npm cache clean --force`)
-   Use `CMD node`, not `npm`
-   `npm` does not work well as an init process, which is how containers work. 1 process launches everything else.
    -   `npm` does not pass signals correctly to node and tends to improperly shut down the container.

#### WORKDIR or mkdir

-   Use `WORKDIR` and not `RUN cd`/`RUN mkdir`
    -   ...however `WORKDIR` will not set permissions on dirs like `chown`

### FROM Base Image Guidelines

-   Base image is the image all of your Node apps will be built on.
-   Stick to even numbered major Node releases
    -   Even=stable, odd=experimental
-   Don't use `:latest` tag
-   Pick a stable node version early and stick with that
-   Start with Debian if migrating versions
-   Stick with what you know and move to Alpine (more minimal and smaller) later
    -   Not every app will work flawlessly out of the box using an Alpine base image
-   Don't use `:slim`
    -   ...but it has `apt`. Use this only if you CAN'T use Alpine. May be a PITA to modify.
-   Don't use `:onbuild`.
    -   It's a Dockerfile command that we don't use (why tho?)
    -   It tends to cause problems later on
    -   Originally it was the idea that commands could be set in an official repo that would execute whenever you pulled an image
    -   This caused users to experience a lack of causality in their commands and not be able to know what was being executed

#### <https://hub.docker.com/_/node>

-   All images by default use Debian as their base image.
    -   You get `apt`, `openssl`, `bash`, etc.
-   Latest image is >800MB
-   We will use 11/alpine and 10/alpine.

### When to use Alpine, Debian, or CentOS images

- <https://kubedex.com/follow-up-container-scanning-comparison/>
- <https://www.youtube.com/watch?v=e2pAkcqYCG8>

#### Alpine

-   Alpine is 'small' and 'sec focused'
-   Minimal utilities OOTB
-   But Debian/Ubuntu bases are smaller now too (100MB/85MB)
    -   Used to be 150/200MB
-   Who cares about 100MB anyways?
    -   IoT?
-   Alpine has its own issues
    -   2018 nodemon had a problem only on Alpine
-   Alpine CVE scanning fails
    -   Current Alpine CVE scanning doesn't work due to an Alpine file translation database linking issue
    -   Debian/Ubuntu/CentOS do work better with the CVE scanning

- Enterprises may require CentOS or Ubuntu/Debian (there is no CentOS/RHEL Node image)

### Assignment: Making a CentOS Node Image

See code repo at top.