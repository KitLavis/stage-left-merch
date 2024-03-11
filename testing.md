This test script can be followed in order to manually test the site for any faults.

| Ref No | Testcase                          | Expected Result                                         | Test Result |
|--------|-----------------------------------|---------------------------------------------------------|-------------|
|        |**Home**                           |                                                         |             |
| 01     | Open the homepage                 | Homepage loads with the correct template and data       | Pass        |
|        | **Products**                      | Meet the team page loads with correct template and data |             |
| 02     | Open all products page            | Page loads with the correct template and data           | Pass        |
| 03     | Open a product                    | Page loads with the correct template and data           | Pass        |
| 04     | Add to basket                     | Product added to basket and total updated in nav bar    | Pass        |
| 05     | Change quanitity                  | Correct quantity is displayed and added to the basket   | Pass        |
| 06     | Add product                       | Form loads and submits and product is added to database | Pass        |
| 07     | Edit product                      | Form loads and submits and product details are updated  | Pass        |
| 08     | Delete product                    | Product removed from the site and the database          | Pass        |
| 11     | Search a keyword                  | All relevant products are shown                         | Pass        |
| 09     | Continue shopping                 | Button sends user back to the products page             | Pass        |
|        | **Basket**                        |                                                         |             |
| 11     | Open the basket via basket icon   | Basket loads with correct items and information present | Pass        |
| 12     | Modify product quantity           | Product quantity updated                                | Pass        |
| 13     | Remove product                    | Product removed from basket                             | Pass        |
| 14     | Continue shopping                 | Button sends user back to the products page             | Pass        |
| 15     | Secure checkout button            | Button sends user to the checkout page                  | Pass        |
|        | **User Account**                  |                                                         |             |
| 16     | Register a user with valid data   | Success, user is registered                             | Pass        |
| 17     | Register a user with invalid data | Unsuccessful, form loads again with data and errors     | Pass        |
| 18     | Login a user with valid data      | Success, user is logged in                              | Pass        |
| 19     | Login a user with invalid data    | Unsuccessful, form loads again with data and errors     | Pass        |
| 20     | Update deliery information.       | Delivery info updated and autofills at checkout         | Pass        |
|        | **Checkout**                      |                                                         |             |
| 21     | Open checkout page                | Page loads with the correct template and data           | Pass        |
| 22     | Save delivery information         | Delivery info saved and autofills form                  | Pass        |
| 23     | Checkout                          | Loading overlay shown and redirected to checkout success|             |
|        |                                   | Payment is processed and order appears in database      | Pass        |
|        | **Contact**                       |                                                         |             |
| 24     | Open the contact page             | Contact form and template load succesfully              | Pass        |
| 25     | Send a message                    | Form submits and message is created                     | Pass        |
| 26     | View all messages                 | Template loads and all messages are shown in table      | Pass        |
| 27     | View message                      | Message information loads successfully                  | Pass        |
|        | **Artists**                       |                                                         |             |
| 28     | Open all artists page             | Page loads with correct template and information        | Pass        |
| 29     | Open an artist detail page        | Page loads with correct template and information        | Pass        |
| 30     | Follow artist's products button   | Products page loads with correct template and info      | Pass        |
|        | **Login Required Pages**          | Must not be logged in as superuser                      |             |
| 31     | Open restricted page via link/url | Request fails, redirected home or warning message shown | Pass        |
|        | **Links**                         |                                                         |             |
| 32     | Open privacy policy link          | Success, policy opens correct web page in a new tab     | Pass        |

These tests are based on Kristyna Wach's test script for [Fantastic News](https://github.com/Cushione/fantastic-news/tree/main)