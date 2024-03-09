# StageLeft Merchandise

StageLeft Mercahndise is a merchandise management service for bands and artists, taking the responsibility away from them, allowing them to concentrate on their music. The business in its entirety is based around a more complex and involved model, however the online side of the venture is a business to consumer (B2C) e-commerce site aimed at exisiting fans of the musicians that StageLeft work with.

![StageLeft am I responsive image](docs/stage-left-am-i-responsive.png)

[Live deployment link](https://stage-left-merch-6e2378b5745e.herokuapp.com/)

## Planning and Agile Methodology

At the beginning of the planning process it was decided that an agile approach would be taken during development. This meant that effort would be focued on smaller individual pieces, rather than the puzzle as a whole, allowing for clean delivery of each section until the puzzle is complete. This compartmentalisation of the project allowed for large laborious aspects to be broken down into much smaller, manageable tasks. These tasks were derived from the 10 user stories collected before development:

- Create a draft product
- Shopping basket
- Open a product
- Checkout
- Contact form
- View list of products
- Testimonials
- Mailing list
- User account
- Privacy

Due to the agile method of development, as the process moved forward the goal posts often changed, so the certain aspects of the current iteration of the project may not perfectly reflect the resepctive user story. These aspects will be explained in more details in the features section further on in the documentation.

For further information regarding the initial user stories, please visit the [GitHub Project](https://github.com/users/KitLavis/projects/5/views/1).

### E-Commerce Business Model

As mentioned in the intorductory paragraph, although the company offers more complex and involved services to the bands and artists themselves, the online aspect of StageLeft Merchandise follows a business to consumer (B2C) e-commerce business model. This means that the business (StageLeft) sells products directly to consumers i.e. fans of the artists that the business works with.

### SEO

An important feature of any online business in 2024 is search engine optimisation (SEO), as you can't sell products to people if they don't seem. Therefore a number of items were added to improve StageLeft's "online rating". The simplest and most obvious of these aspects are the keywords in the meta tags within the head element of the base HTML template. As well as these keywords, everything written at the top of a page, within header tags, or within strong tags had thought put in to them so as not to waste the oppurtunity to improve the site's SEO. The final aspect of SEO are the sitemap and robots files. The sitemap.xml file is a list of all the pages of the site that can be accessed without logging in, while the robots.txt file tells search engine crawlers where they can't crawl. Although the robots.txt file tells search engines where not to go, the presence of the file itself gives the page a higher rating as it is acknowledging that search engines can crawl your site in the first place.

### Design

The design elements were kept as minimal as possible while still portraying the aim of the project, and as can be seen in features section, they are kept consistent throughout the majority of the site. The hero image of an audience watching a live act is used as the base on every page, while the elements overlaying this image use utilise simple black and white backgrounds with the opacity lowered slightly to allow for the underlying image to be seen.

Hero Image:

![Hero image](static/images/hero-image.webp)

Colour Swatch:

![Colour swatch with hex values](docs/stage-left-swatch-hex.png)

Wireframes:

- All Products:

![All products page wireframe](docs/all-products.png)

- Product Detail:

![Product detail page wireframe](docs/product-detail.png)

## Features

### Base Template and Consistent Features

As well as the overriding design aspects, there are two features that remain consistent across all pages. These are the header and footer. The header consists of a top banner with the company name, and a secondary navigation panel where the user can navigate to the specific product or artist pages, and the testimonials section. The right hand side of the bar holds the user profile links, accessable via a dropdown menu attached to the user icon, as well as the basket icon that links to the basket page. Underneath the basket icon the current order total is shown, so the user does not have to navigate to their basket to keep track of their order. On the opposite side of the navigation bar the user can enter a specific keyword in order to search through all the products and filter what is relevant to them. On smaller devices the navigation bar is collapsed into a burger icon so that the page is not over cluttered.

![Header/nav bar](docs/header.png)

The footer consists of a number of links that are also present in the navigation bar, as well as a link to the contact page, a mailing list sign up box, and a link to the privacy policy.

![Footer](docs/footer.png)

### Home

### Products

### Basket

### Checkout

### Artists

### User

### Contact

## Development and Deployment

### Tools and Technologies

## Testing and Validation

### Code Validation

### Manual Testing

## Challenges and Bugs

- Cloudinary media files
- Database foregin key
- Checkout duplicate orders

## Credits

### Code Content

### Media and Site Content