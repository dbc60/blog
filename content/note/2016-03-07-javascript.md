---
layout: post
title: JavaScript
categories: notes
tags: [javascript]
excerpt: Learning to learn JavaScript
---

## Contents
{:.no_toc}

- TOC
{:toc}

## Project Directory Layouts

### One Layout
This layout is what one team uses for their ReactJS projects.

```
project/
|-- actions/    (Flux action creators)
|-- components/ (JSX React components (the presentation layer), so there are subfolders like
                 "pages", "controls", etc.)
|-- images/
|-- reducers/   (Redux reducucers - they're the logic that handles all the application state)
|- services/    (basic ES6 modules, with methods like "fetchUser(id)" which use the new JS Fetch
                 API behind the scenes. With redux-thunk and redux-promise middleware the team can
                 easily offload state manipulation to these services w/o actually putting state
                 logic in them)
|-- utils/
|-- app.js
```

### Domain Folder Layout
Instead of folders like "`actions/userActions.js`" and "`reducers/userReducers.js`", this layout uses "`users/actions.js`" and "`users/reducers.js`." There's a good template [here](https://github.com/scottwoodall/django-react-template). Under the `frontend/src/app` directory, the template has the following layout:

```
app/
|- actions/
|   |-- alerts.js
|   \-- collection.js
|
|-- components/
|   |-- alers/
|   |-- higherOrder/
|   |-- master/
|   |-- DeleteButton.js
|   |-- EmptyComponent.js
|   |-- LinkedListGroup.js
|   |-- Pagination.js
|   |-- PaginationInfo.js
|   |-- RefreshButton.js
|   \-- SearchBox.js
|
|-- layouts/Admin/
|   |-- MainFooter.js
|   |-- MainHeader.js
|   |-- MainSidebar.js
|   \-- index.js
|
|-- reducers/
|   |-- alerts.js
|   \-- collection.js
|
|-- users/
|   |-- components/
|   |-- containers/
|   |-- constants.js
|   |-- records.js
|   |-- reducers.js
|   \-- routes.js
|
|-- utils/
|   |-- http.js
|   |-- isFilterActive.js
|   \-- viewportDimensions.js
|
|-- Root.js
|-- configureStore.js
|-- history.js
|-- rootReducer.js
|-- routes.js
```


## JavaScript Libraries
- redux: keeps track of all the state (UI and domain) in a single object.
- immutable.js: for the immutable data structures which play nicely with the React ecosystem. It also has a rich set of data structures taht aren't found natively within JavaScript. For example, one could make use of `Records` to simulate domain models.
- react-router: for routing within the application.
-superagent: for ajax calls.
- reselect: If you're using redux, you'll cherry pick various parts of the state tree for your components. If any of the data used within components can be derived, then reselect comes into play nicely.

## References
- [Long discussion of a Free React.js Fundamentals Course on HN](https://news.ycombinator.com/item?id=11204481)
- [Free React.js Fundamentals Course](http://courses.reactjsprogram.com/courses/reactjsfundamentals)