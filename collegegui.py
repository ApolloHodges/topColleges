from colleges import Colleges
import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class MainWindow:
    TOPNUM = 15

    def __init__(self):
        try:
            self.topColleges = Colleges()
        except IOError as e:
            tkmb.showerror("Error", e, parent = master)
            exit()


        self.win = tk.Tk()
        self.win.minsize(300, 120)
        self.win.title("Top Colleges")
        CT = tk.Label(self.win, text="College Lookup", fg="blue")
        CT.grid(row=0, column=1, pady=10, sticky='n')
        cost_button = tk.Button(self.win, text="By Cost", command = lambda : self.cost_graph())
        cost_button.grid(row=2, column=0, pady=10, padx=30)

        data_button = tk.Button(self.win, text="By Data", command = lambda : self.data_graph())
        data_button.grid(row=2, column=1, padx=30)

        sal_button = tk.Button(self.win, text="By Salary", command = lambda : self.sal_graph())
        sal_button.grid(row=2, column=2, padx=30)
        # topColleges.rankComp("Student Population")

        CT = tk.Label(self.win, text="College Lookup", fg="blue")
        CT = tk.Label(self.win, text="College Lookup", fg="blue")

        mean_cost = tk.StringVar()
        cost = self.topColleges.getCost()
        mean_cost.set(f"Mean Total Annual Cost : {cost[0]}, standard deviation: {cost[1]}")

        mean_SAT = tk.StringVar()
        SAT = self.topColleges.getSAT()
        mean_SAT.set(f"Mean SAT Lower: {SAT[0]}, standard deviation: {SAT[1]}")

        mean_ACT = tk.StringVar()
        ACT = self.topColleges.getACT()
        mean_ACT.set(f"Mean ACT Lower: {ACT[0]}, standard deviation: {ACT[1]}")

        cost_label = tk.Label(self.win, textvariable=mean_cost)
        cost_label.grid(row=3, column=0, pady=2, sticky='w', columnspan=3)

        SAT_label = tk.Label(self.win, textvariable=mean_SAT)
        SAT_label.grid(row=4, column=0, pady=2, sticky='w', columnspan=3)

        ACT_label = tk.Label(self.win, textvariable=mean_ACT)
        ACT_label.grid(row=5, column=0, pady=2, sticky='w', columnspan=3)

        self.win.mainloop()

    def cost_graph(self):
        fig = plt.figure()
        self.topColleges.costDist()
        plt_win = PlotWindow(fig)

    def sal_graph(self):
        fig = plt.figure()
        self.topColleges.bestSal(self.TOPNUM)
        plt_win = PlotWindow(fig)

    def data_graph(self):
        dw = DialogWindow(self.win, self.topColleges.getHeader())
        self.win.wait_window(dw)
        selection = dw.getChoice()
        if selection:
            fig = plt.figure()
            self.topColleges.rankComp(selection)
            plt_win = PlotWindow(fig)


class PlotWindow(tk.Toplevel):

    def __init__(self, fig):  # master):
        self.win = tk.Toplevel()
        canvas = FigureCanvasTkAgg(fig, master=self.win)
        canvas.get_tk_widget().grid()
        canvas.draw()

class DialogWindow(tk.Toplevel):
    def __init__(self, master, buttons):
        self.master = master
        super().__init__(master)
        # self.data_radio = tk.Toplevel(self.master)
        self.choice = ""
        var = tk.StringVar()
        for item in buttons:
            button = tk.Radiobutton(self, text=item, variable=var, value=item, command=lambda: self.setChoice(var.get()))
            button.grid(sticky='w')

            var.set(buttons[0])

        finish = tk.Button(self, text="ok", command= lambda : self.destroy())
        finish.grid(sticky='s')

    def setChoice(self, choice):
            self.choice = choice

    def getChoice(self):
            return self.choice








a = MainWindow()
a.data_graph()




