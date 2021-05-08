import schedule
import time
from retriever import get_catalogue
from retriever import get_records
from processor import process

schedule.every().day.at("02:01").do(get_records)
schedule.every().day.at("02:02").do(get_catalogue)
schedule.every().day.at("02:03").do(process)

print('MX-COVID bot alive and running!')
while True:
    schedule.run_pending()
    time.sleep(1)