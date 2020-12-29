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