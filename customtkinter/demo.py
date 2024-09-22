import customtkinter as ctk

# Khởi tạo ứng dụng
app = ctk.CTk()
app.title("cybersoft")
app.geometry("800x600")  # Kích thước cửa sổ

#bài 1 pack()
# top_frame = ctk.CTkFrame(master=app)
# top_frame.pack(side="top", fill="both", expand=True)

# frame1 = ctk.CTkFrame(master=top_frame, fg_color="yellow")
# frame1.pack(side="left", fill="both", expand=True)

# frame2 = ctk.CTkFrame(master=top_frame, fg_color="red")
# frame2.pack(side="left", fill="both", expand=True)

# bottom_frame = ctk.CTkFrame(master=app)
# bottom_frame.pack(side="top", fill="both", expand=True)

# frame3 = ctk.CTkFrame(master=bottom_frame, fg_color="gray")
# frame3.pack(side="left", fill="both", expand=True)

# frame4 = ctk.CTkFrame(master=bottom_frame, fg_color="blue")
# frame4.pack(side="left", fill="both", expand=True)


#bài 2 grid
# app.grid_rowconfigure((0, 1), weight=1)  # Đảm bảo hàng 0 và 1 giãn đều
# app.grid_columnconfigure((0, 1), weight=1)  # Đảm bảo cột 0 và 1 giãn đều


# frame1 = ctk.CTkFrame(master=app, fg_color="yellow")
# frame1.grid(row=0, column=0, sticky="nsew")

# frame2 = ctk.CTkFrame(master=app, fg_color="red")
# frame2.grid(row=0, column=1, sticky="nsew")

# frame3 = ctk.CTkFrame(master=app, fg_color="gray")
# frame3.grid(row=1, column=0, sticky="nsew")

# frame4 = ctk.CTkFrame(master=app, fg_color="blue")
# frame4.grid(row=1, column=1, sticky="nsew")


# bài 3 place()
frame1 = ctk.CTkFrame(master=app, fg_color="yellow")
frame1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

frame2 = ctk.CTkFrame(master=app, fg_color="red")
frame2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

frame3 = ctk.CTkFrame(master=app, fg_color="gray")
frame3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)

frame4 = ctk.CTkFrame(master=app, fg_color="blue")
frame4.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)


# Chạy ứng dụng
app.mainloop()
