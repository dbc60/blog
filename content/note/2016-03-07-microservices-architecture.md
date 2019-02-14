---
title: Microservice Archtecture
date: 2016-03-07
categories: web
draft: true
tags: [micrososervices]
---

What is a microservice architecture and how can I put it to use?
<!--more-->

## Goals
I'd like to understand how to design a highly scalable web application where it can serve lots of requests, provide dashboards and logs of the ongoing and historical activity on the site, and make the data available for automated analysis. It should be secure, so the data that can be viewed by any particular party is limited to a subset of the total data in the system and that subset is defined by access control rules based on the party's authentication and authorization.

## The Monolithic Application Architecture
A monolithic architecture typically consists of a three-tier design. The front end is the presentation tier, which might be an application-specific GUI on the desktop or in a browser. The middle tier is the application, and at the back end is a data tier. The application delivers data to the browser, which provides the means for users to request information from the application, view it, and (usually) manipulate or change it. The application reads and writes information from and to the data tier, where a database or other storage device or application organizes and maintains it. The application has the logic for interacting with the other two tiers and for transforming the data as requested by the user.

The drawbacks of the monolithic application architecture derive from the fact that the application is written as a single, unified code base. This makes it difficult for developers to change an application with the agility and flexibility they need to keep pace with the expectaions of mobile users, and for operations teams to scale the applicatin up and down to match demand.

The three-tier architecture lacks scalability, because the functional components of the application are packaged together as a unit. The only way you can respond to changing levels of client demand is to scale the entire application.

