appointments = LOAD 'appointments.csv' USING PigStorage(',') AS (PatientID:chararray, AppointmentID:chararray, Gender:chararray, Age:int, Neighbourhood:chararray, Scholarship:int, Disease:chararray, SMS_received:int, ScheduledYear:int, ScheduledMonth:chararray, ScheduledDay:int, ScheduledHour:int, ScheduledMinute:int, AppointmentYear:int, AppointmentMonth:chararray, AppointmentDay:int, AppointmentDayOfWeek:chararray, No_show:chararray);

disease_counts = GROUP appointments BY Disease;
disease_summary = FOREACH disease_counts GENERATE group AS Disease, COUNT(appointments) AS Count;

DUMP disease_summary;
