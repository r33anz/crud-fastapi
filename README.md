# crud-fastapp

This is a CRUD where I'm using the desisng pattern Repository
The repositories that I'm using are two, one saving data in a
Postgresql database and the other in the CSV file (crud-fastapi/src/data/task.csv)
Ypu can see this process in dependecies.py

I simulate a down sql server(stop the server  process) so when it's happens
the system automacitlly saves the data in the CSV file

You can run the migrations with the next commands: 
    alembic upgrade head

In the .env.example you can configurate your enviroment variables

Virtual Env Activation 
run this command in your terminal:    crud-fastapi\Scripts\activate
run this to exit to the virtual env:  deactivate
run the serve :                       uvicorn app:app 