import schedule
import time
from retriever import get_catalogue
from retriever import get_records
from processor import process

schedule.every().hour.at(":44").do(get_records)
schedule.every().hour.at(":45").do(get_catalogue)
schedule.every().hour.at(":46").do(process)

print('MX-COVID bot alive and running!')
while True:
    schedule.run_pending()
    time.sleep(1)
