Your Data Asset will connect to all files that match the regex that you provide.  Each matched file will become a Batch inside your Data Asset.

For example:

Let's say that your Azure Blob Storage container has the following files:
- "yellow_tripdata_sample_2021-11.csv"
- "yellow_tripdata_sample_2021-12.csv"
- "yellow_tripdata_sample_2023-01.csv"

If you define a Data Asset using the full file name with no regex groups, such as `"yellow_tripdata_sample_2023-01\.csv"` your Data Asset will contain only one Batch, which will correspond to that file.

However, if you define a partial file name with a regex group, such as `"yellow_tripdata_sample_(?P<year>\d{4})-(?P<month>\d{2})\.csv"` your Data Asset will contain 3 Batches, one corresponding to each matched file.  You can then use the keys `year` and `month` to indicate exactly which file you want to request from the available Batches.