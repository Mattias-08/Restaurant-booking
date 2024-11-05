# **Testing**

This is the TESTING file for the [Restaurant Booking](https://restaurant-booking-systems-c7e901b3d3c6.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## **Testing Contents**
  
- [Testing](#testing)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Lighthouse Scores](#lighthouse-scores)
  - [Manual Testing](#manual-testing)
    - [Functional Testing](#functional-testing)
    - [Site Responsivity](#site-responsivity)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)

## **Validation**

### HTML Validation

To validate my HTML code, I used the [HTML W3C Validator](https://validator.w3.org).

I had a error in my base.html so all my pages had the same bug:

![HTML validation error for landing page](/docs/testing/validationerror_html.png)

Once I had resolved the issues on the list, validation passed on every page. I will address the error fixes in the [bugs](#bugs) section below.
I was given the all clear for every page with 'No errors or warnings to show', as seen here.

![HTML validation pass](/docs/testing/valid_html.png)

After i adjusted html none of the pages had any bugs as shown below:

![HTML validation pass](/docs/testing/valid)

### CSS Validation

I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate my custom CSS file. I did not test bootstrap CSS.
The result came back with no errors found as can be seen here.

![CSS validation pass](/docs/testing/css_validator.png)

---

### Python Validation

# AAAAAADDD

### Lighthouse Scores

Lighthouse testing was carried out in Google chrome, all the pages had similar scores of slightly under 90 performance
and around 78 on best practices which propably is linked to not implementing my own js. I apologize for it being in 
Swedish but its just wont change its language but the content is pretty clear anyway

---

![lighthouse score for the landing page](/docs/testing/ligtht_home.png)  
*The Home Page*

---

![lighthouse score for the reservaton page](/docs/testing/light_reserv.png)  
*The Reservation page*

---

![lighthouse score for log out page](/docs/testing/light_logout.png)  
*The log out page*

---



## Bugs

### Known Bugs

While going through the process of testing my app i ran accross this HTML errors:

![landing page HTML validation errors](/docs/testing/validationerror_html.png)