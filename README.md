# Ecommerce

Project name Ecommerce                                  
Customer - This Django app provides a REST API for managing Customers,Products and Orders in the Ecommerce platform
 
INSTALLATION

Clone the repository: https://github.com/sharuhaasan/Ecommerce                                                         
Navigate to the project directory: cd Ecommerce                                                                             
Create a virtual environment: python3 -m venv venv                                                                 
Activate the virtual environment: venv\Scripts\activate                                                              
Install the dependencies: pip install -r requirements.txt                                                
Set up the database: python manage.py makemigrations and python manage.py migrate                                  

USAGE

settings.py                                                                              
models.py                                                                              
serializers.py                                                                                       
views.py                                                                                        
urls.py                                                                                       

Start the development server:    python manage.py runserver                       

Access the API endpoints:                                                                

Create New Customer: POST /api/customers/                                      
List All Customers: GET /api/customers/                                                      
Update Existing Customer: PUT /api/customers/<id>/                                        

Create New Product: POST /api/products/                                                       
List All Products: GET /api/products/                                                  

Create New Order: POST /api/orders/                                                  
List All Orders: GET /api/orders/                                                 
Update Existing Order: PUT /api/orders/<id>/                                             
List Order based on the Products: GET /api/orders/?products=Laptop                                              
List Order based on the Customer: GET /api/orders/?customer=Sharu                                                

SAMPLE API

http://127.0.0.1:8000/api/orders/  --  (POST) To create new order                                            
http://127.0.0.1:8000/api/orders/?customer=sharuu  -- (GET) List of order based on customer name                      
http://127.0.0.1:8000/api/products/  --  (GET) Lists all existing products                                   
http://127.0.0.1:8000/api/customers/1/  --  (PUT) To update the details of existing customer using customer id                    

DATABASE : I have used the MySQL database to check if the table values are filled.
