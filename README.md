# mx-covid

## How it works?
This program retrieves public COVID information in Mexico stright from the goverment. The goverment submits a big .csv file, enclosed in a .zip file
with a separate file that contains what each column means. The information in the CSV is mostly normalized, but in this case we remove the normalization
using both files and add them to a local MongoDB instance. Using a scheduler, the program runs automatically each day, with no user interaction required.


## What's the point? 
I created this program as a school project, but I extended its usage a bit more with the automation and automatic file unzipping. My end goal for this program
is to run it for as long as COVID is relevant and then generate some information dashboards to see current and historical data on the pandemic.

## Next steps
This program processes the whole file each day, the file is over 5 million rows and growing, which generates slowness as the program checks if each row exists in the DB prior to it's insertion. An upgrade would be to retrieve all ID's in one go and then remove them from the local ID's in the program and only insert them when they don't exist in the query.

Also, we could implement a hashcheck for the file, so that it is updated at the same time as the public database is updated and not at a pre-determined time of day, as it currently happens.
