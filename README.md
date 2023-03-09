# Indicium Tech Code Challenge

Code challenge for Software Developer with focus in data projects.
https://github.com/techindicium/code-challenge


## Setup of the project

You can clone this repository by using the command:

```
git clone https://github.com/AgnyFonseca/Northwind.git
```

After that you can enter the main directory of the project and start the docker container, once the container is up, check on the docker-compose.yml file the credentials for the northwind DB. This first container is running on port 5433.

```
docker-compose up
```

Once it's up, you can change the directory to "scripts".

```
cd scripts
```
Again run the docker-compose up command to run the second docker container. This second container is running on port 5434 and also for that you can find the indicium-northwind database credentials on the docker file. 

```
docker-compose up
```

When all containers are up to run, you can then test the python scripts "csv_writer_db" and "csv_writer_order_details". 


This first script will write all the data from the first database into csv's files. 

```
python csv_writer_db.py
```

The second script will save the original order_details csv file into a new csv which later we will use to save in the second DB.

```
python csv_writer_order_details.py
```   

After both these scripts are running, it should create a folder structure like this:
/data/csv/{table_name}/{YYYY-mm-dd}/table_name.csv

The last step is to run the "write_csv_to_db" script, which will extract all the data saved previously in the csv files, and insert into the indicium-northwind DB.

```
python write_csv_to_db.py
``` 


## Final considerations

I tried to simplify this challenge into small pieces to solve, trying to focus on the main goal of this challenge. Unfortunately, I was not able to fulfill all the requirements for this project, either not having enough time or enough knowledge for it. But, I'm glad about my final result, considering the fact that I'm not a Python developer. 
There are things that with time and experience I would like to improve in this project starting by adding error treatments, for example when we want to insert a value and the id already exists, in this case, we would update an existing reference and not insert a new one. Also automation by adding a batch process that would run every day at x time. These are all things that I have to learn, for now, it is as it is and I'm happy with my accomplishment.

Thank you for the invitation to this code challenge, it's always nice to practice and learn something new. 


