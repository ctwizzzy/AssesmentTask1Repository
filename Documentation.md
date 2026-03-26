## Requirements definition
The system is able to provide the user real-time weather information about the city they have input. The application should save past citites the user has inputted and also must create a city temperature graph when the user asks the system to. Finally, the system must give the option for the user to exit the program. 

### Functional requirements: 

- User is able to input a city of their choice
- The system is able to retreive weather data on the given city by the user
- The system displays the required weather information such as temperature, humidity and a description of the weather
- Using pandas they system is able to store the data of user inputs
- The system gives the user the ability to view their past searches 
- Using matplotlib, the system generates a temperature graph of the cities the user has inputted
- The user has the ability to exit the program whenever they choose

### Non-Functional Requirements:
 
- The user must feel the system is user friendly 
- The system should quickly respond an output to the users input
- The system must be reliable and not crash or have any errors

## Determining Specifications: 

### Functional Specifications:
| Function       |    Input         |     Process                | Output                            |
|----------------|------------------|----------------------------|-----------------------------------|
| Search Weather | Name of City     | Call the API               | Weather data of city              |
| Store History  | Data of weather  | Saves to list using Pandas | History is stored                 |
| View History   | No inputs        | Retreive the stored data   | User is able to view history      |
| Create Graph   | The stored data  | Uses Matplotlib to create  | City temperature graph is created |

### Non-Functional Specifications: 

- The API must respond to user inputs within a few seconds 
- The user interface must be simple and easy to navigate through
- The system must be able to respond to invalid inputs and fix errors
- The code must be well commented with explanations 
- The API key is stored in a secure manner

## Design: 

### Data Dictionary:

| Variable | Variable Type | Description                           |
|----------|---------------|---------------------------------------|
| city     | string        | The name of the city                  |
| temp     | float         | Value of temperature                  |
| humidity | integer       | percentage of humidity                |
| history  | DataFrame     | Storees the past searches of the user |

### Structure Chart: 

Main Program
1. retrieve_weather() 
2. save_weather_search()
3. weather_search_history()
4. create_temperature_graph()

### Pseudocode
Start
Display UI
Receive User Input

If Choice = 1
GET city 
CALL API
DISPLAY weather data
SAVE data

elif Choice = 2
GET weather_history.csv data
DISPLAY User history

elif Choice = 3 
READ data from csv file
CREATE city temperature graph

elif choice = 4 
EXIT program

else:
PRINT ("Invalid choice")

## Development: 

This application was developed using the Python programming language. The OpenWeatherMAp API hhad the purpose of retrieving real time data of the temperature of cities around the world. 

Four libraries were required to be used in the development of this API. These include:
- requests
- pandas
- matplotlib
- os

Attached in another file is a photo of my UI. 

## Integration: 

The OpenWeatherMap API integrated by using different Python libraries. These libraries include
- requests (used to send requests to the API)
- pandas (used to store the search history of the user)
- matplotlib (used to create the city temeprature graph)

The API returns weather data in a json format to allow specific weather data such as temperature, humidity and weather description to be extracted. 

## Testng: 

Test Case 1:
Input: City name which is valid
Output: Informsation about weather is dispalyed

Test Case 2: 
Input: View search hsitory
Output: Search history of user is displayed 

Test Case 3: 
Input: Generate City Temperature Graph 
Output: A graph with past cities that were searched up and their weather is displayed. 

Test Case 4: 
Input: Exit Program
Output: User exits the program

Test Case 5: 
Input: Invalid Choice
Output: Error message is displayed

Feedback from two students: 

Martin Han: I have tested Aarav's system and it performs very efficiently. It responds within seconds to user inputs and there are  no bugs within the system. 

Oscar Lou: Aarav's API system is to a high standard and responds to inputs very well. The UI is neat and easy to understand and there are a variety of options provided in the menu. 

## Maintenance: 

It is important to continue to maintain this application so that it continues to function well and stays useful over time. Due to the application relying on an external API and user input, many areas require constant maintenance. 

### Ongoing maintenance: 

- The API integration must be monitored regularly to ensure its compatibility as changes to the OpenWeatherMap API may occur which could potentially break the program. 
- The libraries used such as requests, pandas and matplotlib must be updated regularly to ensure security and performance. 
- The weather_history.csv file must be monitored regularly to prevent data corruption or excessive file size. 

### Bug fixing: 

- Future bugs may arise to sue to an invalid input by the user 
- Issues related to network such as timeouts or API downtime will require maintenance improvements and more frequent checks on the     program.

### Future Improvements: 

- Implementing a Graphical User Interface to improve usability and accesibility for users. 
- Improve the temeprature graph by allowing users to filter and compare cities of their choice. 
- Add more weather descriptions such as wind speed and information about the forecast. 

### Long-Term Enhancements: 

- Add the option for users to create accounts to allow a personalised search history.
- Expand the application to allow the support of multiple APIs for a variety of data sources. 
- Make the application a web-based system for better accessibility. 

### Strategies for Maintenance: 

- Regular updates to libraries.
- Testing after updates.
- Allowing users to give feedback to improove on the system further. 
