from dotenv import load_dotenv
import schedule
import time
from utils import convert_to_wat, get_database


load_dotenv()


wat_4 = convert_to_wat('13:59', 'Africa/Lagos')
schedule.every().day.at(str(wat_4.strftime('%H:%M'))).do(get_database)

wat_12 = convert_to_wat('12:00', 'Africa/Lagos')
schedule.every().day.at(str(wat_12.strftime('%H:%M'))).do(get_database)

wat_21 = convert_to_wat('21:00', 'Africa/Lagos')
schedule.every().day.at(str(wat_21.strftime('%H:%M'))).do(get_database)

while True:
    schedule.run_pending()
    time.sleep(1)