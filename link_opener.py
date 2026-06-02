# Text Editor

from tkinter import*
import webbrowser



# اولا انشاء نافذة
root =Tk()

# # ثانيا انشاء عنوان + حجم الشاشة
root.title('Simple Link Opener')
root.geometry("400x200")

root.config(bg="#e6f3ff")

# # هذي دالة عشان اللينك
def open_link():
  link = entry.get().strip()
  if not link:
        result_label.config(text="Please enter a link!", fg="red")
        return
  webbrowser.open(link)
  result_label.config(text="Link opened successfully!", fg="green")


#  العنوان
mylabel=Label(root,text="Welcome To My App!",font='arial 20 bold')
# وبعدين احدد كيف بيكون عرضها
mylabel.pack(pady=40)


# إدخال الرابط
entry= Entry(root,width=50)
entry.pack(pady=20)

# زر الفتح
btn = Button(root,text="Open Link",bg="yellow",command=open_link)
btn.pack(pady=10)

# رسالة النتيجة
result_label = Label(root, text="", bg="#e6f3ff")
result_label.pack(pady=10)

# تحسين الألوان
root.config(bg="#e6f3ff")
mylabel.config(bg="#e6f3ff", fg="#003366")
btn.config(bg="#ffd966")

# تشغيل البرنامج
root.mainloop()