## The Four-Tier Application Architecture
The four-tier model is designed to create a foundation for excellent performance, device-tailored experiences, and allows for integration of both internal services and applications as well as third-party services and APIs. The [Forrester Four-Tier Engagement Platform](http://blogs.forrester.com/ted_schadler/13-11-20-mobile_needs_a_four_tier_engagement_platform) is divided into client, delivery, aggregation and services layers.

- Client tier.
  - Responsible for experience delivery.
  - Leverages the delivery, aggregation and services layers to create device-specific and highly tailored experiences.
  - Mobile clients.
  - Wearables.
  - Internet of Things (IoT).
  - Web browsers.
  - Good old-fashion desktop app?
- Delivery tier.
  - Optimizes content for proper display on device.
  - Caches content for performant delivery.
  - Drives personalization by using analytics to monitor user behavior.
- Aggregation tier.
  - Aggregates and federates services' tier data.
  - Provides discovery for the underlying service library.
  - Performs data protocol translation (e.g., SOAP to JSON).
- Services tier.
    - Existing on-premises systems of record, services, and data.
    - External third-party services (e.g., Box, Twilio, Urban Airship).

The components you need to adopt a four-tier architecture might include such things as:

- client-tier: a capability to stream media in a way that's best for specific devices.
- delivery-tier:
    -a load balancer.
    - a caching mechanism.
- aggregation-tier:
    - a reverse proxy to request and cache data from a variety of services.
    - a platform for your own APIs, to easily manage and secure them.
- services-tier: code to support and coordinate a variety of microservices, which consist of highly reliable and independent components.

## Best Practices at Netflix
Notes from [Adopting Microservices at Netflix: Lessons for Architectural Design](https://www.nginx.com/blog/microservices-at-netflix-architectural-best-practices/).

### What is a Microservices Architecture?
Adrian Cockcroft (once the Director of Web Engineering and Clound Architecure and Netflix) defines a microservices architecture as a service-oriented architecture composed of _loosely coupled_ elements that have _bounded contexts_.

_Loosely coupled_ means that you can update the services independently; updating one service doesn’t require changing any other services. One kind of coupling that can be overlooked is database coupling, where all services talk to the same database and updating a service means changing the schema. You need to split up the database and denormalize it.

The concept of _bounded contexts_ comes from the book Domain Driven Design by Eric Evans. A microservice with correctly bounded context is self-contained for the purposes of software development. You can understand and update the microservice’s code without knowing anything about the internals of its peers, because the microservices and its peers interact strictly through APIs and so don’t share data structures, database schemata, or other internal representations of objects.

### Create a Separate Data Store for each Microservice
You want the team for each microservice to choose the database that best suites the service. It has the benefit that each team can structure their database independently of the others.

Breaking apart the data can make data management more complicated, because the separate storage systems can more easily get out sync or become inconsistent, and foreign keys can change unexpectedly. You need to add a tool that performs [master data management](http://en.wikipedia.org/wiki/Master_data_management?utm_source=microservices-at-netflix-architectural-best-practices&utm_medium=blog) (MDM) by operating in the background to find and fix inconsistencies. For example, it might examine every database that stores subscriber IDs, to verify that the same IDs exist in all of them (there aren’t missing or extra IDs in any one database).

### Keep Code at a Similar Level of Maturity
If you need to add or rewrite some of the code in a deployed microservice that’s working well, the best approach is usually to create a new microservice for the new or changed code, leaving the existing microservice in place. [Editor’s note: This is sometimes referred to as the [immutable infrastructure](http://highops.com/insights/immutable-infrastructure-what-is-it/?utm_source=microservices-at-netflix-architectural-best-practices&utm_medium=blog) principle.] This way, you can interatively deploy and test the new code until you're sure it works as intended, without risking failure or performance degradation in the existing microervice.

### Do a Separate Build for each Microservice
Separate builds allows each microsservice to pull in component files from the repository at the revision level appropriate to it. It trades a more complicate process for tracking and decommissioning old file versions, for the ease of adding new files as you build new microservices. You want the process of introducing a new microservice, file or function to be easy, not dangerous.

### Deploy in Containers
Deploying microservices in containers means you need just one tool to deploy everything. As long as the microservice is in a container, the tool knows how to deploy it. It doesn’t matter what the container is.

### Treat Servers as Cattle
Servers should be treated as interchangeable members of a group. THey all perform the same functions, so you don't need to be concerned about them individually. Your only concerns are that there are enough of them to produce the amount of work you need, and can you automatically adjust their numbers to handle changes in load.

## The Patterns
The [Microservice Architecture site](http://microservices.io/patterns/index.html) lists a series of patterns related to microservices.

1. Core Patterns
    1. [Monolithic architecture](http://microservices.io/patterns/monolithic.html), probably listed for contrast.
    2. [Microservices architecture](http://microservices.io/patterns/microservices.html)
    3. [API gateway](http://microservices.io/patterns/apigateway.html)
2. Service Discovery Patterns
    4. [Client-side discovery](http://microservices.io/patterns/client-side-discovery.html)
    5. [Server-side discovery](http://microservices.io/patterns/server-side-discovery.html)
    6. [Service registry](http://microservices.io/patterns/service-registry.html)
    7. [Self registration](http://microservices.io/patterns/self-registration.html)
    8. [3rd party registration](http://microservices.io/patterns/3rd-party-registration.html)
3. Deployment Patterns
    9. [Multiple service instances per host](http://microservices.io/patterns/deployment/multiple-services-per-host.html)
    10. [Single service instance per host](http://microservices.io/patterns/deployment/single-service-per-host.html)
    11. [Service instance per VM](http://microservices.io/patterns/deployment/service-per-vm.html)
    12. [Service instance per Container](http://microservices.io/patterns/deployment/service-per-container.html)
4. Data Patterns
    13. [Database per Service](http://microservices.io/patterns/data/database-per-service.html)
14. [Microservice chassis](http://microservices.io/patterns/microservice-chassis.html)

## What Services Do I Need?
- datastore: postgresql, sqlite
- message queueing: RabbitMQ, ZeroMQ or some other message queue.
- SMTP services for outbound mail, like Postfix. The application, or its components, may need need to send email alerts.
- Caching: memcached?
- routing:
- authentication:
- authorization:
- logging:
- service discovery:
- load balancing:
- Health checks:
- Metrics:
- A tool for deploying containers: Chef? Puppet? Ansible? Salt? Just say no to Docker.

## The Microservice Chassis
[This pattern](http://microservices.io/patterns/microservice-chassis.html) stinks. It's written with the headings of an architectural pattern, but it does *NOT* describe a solution to the problems and concerns it proports to address.

It starts with the stating some of the concerns with developing an application in the [microservices architecture](http://microservices.io/patterns/microservices.html). It lists two "forces" and then says the solution is to use a microservices chassis framework. Instead of describing what such a framework might look like, all it does is give a few examples of projects that might be microservice chassis.

The general context is that in developing an application, there are always serveral cross-cutting concerns that must be handled. These are such things as:
- Externalized configuration, such as credentials, and network locations of external services such as databases and message brokers.
- Logging and the configuration of such services.
- Health checks - configuring endpoints that a monitoring service can "ping" to determine the health of an application, service or that a client can ping to make the same determination.
- Metrics - measurements that provide insight into the state of the application and how it is performing.
- service registration and discovery.
- circuit breakers for reliably handling partial failures.

You cannot afford to spend a few days configuring the mechanisms to handle cross-cutting concerns for each service, because you will likely have tens or hundreds of services, each of which will take days or weeks to develop.

The goals/forces-at-play are:
- Creating a new microservice should be fast and easy.
- When creating a microservice you must handle cross-cutting concerns such as externalized configuration, logging, health checks, metrics, service registration and discover, circuit breakers and others. There are also cross-cutting concerns that are specific to the technologies that the microservices use and are built upon.

The solution is to build microservices using a microservice chassis framework, which handles cross-cutting conerns. Examples of such frameworks are:

- Java
    - [Spring Boot](http://projects.spring.io/spring-boot/) and [Spring Cloud](http://cloud.spring.io/)
    - [Dropwizard](https://dropwizard.github.io/)
- Go
    - [Gizmo](http://open.blogs.nytimes.com/2015/12/17/introducing-gizmo/?_r=2)
    - [Micro](https://github.com/micro)
    - [Go Kit](https://github.com/go-kit/kit)

## Service Discovery
According to [this article](https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/) on the [NGINX blog](https://www.nginx.com/blog/) there are two service-discovery patterns: [client-side discovery](http://microservices.io/patterns/client-side-discovery.html) and [server-side discovery](http://microservices.io/patterns/server-side-discovery.html).


## The Twelve-Factor App
See [The Twelve-Factor App](http://12factor.net). The epub document, 12factor.epub, explains each of these twelve factors. The justification is compelling. I hadn't considered all of these aspects before.

1. Codebase: One codebase tracked in revision control, many deployments.
2. Dependencies: Explicitly declare and isolate dependencies.
3. Configuration: Store configuration in the environment.
4. Backing Services: Treat backing Services as attached resources.
5. Build, Release, Run: Stricly separate build and run stages.
6. Processes: Execute the app as one or more stateless processes.
7. Port Binding: Export services via port binding.
8. Concurrency: Scale out via the process model.
9. Disposability: Maximize robustness with fast starup and graceful shutdown.
10. Development/Production Parity: Keep development, staging and production as similar as possible.
11. Logs: Treat logs as event streams.
12. Administrative Processes: Run administrative/management tasks as one-off processes.

Note that *backing service* is any service the app consumes over the network as part of its normal operation. Examples include datastores (such as MySQL or CouchDB), messaging/queueing systems (such as RabbitMQ or Beanstalkd), SMTP services for outbound email (such as Postfix), and caching systems (such as Memcached).

## References

- [Microservices at Netflix](https://www.nginx.com/blog/microservices-at-netflix-architectural-best-practices/)
- [It's Time to Move to a Four-Tier Application Architecture.](https://www.nginx.com/blog/time-to-move-to-a-four-tier-application-architecture/)
- [The Four-Tier Engagement Platform](http://blogs.forrester.com/ted_schadler/13-11-20-mobile_needs_a_four_tier_engagement_platform)
- [Adopting Microservices at Netflix: Lessons for Team and Process Design](https://www.nginx.com/blog/adopting-microservices-at-netflix-lessons-for-team-and-process-design/)
- [What is utm_source?](https://www.maketecheasier.com/what-is-utm-source/)
- [Does Piwik support Google Analytics campaign parameters (utm_campaign, utm_medium, utm_source, utm_term)?](http://piwik.org/faq/general/faq_119/)
