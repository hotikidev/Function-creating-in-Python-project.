# HELLO GUYS IM WRITING A DEFINATIONAL ( Function Creating) PROJECT HOPE YOU LIKE IT ╰(*°▽°*)╯

# Reporting lengh but its enterable ( INPUT ) ■
def report_lengh():
    wordr = input('Enter the word : ')
    reporting__ = len(wordr)
    print(f'Lengh Equals ➡️  {reporting__}')
report_lengh()
# Save the documents to an directory quick and direct ^_^
import os as hotikidev # For being sure╰(*°▽°*)╯
def save_docs_to_an_DATAbase():
    saverw1 = input('Ok now enter datas to save on TXT file. : ')
    saver__ = open('data.txt','a')
    saver__.write(saverw1)

save_docs_to_an_DATAbase()
# Save the documents to an directory quick and direct 5 times ( 5x ) ^_^
import os as hotikidev # For being sure╰(*°▽°*)╯
def save_docs_to_an_DATAbase():
        for i in range(5):
            saverw1 = input('Ok now enter datas to save on TXT file. : ')
            saver__ = open('data.txt','w')
        saver__.write(saverw1)

save_docs_to_an_DATAbase()

# A function that creates an page with an button and an entry automaticly╰(*°▽°*)╯
def auto_tkinter_gui_entbut():
    import tkinter
    Window_root_GUI = tkinter.Tk()
    Window_root_GUI.title('HOTIKIDEV ON GITHUB 😁')
    Window_root_GUI.geometry('670x560')
    Window_root_GUI.configure(bg='#24D6AE')
    enterable___ = tkinter.Entry(
        Window_root_GUI,
        font=('Arail')
    )
    enterable___.pack(padx=80)
    button = tkinter.Button(
    Window_root_GUI,
    text='writing this cool thing.😁',
    font=('Arial',25),
    bg='#00FF85'
    )
    button.pack(pady=50)
    Window_root_GUI.mainloop()
auto_tkinter_gui_entbut()



# =======================================CREATED WITH LOVE BY (@hotikidev)=====================================