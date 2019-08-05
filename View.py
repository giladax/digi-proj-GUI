import tkinter as tk
from os import path, O_CREAT, O_RDWR
from tkinter import filedialog
from shutil import copyfile
import urllib

alphabet = 'אבגדהוזחטיכלמנסעפףצקרשת'


class popupWindow(object):
    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        self.l = tk.Label(top, text="Hello World")
        self.l.pack()
        self.e = tk.Entry(top)
        self.e.pack()
        self.b = tk.Button(top, text='Ok', command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()


class View:
    def __init__(self, fm, text_wrapper, height, width):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=height, width=width)
        self.background_image = tk.PhotoImage(file='landscape.png')
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        self.search_line = tk.Entry(self.frame, font="Palatino 20", justify=tk.RIGHT)
        self.search_button = tk.Button(self.frame, text="חפש ערכים", font="Palatino 16",
                                       command=lambda: self.list_search_results(
                                           self.fm.find_optional_matches(self.search_line.get())))

        self.browse_button = tk.Button(self.frame, text="חפש לפי אלפבית", font="Palatino 16",
                                       command=lambda: self.browse())

        self.download_button = tk.Button(self.frame, text="הורד מסמך", font="Palatino 16",
                                         command=lambda: self.download_curr_file())
        self.curr_file = ""

        self.canvas.pack()
        self.background_label.place(relwidth=1, relheight=1)
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
        self.search_line.place(relwidth=1, relheight=1)
        self.search_button.place(relx=0.15, relheight=1, relwidth=0.15)
        self.browse_button.place(relx=0, relheight=1, relwidth=0.15)

        self.lower_frame = None
        self.lb = None
        # self.browse_lb = None
        self.lower_frame_text = None
        self.fm = fm
        self.text_wrapper = text_wrapper

    def present_file_content(self, selection_event):
        w = selection_event.widget
        index = int(w.curselection()[0])
        file_name = w.get(index) + '.txt'

        self.curr_file = file_name
        file_content = self.fm.read_file(file_name)

        # Clear the listbox and replace with the chosen content
        self.lb.pack_forget()
        self.lower_frame_text.config(state=tk.NORMAL)
        self.lower_frame_text.delete('1.0', tk.END)
        self.lower_frame_text.tag_configure("right", justify='right')

        # Print each line.
        for line in file_content.split('\n'):
            # Wrap each line with predefined width
            word_list = self.text_wrapper.fill(text=line)
            self.lower_frame_text.insert(tk.END, word_list)
            self.lower_frame_text.insert(tk.END, '\n')

        self.lower_frame_text.tag_add("right", 1.0, "end")
        self.lower_frame_text.config(state=tk.DISABLED)

        scrollbar = tk.Scrollbar(self.lower_frame_text, orient=tk.VERTICAL, command=self.lower_frame_text.xview)
        scrollbar.place(rely=1)
        self.download_button.place(relx=0.30, relheight=1, relwidth=0.15)

    def list_search_results(self, search_results):
        # Set proper callback
        self.lb.bind('<<ListboxSelect>>', self.present_file_content)

        # Clear list box
        self.lb.delete(0, tk.END)

        for file_name in search_results:
            self.lb.insert(tk.END, file_name.replace('.txt', ''))

        self.lb.pack(side="right", fill="both", expand=True)

    def list_by_letter(self, selection_event):

        w = selection_event.widget
        index = int(w.curselection()[0])
        letter = w.get(index)

        files = self.fm.find_optional_matches_by_prefix(letter)

        # Set proper callback
        self.lb.bind('<<ListboxSelect>>', self.present_file_content)

        # Clear list box
        self.lb.delete(0, tk.END)

        for file in files:
            self.lb.insert(tk.END, file.replace('.txt', ''))

        self.lb.pack(side="right", fill="both", expand=True)

    def browse(self):
        self.lower_frame_text.delete('1.0', tk.END)
        self.download_button.forget()
        # Set proper callback
        self.lb.bind('<<ListboxSelect>>', self.list_by_letter)

        # Clear list box
        self.lb.delete(0, tk.END)

        for letter in alphabet:
            self.lb.insert(tk.END, self.text_wrapper.fill(letter))

        self.lb.pack(side="right", fill="both", expand=True)

    def init_view(self):
        self.lower_frame = tk.Frame(self.root, bg='#80c1ff')
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.6, anchor='n')

        self.lower_frame_text = tk.Text(self.lower_frame,
                                        font="Palatino 14", width=100, spacing1=0, spacing2=0, spacing3=0,
                                        borderwidth=0, wrap="none")
        self.lower_frame_text.place(relwidth=1, relheight=1)
        self.lower_frame_text.config(state=tk.DISABLED)

        self.lb = tk.Listbox(self.lower_frame_text, bd=0, font="Palatino 14")
        self.lb.configure(justify=tk.RIGHT)

        # self.browse_lb = tk.Listbox(self.lower_frame_text, bd=0, font="Palatino 14")
        # self.browse_lb.configure(justify=tk.RIGHT)
        self.root.mainloop()

    def popup(self):
        self.w = popupWindow(self.root)
        self.download_button["state"] = "disabled"
        self.root.wait_window(self.w.top)
        self.download_button["state"] = "normal"

    def download_curr_file(self):
        # self.popup()
        download_path = filedialog.askdirectory(parent=self.root, initialdir="/", title='Pick a directory')
        try:
            copyfile(path.join(self.fm.base_dir, self.curr_file), path.join(download_path, self.curr_file))
            copyfile(path.join(self.fm.base_dir, self.curr_file.replace("txt", "xml")),
                               path.join(download_path, self.curr_file.replace("txt", "xml")))
            # f = open(path.join(self.fm.base_dir, self.curr_file), "r", encoding="utf8")
            # new_text = open(path.erjoin(download_path, self.curr_file), "w+")
            # new_text.write(f.read(dsd))
            #
            # f.close()
            # new_text.close()
            #
            # f = open(path.join(self.fm.base_dir, self.curr_file.replace("txt", "xml")), "r", encoding="utf8")
            # new_xml = open(path.join(download_path, self.curr_file.replace("txt", "xml")), "w+")
            # new_xml.write("fsdds".encode("utf8"))
            #
            # f.close()
            # new_xml.close()
        except FileNotFoundError:
            pass
