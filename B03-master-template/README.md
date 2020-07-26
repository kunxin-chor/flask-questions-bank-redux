# Master Template Practise

Create a master template and use it for `about.template.html` and `home.template.html`. The master template should make use of Bootstrap 4.5 (see https://getbootstrap.com/docs/4.5/getting-started/introduction/ 
for the `Getting Started Template`).

For each template, add the content within a Bootstrap container.

## Create a new route
Create a new route, `\our-vision`, which will display the following text:

```
Our mission at ACME Anvils is selling the cheapest products with energy, humor and wit
```

## Add a Nav background

In the master template, add a Bootstrap Navbar which has links to the three pages. Do not hard-code the url, rather use the `url_for` function inside the master template.

## Advanced Challenge
In the master layout, add in a Jumbotron. The header text of the Jumbotron should say `Home`, `About Us`. `Our Vision` respectively for each of the template.
Also, change the background image of the Jumbotron to `about.jpg`,  `home.jpg` and `vision.jpg` respectively. 
