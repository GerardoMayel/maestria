appointments = LOAD 'appointments.csv' USING PigStorage(',') AS (PatientID:chararray, AppointmentID:chararray, Gender:chararray, Age:int, Neighbourhood:chararray, Scholarship:int, Disease:chararray, SMS_received:int, ScheduledYear:int, ScheduledMonth:chararray, ScheduledDay:int, ScheduledHour:int, ScheduledMinute:int, AppointmentYear:int, AppointmentMonth:chararray, AppointmentDay:int, AppointmentDayOfWeek:chararray, No_show:chararray);

grouped = GROUP appointments BY No_show;
average_age = FOREACH grouped GENERATE group AS No_show, AVG(appointments.Age) AS Average_Age;

DUMP average_age;
