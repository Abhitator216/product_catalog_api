E-commerce Product Catalog API<br>
This is a Python and Django-based API for managing an e-commerce product catalog. It provides endpoints for creating, updating, deleting, and searching for products in the catalog.
It is a simple user friendly API build to fulfill the requirement of the user.

Installation
1. Clone this repository to your local machine.
*
`git clone https://github.com/your_username/ecommerce-product-catalog.git`<br>
 

##API Endpoints<br><br>
`GET /api/v1/products/` - Retrieve a list of all products in the catalog.<br><br>
`GET /api/v1/products/{product_id}/` - Retrieve details for a specific product by ID.<br><br>
`POST /api/v1/products/` - Create a new product in the catalog. Requires a JSON payload containing the product details.<br><br>
`PUT /api/v1/products/{product_id}`/ - Update an existing product in the catalog. Requires a JSON payload containing the updated product details.<br><br>
`DELETE /api/v1/products/{product_id}/` - Delete a product from the catalog.<br><br>
`GET /api/v1/products/search/?query={search_query}` - Search for products by name, brand, or category. The search_query parameter should be the search string.<br><br>
##Sample JSON Payload<br><br>
When creating or updating a product, you should send a JSON payload in the request body containing the product details. Here's an example of what the payload should look like:
`{
    "name": "Product Name",
    "category": "Category Name",
    "brand_name": "Brand Name",
    "image": "path/to/image.jpg"
}`
