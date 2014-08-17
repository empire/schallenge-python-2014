Question 4-Ip-Location
Python 2.7
Ubuntu 14.04
hossein.zolfi@gmail.com

برای اجرای برنامه دستورات زیر را اجرا می کنیم
source python-lib/bin/activate
python app.py

ممکن است برنامه اجرای برنامه به علت فراخوانی طول بکشد.
برای استفاده از این سرویس به صورت زیر عمل می کنیم.
from lib.geoipserverice import get_geo_ip
print get_geo_ip('4.2.2.4')

برنامه خطاهای urllib2.URLError, socket.timeout را مدیریت می کند و اگر خطایی اتفاق بیفتد در جواب None بر می گرداند و اگر اشکالی پیش نیاید نام کشور به عنوان خروجی برگردانده می شود. خطاهای دیگر بدون گرفته شدن ارسال خواهند شد.
برای بررسی اجرای برنامه می توانید از log استفاده کنید که به صورت زیر فعال می شود
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

برنامه به صورت تست شده آماده شده و تست ها در قسمت tests قرار دارند برای تست دستور زیر را اجرا می کنیم البته قبل از آن virtualenv را فعال می کنیم. در صورتی که فعال باشد نیازی به اجرای مجدد آن نیست.
source python-lib/bin/activate
py.test tests


طریقه نصب از ابتدا در لینوکس