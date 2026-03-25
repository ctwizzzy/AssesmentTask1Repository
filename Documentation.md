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

## Design: 

### Data Dictionary:

- city: Name of the city entered by the user
- temp: Temperature of the city measured in degrees celcius
- humidity: Humidity percentage of the city
- weather: description of the weather condition of the chosen city

### Structure Chart: 

- 

