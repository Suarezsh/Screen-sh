import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import ImageGrab as ig
import time as t
import math as m

class CP(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Screen-Sh")
        self.overrideredirect(True)
        self.attributes('-topmost', True)

        r = 40
        w = r * 2
        h = r * 2

        sa = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = m.floor((sa - w) / 2)
        y = m.floor((sh - h) / 2)

        self.geometry(f"{w}x{h}+{x}+{y}")
        self.resizable(False, False)

        self.f = tk.Frame(self)
        self.f.pack(fill=tk.BOTH, expand=True)

        self.b_c = tk.Button(self.f, text="Capturar", width=8, command=self.dc_c, bg="#0F0", fg="#000")
        self.b_c.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.b_q = tk.Button(self.f, text="Cerrar", width=8, command=self.dc_q, bg="#F00", fg="#FFF")
        self.b_q.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.x = 0
        self.y = 0
        self.bind("<ButtonPress-1>", self.i_d)
        self.bind("<ButtonRelease-1>", self.d_d)
        self.bind("<B1-Motion>", self.d)

        self.c_c = 0
        self.u_c_c = 0
        self.c_q = 0
        self.u_c_q = 0
        self.t = 0.3

    def i_d(self, e):
        self.x = e.x
        self.y = e.y

    def d_d(self, e):
        self.x = None
        self.y = None

    def d(self, e):
        dx = e.x - self.x
        dy = e.y - self.y
        x = self.winfo_x() + dx
        y = self.winfo_y() + dy
        self.geometry(f"+{x}+{y}")

    def dc_c(self):
        t_a = t.time()
        if t_a - self.u_c_c < self.t:
            self.c_c += 1
        else:
            self.c_c = 1
        self.u_c_c = t_a

        if self.c_c == 2:
            self.o_v()
            self.c_c_p()
            self.m_v()
            self.c_c = 0

    def dc_q(self):
        t_a = t.time()
        if t_a - self.u_c_q < self.t:
            self.c_q += 1
        else:
            self.c_q = 1
        self.u_c_q = t_a

        if self.c_q == 2:
            self.c_c_q()
            self.c_q = 0

    def o_v(self):
        self.geometry("0x0")

    def m_v(self):
        self.geometry("100x100")

    def c_c_p(self):
        s = ig.grab()
        r = fd.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos de imagen", "*.png")])

        if not r:
            return

        s.save(r)
        print(f"Captura realizada y guardada como '{r}'.")

    def c_c_q(self):
        self.withdraw()
        r = mb.askyesno("Screen-Sh", "¿Seguro de cerrar?")
        self.deiconify()
        if r:
            self.destroy()

if __name__ == "__main__":
    a = CP()
    a.mainloop()
