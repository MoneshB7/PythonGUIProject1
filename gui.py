import tkinter as tk
import socket
import uuid
window=tk.Tk()
window.title("System Details - A Monesh B Production")
window.geometry("300x300")
hostname=socket.gethostname()
ipaddr=socket.gethostbyname(hostname)
title = tk.Label(text="Hostname "+str(hostname))
title.grid(column=0,row=1)
title = tk.Label(text="IP Address "+str(ipaddr))
title.grid(column=0,row=3)
title = tk.Label(text="MAC Address "+str(uuid.getnode()))
title.grid(column=0,row=5)
title = tk.Label(text="Developed by Monesh B - 2019")
title.grid(column=0,row=7)
window.mainloop()
