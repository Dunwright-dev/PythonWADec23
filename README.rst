===============================================
**PythonWADec23 - Django Htmx Tailwind Alpine**
===============================================

|

**Version = "0.1.0"**


A presentation to the PythonWA meetup group with some demonstrations.

**Talking Points**

*landing*

Welcome and wait for everyone to settle.

*2 - A bit about me*

Discuss the bullet points.

Talk through the slides that Ben made.

*3 - Locality of behaviour*

Basically means that all of the code relating to the element that is displayed
in the webpage is right there. You don't need to refer to a bunch of other files
just to understand what is going on.

*4 - Introduce Tailwind*

Discuss points on page.

Tailwind also removes all of the default styling from the browser. This gives a clean
slate when starting a project and removes any potential conflicts with your classes.

*5 - Tailwind Components Example*

Just a copy paste from the Tailwind Components page.

Highlight that the menus at the bottom are not working, no JS provided.

*6 - Introduce AlpineJS*

Discuss points on page.

*7 - AlpineJS Example*

Show the working menus on the Tailwind Components demo.

Highlight that Tailwind are using AlpineJS in their components site.
They also have the transition configurations to make it all look smooth.

*8 - Introduce HTMX*

Discuss points on page.

*9 - HTMX Example 1 - Pagination*

A bit of a boring example. Highlight that the refresh timer has not reset.

*10 - HTMX Example 2 - Infinite Scroll*

Using the Django pagination machinery, we can use that for infinite scroll
by adjusting the way the HTMX insert the HTML partial.

*11 - HTMX Example 3 - Active Search*

Show the active search and discuss how it works.

*12 - HTMX Example 4 - CRUD*

Lazy loading in the list of users.

Add a user is utilising HTMX and AlpineJS to display the modal.
Chaining dropdowns using HTMX.

Using events to update the user list after a change and display the message.

Delete is using hx-confirm as a prompt.

*13 - Drawbacks*

Discuss points on page.

*14 - Questions & Resources*

Discuss points on page.

|
.. image:: https://www.repostatus.org/badges/latest/no.svg
   :target: https://www.repostatus.org/#no
   :alt: Project Status: no

|
:License: MIT license















Built with
`Django Cookiecutter <https://github.com/imAsparky/django-cookiecutter>`_
