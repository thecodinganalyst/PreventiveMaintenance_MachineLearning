# Preventive Maintenance Modeling Practise

This is a sample project used to practise machine learning with data from https://github.com/microsoft/SQL-Server-R-Services-Samples/tree/master/PredictiveMaintenanceModelingGuide/Data. In order to run the files, the respective data csv files (telemetry.csv, failures.csv, machines.csv, maint.csv, errors.csv) need to be downloaded from the above github directory and copied into a "data" folder.

## Input data overview:

Telemetry.csv: The telemetry time-series data consists of voltage, rotation, pressure and vibration measurements.

Errors.csv: The error logs contain non-breaking errors thrown while the machine is still operational and do not qualify as failures. The error date and times are rounded to the closest hour since the telemetry data is collected at an hourly rate.

Maint.csv: The scheduled and unscheduled maintenance records which correspond to both regular inspection of components as well as failures. A record is generated if a component is replaced during the scheduled inspection or replaced due to a break down.

Machines.csv: This data set includes machine model and age in years in service.

Failures.csv: These are the records of component replacements due to failures. Each record has a date and time, machine ID and failed component type associated with it.

## Code Structure

pm_telemetry.py is the helper function, which is a class by itself, to read the telemetry data and merge the other features/targets.

test_pm_telemetry.py is the test for pm_telemetry, use it to ensure the functions in pm_telemetry is running correctly. 

Each python file is a meant to do just 1 analysis/model/graph, and is named according to what they should function. Other than the pm_telemetry.py and test_pm_telemetry, the other files are meant to be run individually when desired. 

