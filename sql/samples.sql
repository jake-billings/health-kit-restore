select datetime(samples.start_date+978307200,'unixepoch','localtime') as "Start Date", datetime(samples.end_date+978307200,'unixepoch','localtime') as "End Date", 
samples.data_id, data_type, quantity, original_quantity, unit_strings.unit_string from samples
left outer join quantity_samples on samples.data_id = quantity_samples.data_id
left outer join unit_strings on quantity_samples.original_unit = unit_strings.RowID
left outer join objects on samples.data_id = objects.data_id
left outer join data_provenances on objects.provenance = data_provenances.RowID
where "Start Date" like '%2016-04-03'