# **Testing**

This is the TESTING file for the [Restaurant Booking](https://restaurant-booking-systems-c7e901b3d3c6.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## **Testing Contents**
  
- [Testing](#testing)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
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

## **Manual Testing**

# AAADDDD


### Site Responsivity

# AAADDDD

### Browser Compatibility

The Restaurant was tested on the browsers below. No issues were encountered on any of the platforms used.

| Browser                 | Issues | Functionality                   |
|-------------------------|--------|---------------------------------|
| Chrome v123.0.0.0       | none   | ✔️ good         |
| FireFox v132.0          | none   | ✔️ good         |
| Edge v131.0.2903.9      | none   | ✔️ good         |
| Samsung Internet v25.0  | none   | ✔️ good         |


### Testing User Stories

User stories can be reviewed in the Restaurant Booking [GitHub project board]. User stories have been numbered according to how they appear on the project board. Testing was carried out by myself, but also colleagues, friends, and family.

| User Story                 | Acceptance Criteria Met?  | Tested | Response     | Pass/Fail | Fix     |
|----------------------------|---------------------------|--------|--------------|-----------|---------|
| -    |      Epic: Admin                 |   - |  -  |   -  | -   |
| #11 Manage table bookings   | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #18 Search games and add to library | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #6 Events CRUD              | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #12 Manage Library            | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #7 Event drafts  | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #8 Approve comments        | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #14 Review suggestions   | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| -    |           Epic: User Interaction            |  -  | -   |   -  |  -  |
| #10 Make a booking         | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #3 View comments          | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #5 Modify or delete comments | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| -    |         Epic: Navigation              |   - | -   | -    |  -  |
| #1 Event pagination  | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #2 Event details         | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #16 View landing page       | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| #13 View games library         | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
| -    |         Epic: Log in / Register              |  -  |  -  |   -  | -   |
| #4 Register account      | ✔️ Yes                       | Yes    | No issues    | Pass      |    -    |
             

---



## Bugs

### Known Bugs

While going through the process of testing my app i ran accross this HTML errors:

![landing page HTML validation errors](/docs/testing/validationerror_html.png)