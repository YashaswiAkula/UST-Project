# Customer Support Ticketing System



#### Overview



###### The Customer Support Ticketing System is a desktop application designed to streamline customer support operations. It provides a simple and intuitive interface for users to create, manage, and track support tickets.



#### Features



* ###### **User Management**: Allows registration and login with role-based access (Admin and User).

###### 

* ###### **Ticket Management**: Users can submit tickets, while admins can view, update, and close them.

###### 

* ###### **Desktop GUI**: Built using Tkinter, providing a user-friendly interface without needing a web browser.

###### 

* ###### **Database Integration:** Uses SQLite for storing all user and ticket information locally, ensuring lightweight and fast operations.

###### 

* ###### **Easy to Use:** Designed for small to medium-sized teams or businesses that want a simple, offline ticket tracking system.



#### Tech Stack



###### - Frontend / GUI:Python Tkinter

###### - Backend / LogicPython

###### - Database:SQLite

###### - Version Control: Git \& GitHub





#### Project Structure



PROJECT-CUSTOMER-TICKET/

│

├── app/        

│   ├── \_\_init\_\_.py

│   ├── app.py                  

│   ├── auth.py                

│   ├── users.py               

│   ├── allocation.py          

│   ├── analytics.py             

│   ├── database.py

│   ├── models.py               

│   ├── schemas.py               

│   ├── permissions.py           

│   ├── demo\_roles.py            

│   └── tickets.db              

├── frontend/                    

│   ├── main.py

│   ├── api\_client.py

│   ├── theme.py

│   ├── utils.py

│   ├── auth\_ui.py

│   ├── admin\_ui.py

│   ├── helper\_ui.py

│   ├── customer\_ui.py

│   └── comments\_ui.py

│

├── tests/                      

│   ├── \_\_pycache\_\_

│   ├── conftest.py

│   ├── test\_allocation.py

│   ├── test\_api.py

│    ├── test\_permissions.py

│    ├── test\_users.py

│   └── test\_database.py

│

├── requirements.txt

└── README.md





#### Installation \& Setup



##### 1\. Create Virtual Environment



###### &nbsp;       python -m venv venv

###### &nbsp;       source venv/bin/activate   # Linux/Mac

###### &nbsp;       venv\\Scripts\\activate      # Windows





##### 2\. Install Dependencies



###### &nbsp;       pip install -r requirements.txt





##### 3\. Run the Application



###### &nbsp;     python app/main.py





#### Application Functionality



* ###### User Management:

&nbsp;       - User registration and login

&nbsp;       - Role-based access (Admin / User)



* ###### Ticket Management:

&nbsp;        - Create new support tickets

&nbsp;        - View existing tickets

&nbsp;        - Update ticket status

&nbsp;        - Close resolved tickets



* ###### &nbsp;Data Storage:

&nbsp;        - All data is stored locally using SQLite

&nbsp;        - No external APIs or HTTP requests are used



* ###### Interface:

&nbsp;      - Desktop-based graphical user interface built with Tkinter

&nbsp;      - All operations are performed through the GUI





#### View Records 



###### \- Users can view all previously created support tickets from the application interface.

###### \- Admin users can view all tickets submitted by different users.

###### \- Tickets are fetched directly from the \*\*SQLite database\*\*.

###### \- No HTTP requests or REST APIs are involved.



#### Search and Filter Tickets



###### \- Users can search support tickets using keywords such as:

###### &nbsp; - Ticket title

###### &nbsp; - Ticket description

###### &nbsp; - Ticket status

###### \- Admin users can filter tickets based on:

###### &nbsp; - User

###### &nbsp; - Status (Open / In Progress / Closed)

###### \- Search operations are performed directly on the SQLite database.

###### \- Results are displayed in the Tkinter GUI.





#### Ticket History and Status Tracking



###### \- Each support ticket maintains its current status (Open, In Progress, Closed).

###### \- Updates to tickets are stored in the SQLite database.

###### \- Admin users can view ticket details and track status changes.

###### \- All ticket information is accessed directly through the Tkinter GUI.



#### View Ticket Details



###### \- Users can view complete details of a support ticket from the application interface.

###### \- Ticket information includes title, description, status, and created date.

###### \- All data is stored and retrieved from the SQLite database.

###### \- File downloads and document versioning are not implemented

###### 

#### Database Schema

###### 

##### &nbsp;Users Table

###### \- id: Primary key

###### \- username: User name

###### \- email: User email

###### \- password: Hashed password

###### \- role: User role (Admin / User)

###### 

##### Tickets Table

###### \- id: Primary key

###### \- title: Ticket title

###### \- description: Issue description

###### \- status: Ticket status (Open, In Progress, Closed)

###### \- created\_at: Ticket creation timestamp

###### \- user\_id: Foreign key referencing Users table





#### Data Storage

###### \- The application uses SQLite as a local database.

###### \- All user and ticket information is stored in database tables.

###### \- No external file storage or document uploads are implemented.

###### \- The system is designed for lightweight, local usage.

###### 

#### Security Features



###### \- User authentication using username and password

###### \- Role-based access control (Admin and User)

###### \- Restricted access to ticket management based on user role

###### \- SQLite database access limited to the application

###### \- Input validation to prevent invalid or empty data entries





#### Testing



###### \- The application was tested manually using the Tkinter graphical user interface.

###### \- User workflows tested include:

###### &nbsp; - User registration and login

###### &nbsp; - Creating new support tickets

###### &nbsp; - Viewing existing tickets

###### &nbsp; - Updating ticket status

###### &nbsp; - Role-based access verification (Admin/User)

###### \- SQLite database entries were verified to ensure correct data storage and retrieval.





#### Configuration



###### \- The application uses SQLite  as the default database.

###### \- Database file is created locally when the application runs.

###### \- No external configuration files are required.

###### \- All settings are handled within the Python source code.

###### 



#### Future Enhancements



###### \- Improved user authentication and authorization

###### \- Enhanced role-based access control

###### \- Ticket priority levels (High, Medium, Low)

###### \- Email notifications for ticket updates

###### \- Search and filter improvements

###### \- Report generation for admin users

###### \- Improved UI design using advanced Tkinter widgets





#### License



###### This project is open source and available for educational and learning purposes.

###### 



