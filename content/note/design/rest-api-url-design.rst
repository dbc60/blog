---
title: REST API URI Design
date: 2019-04-08
draft: true
categories: [design]
tags: [rest, api, uri]
---

REST APIs use Uniform Resource Identifiers (URIs) to identify and address
resources.
<!--more-->

Some designs are based is this quote:

.. pull-quote::

    The only thing you can use an identifier for is to refer to an object. When you are not dereferencing, you should not look at the contents of the URI string to gain other information.

    -- Tim Burners-Lee

It means that these two URIs are equivalent, but the first one conveys too
much information::

    http://api.example.com/louvre/leonardo-da-vinci/mona-lisa

    http://api.example.com/68dd0-a9d3-11e0-9f1c-0800200c9a66

First a reminder of the URI format, as the rules and guidelines below depend on it. The generic URI syntax, as defined by `RFC 3986`_, is::

    URI = scheme "://" authority "/" path ["?" query]["#" fragment]

<!--more-->

.. contents:: Contents
   :class: sidebar

**********************************
`7 Rules for REST API URI Design`_
**********************************

Rule 1: Trailing Slash
**********************

The first rule of URI design is that a trailing forward slash should *not* be included in URIs. It adds no sematic value and may cause confusion.

There are two reasonable ways to treat trailing slashes. Since each character within a URI count toward a resource's unique identify, then each should map to a different resource. Alternatively, a more forgiving API would redirect clients to URIs without a trailing forward slash, and they may also return HTTP error code 301 - "Moved Permanently".

Rule 2: Hierarchical Relationships
**********************************

Use a forward slash to indicate a hierarchical relationship. The forward slash is used in the path portion of the URI to separate a parent resource from a child. Parents might be collections of child resources, or child resources might be specializations of the parent. For example::

    http://api.canvas.com/shapes/polygons/quadrilaterals/squares

Rule 3: Use Hyphens to Improve Readability
******************************************

Anywhere you would use a space or a hyphen, use a hyphen in a URI::

    http://api.example.com/blogs/john-doe/posts/this-is-my-first-post

Rule 4: Do Not Use Underscores in URIs
**************************************

Browsers, editors and other text viewer applications will often underline URIs to provide a visual cue that they are clickable. Underscores can be partially obscured or completely hidden by the applications underline mechanism.

Rule 5: Prefer Lowercase Letters in URI Paths
*********************************************

`RFC 3986`_ defines some parts of URIs as case-sensistive, but also has rules about normalizing URIs to lowercase. It can be confusing if your API defines URIs with anything but lowercase letters.

Rule 6: Don't Include File Extensions
*************************************

File extensions are neither consistent nor a well defined means of indicating a file's content over the web. A REST API should rely on the media type, as communicated through the Content-Type header, to determine how to process a body's content.

REST API clients should be encouraged to utilize HTTP's provided format selection mechanism, the Accept request header.

To enable simple links and easy debugging, a REST API may support media type selection via a query parameter.

Rule 7: Use Plural Forms to Identify Resource Collections
*********************************************************

Even if there is only one instance of a "thing", using a plural word will make your API simpler, consistent and easier to understand. For example, you won't have to know in advance whether there is just one instance or multiple instances of a particular resource.

Even relations that can exist within only one resource can be handled with plural words as guided by RESTful principles. For example, a student has several courses. These courses arelogically mapped to the ``/students`` endpoint as follows:

* http://api.college.com/students/3248234/courses will retrieve a list of all courses registered to the student with ID ``3248234``.
* http://api.college.com/students/3248234/courses/physics will retrieve the physics course or courses (perhaps it's possible for there to be more than one) registered to the student with ID ``3248234``.

*************************************
`5 Basic REST API Design Guidelines`_
*************************************

According to this article, there are five basic design guidelines that make a RESTful API. The five are:

#. Resources (URIs)
#. HTTP Methods
#. HTTP Headers
#. Query Parameters
#. Status Codes

1. Resources (URIs)
*******************

Describe your resouces with concrete names rather than verbs. The HTTP methods, like ``GET``, ``POST``, or ``DELETE`` are the verbs that act on your resources.

Define URIs with lowercase words separated by hyphens.

2. HTTP Methods
***************

* GET: use to retrieve information identified by a URI.
* HEAD: same as GET, but transfers the status line and header section only.
* POST: send data to the server using HTML forms.
* PUT: replaces all curent representations of the target resource with the uploaded content.
* DELETE: removes all current representations of the target resource identified by a URI.
* OPTIONS: describes the communication options for a target resource.


3. HTTP Headers
***************

HTTP header fields provide required information about the request or response, or about the object sent in the message body. There are 4 types of HTTP emssage headers:

* General Headers: these header fields have general applicability for both request and response messages.
* Client Request Headers: these header fields have applicability only for request messages.
* Server Response Headers: these header fields have applicability only for response messages.
* Entity Headers: these header fields define meta information about the entity-body or, if no BODY is present, about the resource identified by the request.

4. Query Parameters
*******************

When it comes to query parameters, consider how paging, filtering, sorting, and searching will be affected by the amount of data that your application will return.

Paging
======

Anticipate how to page resources early in the design phase of your API. It is difficult to forsee the amount of data that will be returned. Therefore, paginate your resources with default values when they are not provided by the client. For example, use a range of values like 0 - 25 for the first page.

Filtering
=========

Filterhing consists of restricting the number of queried resources by specifying some attributes and their expected values. Ensure it is possible to filter a collection on several attributes at the same time, and allow several values for each filtered attribute.

Sorting
=======

Sorting the result of a query on a collection of resources. A sort parameter should contain the names of the attributes on which the sorting is performed. Each attribute should be separated by a comma.

Searching
=========

A search is a sub-resource of a collection. As such, its result will have a different format than the resources and the colletion itself. This allows us to add suggestions, corrections and information related to the search. Parameters are provided the same way as for a filter, through the query-string, but they are not necessarily exact values, and their syntax permits approximate matching.

5. Status Codes
***************

It is very important that as a RESTful API, you make use of the proper HTTP Status Codes, especially when mocking a RESTful API. The most used status codes are:

* 200: OK. Everything is working
* 201: CREATED. A new resource has been created.
* 204: NO CONTENT. The resource was successfully deleted. There is no response body associated with this code.
* 304: NOT MODIFIED. The data returned is cached data, because it has not changed.
* 400: BAD REQUEST. The request was invalid, or cannot be served. The exact error should be explained in the error payload. For example, "The JSON is not valid."
* 401: UNAUTHORIZED. The request requires authentication.
* 403: FORBIDDEN. The server understood the request, but is refusing it or the access is not allowed.
* 404: NOT FOUND. There is no resource behind the URI.
* 500: INTERNAL SERVER ERROR. API developers should avoid this error. If a serious error occurs, the stack trace should be logged, but not returned as a response.


**********
References
**********

* _`7 Rules for REST API URI Design`: http://blog.restcase.com/7-rules-for-rest-api-uri-design/
* _`RFC 3986`: https://www.ietf.org/rfc/rfc3986.txt
* _`5 Basic REST API Design Guidelines`: http://blog.restcase.com/5-basic-rest-api-design-guidelines/
* `RESTcase RESTful API Mocking <http://www.restcase.com/>`_
