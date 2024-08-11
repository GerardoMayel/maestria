appointments = LOAD 'appointments.csv' USING PigStorage(',') AS (PatientID:chararray, AppointmentID:chararray, Gender:chararray, Age:int, Neighbourhood:chararray, Scholarship:int, Disease:chararray, SMS_received:int, ScheduledYear:int, ScheduledMonth:chararray, ScheduledDay:int, ScheduledHour:int, ScheduledMinute:int, AppointmentYear:int, AppointmentMonth:chararray, AppointmentDay:int, AppointmentDayOfWeek:chararray, No_show:chararray);

grouped = GROUP appointments BY (Disease, No_show);
summary = FOREACH grouped GENERATE FLATTEN(group) AS (Disease, No_show), COUNT(appointments) AS Count;

DUMP summary;
