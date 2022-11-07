## Recyclops Backend Application 
   Encapsulates the backend structure of the app,
   along with code examples for basic functionality. This read me will contain additional 
   info on testing and setting up a local SQL server

## Configuring A MySQL Server
   
   To configure a server, open up a terminal and 
   do the following. 

   * Commands:
      - To install mySQL run: **'sudo apt install mysql-server'**
      - Starting the server on your local:  **'sudo systemctl start mysql'** 
      - Invoking mySQL: **'sudo mysql -u root'** This will log you as the 
        root user with no password. One can be set up at a later time for 
        our purposes. You will then be prompted with the 
        mySQL shell 
      - To create a user issue the following:
        **'CREATE USER 'asap'@'localhost' IDENTIFIED BY '$PokerCh1p1234';**
        where 'asap' is the username and '$PokerCh1p1234' is the password. 
      - To create the database: **'CREATE DATABASE recyclops;'**
      - We then need to grant the user with permissions: 
        **'GRANT ALL ON recyclops.\* To 'asap'@'localhost' WITH GRANT OPTION;'**
      - To change the database: **'USE recyclops;'**
      - To create the 'centers' table: **'CREATE TABLE 
         centers(material VARCHAR(255) NOT NULL, 
         center_name VARCHAR(255) NOT NULL, 
         longitude FLOAT(53) NOT NULL,
         latitude FLOAT(53) NOT NULL),
         PRIMARY KEY ( material ));'**
      - You are now all set to run the application.

## Testing
* '/getLocations' endpoint: **'curl -X GET 
   http://127.0.0.1:5000/getLocations?material={material}'**
* /insertTable **'curl -X POST http://127.0.0.1:5000/insertTable'**
