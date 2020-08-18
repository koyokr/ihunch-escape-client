import notify
import time

class Notify:
	def __init__(self):
		notify.init('../resource/app_icon.ico', 0)
	
	def notify(title, body, *s_time):
		notify.init('../resource/app_icon.ico', 0)
		notify.notify(body, title, '../resource/app_icon.ico', False, 3, notify.dwInfoFlags.NIIF_USER | notify.dwInfoFlags.NIIF_LARGE_ICON)

		if s_time:
			time.sleep(s_time[0])

		notify.uninit()