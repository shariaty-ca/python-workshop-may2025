from tkinter import *
import time , datetime , winsound
from threading import *

root = Tk()
root.geometry("350x250")

def threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_time)
        if current_time == set_time:
            print("Time To Wake up")
            winsound.PlaySound("E:/kargah/music.wav" , winsound.SND_ASYNC)



Label(root,text="Alarm Clock" , font=("italy 20 bold"),fg="red").pack(pady=20)
Label(root,text="Set Time",font=("italy 15 bold"),fg="blue").pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])

h_menu = OptionMenu(frame,hour,*hours)
h_menu.pack(side=LEFT)


minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59')
minute.set(minutes[0])

m_menu = OptionMenu(frame,minute,*minutes)
m_menu.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59')
second.set(seconds[0])

s_menu = OptionMenu(frame,second,*seconds)
s_menu.pack(side=LEFT)

Button(root,text="set Alarm", font=("italy 10"), fg="black",command=threading).pack(pady=10)

root.mainloop()