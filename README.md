# RemindMe
  Web application that sends a text message using Twilio API at a certain time in either a week, day, hour, or minute as a quick reminder to do certain things. Implements MongoDB to store the phone number of someone, the delay rate, and the actual message to send. Implements two scripts, one to run the server to store new items within the database and another to continuously check the existing database if one of the reminders have "expired." 

>mongo
>show databases
>use <database>
>show collections
>db.<collection>.find()
