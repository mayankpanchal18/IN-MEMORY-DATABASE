# IN-MEMORY-DATABASE
This is my EHAX project. I made a simple key-value database using basic Python.

The program starts with an empty dictionary. I can enter commands to add, get, delete, and check data. I can also save the data to a JSON file and load it later using save and load commands.

In this project, I learned about the usage of the json library to save a dictionary to a file with "json.dump()" and load it back with "json.load()".

I also learned, exception handling in python in this project, in order to not get errors.
For ex:- KeyERROR --> If we perform DEL databey[key], but there is no such key, the we will face this error.
The solution was, I used "If key in Database" , and in else statment, i wrote key not found.
