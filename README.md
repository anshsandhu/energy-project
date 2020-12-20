Energy-project
Data science for energy systems final project




**Summary to Run:

Go to the folder: 'final-applying-ga-to-all-cities'
run: 'ga-on-normalised-data.pyn'

All the processes - data cleaning, data to electricity - have been condensed into a CSV file 'df_input_to_ga.csv'




**Decription of the process:

1. wind-solar-functions **(20 percent of the time)
    i. CSV file : contains wind power curves data
    ii. PYNB file : contains master wind and solar functions
    
2. screenshots-of-power-curve-wind
    i. JPEG file : contains wind power curves screenshot as found on the internet
    
3. final-applying-ga-to-all-cities **(40 percent of the time)
    i. combining-all-cities.pynb : first run this to create csv file named "combined-cities-dataset"
    ii. normalising-energy-data.pynb : run this to normalize data and obtain csv file named "df_input-to-ga"
    iii. ga-on-normalised-data.pynb : run this to perform genetic algorithm and get the required sizing of hybrid renewable system
    
4. cleaned-cities-dataframe-with-power-values
    i. CSV file : contains cities data along with the power values for each type of wind turbine and solar panel used
    
5. data-cleaning **(40 percent of the time)
    i. CSV files : contains various data cleaning files based on individual cities weather data
    ii. PYNB files : data cleaning: matching indices, removing leap year from weather data, tidying data into long form data,             removing NA, 0 values
    

    

