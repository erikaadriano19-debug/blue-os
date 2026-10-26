import tkinter as tk
from tkinter import messagebox
import datetime

# --- Setup Main PC Desktop Window ---
root = tk.Tk()
root.title("BlueOS PC Simulator")
root.geometry("600x800")
root.configure(bg="#0047ab")

wallet = {"balance": 150}
is_fullscreen = False

def toggle_fullscreen():
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes("-fullscreen", is_fullscreen)
    if is_fullscreen:
        fullscreen_btn.config(text="Exit Full OS", bg="#dc3545")
    else:
        fullscreen_btn.config(text="Full Screen OS", bg="#28a745")

# --- AUTO FULL SCREEN WINDOW CREATOR ---
def make_window(title_text, content_func):
    desktop_height = root.winfo_height() - 45
    desktop_width = root.winfo_width()
    
    if desktop_height <= 0: desktop_height = 700
    if desktop_width <= 0: desktop_width = 450

    win = tk.Frame(root, bg="#f0f0f0", bd=2, relief="raised")
    win.place(x=0, y=0, width=desktop_width, height=desktop_height)
    
    title_bar = tk.Frame(win, bg="#0056b3", height=35)
    title_bar.pack(fill="x", side="top")
    
    title_label = tk.Label(title_bar, text=title_text, bg="#0056b3", fg="white", font=("Arial", 11, "bold"))
    title_label.pack(side="left", padx=10, pady=5)
    
    close_btn = tk.Button(title_bar, text=" Close Window X ", bg="#ff4d4d", fg="white", bd=0, font=("Arial", 10, "bold"), command=win.destroy)
    close_btn.pack(side="right", padx=10, pady=2)
    
    body = tk.Frame(win, bg="#f0f0f0")
    body.pack(fill="both", expand=True, padx=15, pady=15)
    content_func(body)
def open_browser():
    def browse_action():
        search_query = search_entry.get().strip().lower()
        if search_query == "devmenu.com":
            for widget in browser_inner_frame.winfo_children(): widget.destroy()
            tk.Label(browser_inner_frame, text="⚡ MY SECRET DEVMENU ⚡", bg="#f0f0f0", fg="#0056b3", font=("Arial", 14, "bold")).pack(pady=10)
            def add_money():
                wallet["balance"] += 500
                wallet_label.config(text=f"Store Account Credits: ${wallet['balance']}")
                messagebox.showinfo("DevMenu", "Injected +$500 credits!")
            tk.Button(browser_inner_frame, text="💰 Give +$500 Store Credits", bg="#28a745", fg="white", font=("Arial", 10, "bold"), command=add_money).pack(fill="x", pady=8)
            def trigger_matrix():
                browser_inner_frame.config(bg="black")
                for w in browser_inner_frame.winfo_children():
                    try: w.config(bg="black", fg="#00ff00")
                    except: pass
            tk.Button(browser_inner_frame, text="🎨 Load Matrix Theme Core", bg="#343a40", fg="#00ff00", font=("Arial", 10, "bold"), command=trigger_matrix).pack(fill="x", pady=8)
        else: messagebox.showinfo("Browser", f"Searching for: {search_query}")
    def load_content(frame):
        global browser_inner_frame
        browser_inner_frame = frame
        tk.Label(frame, text="BlueOS Web Browser", bg="#f0f0f0", font=("Arial", 14, "bold")).pack(pady=10)
        global search_entry
        search_entry = tk.Entry(frame, width=30, font=("Arial", 12))
        search_entry.insert(0, "devmenu.com"); search_entry.pack(pady=10)
        tk.Button(frame, text="Search Network", bg="#007bff", fg="white", font=("Arial", 11), command=browse_action).pack(pady=10)
    make_window("Browser System", load_content)

def open_game():
    def hack_action():
        if guess_entry.get() == "7": res_label.config(text="GRANTED! System Hacked 🔓", fg="green")
        else: res_label.config(text="DENIED! Try code 7. ❌", fg="red")
    def load_content(frame):
        tk.Label(frame, text="Matrix Cryptic Guess Game", bg="#f0f0f0", font=("Arial", 14, "bold")).pack(pady=10)
        global guess_entry, res_label
        guess_entry = tk.Entry(frame, width=15, font=("Arial", 12)); guess_entry.pack(pady=10)
        tk.Button(frame, text="Execute Injector", bg="#007bff", fg="white", font=("Arial", 11), command=hack_action).pack(pady=10)
        res_label = tk.Label(frame, text="", bg="#f0f0f0", font=("Arial", 12, "bold")); res_label.pack(pady=10)
    make_window("Game Matrix core", load_content)

def open_calculator():
    def calc_sum():
        try: res = float(num1.get()) + float(num2.get()); calc_res.config(text=f"Result: {res}", fg="black")
        except: calc_res.config(text="Error Input!", fg="red")
    def load_content(frame):
        tk.Label(frame, text="Calculator Addition Module", bg="#f0f0f0", font=("Arial", 14, "bold")).pack(pady=10)
        global num1, num2, calc_res
        num1 = tk.Entry(frame, width=15, font=("Arial", 12)); num1.pack(pady=5)
        num2 = tk.Entry(frame, width=15, font=("Arial", 12)); num2.pack(pady=5)
        tk.Button(frame, text="Sum Values", bg="#28a745", fg="white", font=("Arial", 11), command=calc_sum).pack(pady=10)
        calc_res = tk.Label(frame, text="", bg="#f0f0f0", font=("Arial", 12, "bold")); calc_res.pack(pady=10)
    make_window("Calculator App", load_content)

def open_book():
    def load_content(frame):
        tk.Label(frame, text="Python Dev Guide", bg="#f0f0f0", font=("Arial", 14, "bold")).pack(pady=10)
        story = tk.Text(frame, wrap="word", height=8, width=35, font=("Arial", 11))
        story.insert("1.0", "Chapter 1: The Dev Journey\nYou have compiled your mobile system core completely functional!")
        story.config(state="disabled").pack(pady=10)
    make_window("Blue E-Book Reader", load_content)
def open_bootloader():
    def flash_os(os_name, bg_color, fg_color, message):
        root.config(bg=bg_color)
        messagebox.showinfo("Bootloader", f"Flashing custom recovery...\nSystem changes applied:\n{message}")
    def load_content(frame):
        tk.Label(frame, text="⚙️ ADVANCED SYSTEM BOOTLOADER", bg="#f0f0f0", fg="red", font=("Arial", 13, "bold")).pack(pady=5)
        tk.Button(frame, text="🐧 Boot into Linux Core Terminal", bg="black", fg="#00ff00", font=("Arial", 10, "bold"), command=lambda: flash_os("Linux", "black", "#00ff00", "Linux Terminal mode active.")).pack(fill="x", pady=5)
        tk.Button(frame, text="🍏 Emulate Apple Custom iOS", bg="#f8f9fa", fg="black", font=("Arial", 10, "bold"), command=lambda: flash_os("iOS", "#e9ecef", "black", "iOS white desk active.")).pack(fill="x", pady=5)
        tk.Button(frame, text="🤖 Restore Android Recovery Core", bg="#343a40", fg="white", font=("Arial", 10, "bold"), command=lambda: flash_os("Android", "#0047ab", "white", "Default BlueOS core restored.")).pack(fill="x", pady=5)
    make_window("Bootloader Utility v1.0", load_content)

def open_bpk_installer():
    def execute_bpk(file_name, display_name, action_func):
        messagebox.showinfo("BPK Installer", f"Extracting manifest for {file_name}...\nInstalling packages to user system directory.")
        action_func(display_name)
    def run_flappy(name):
        def play_tap(): bird_lbl.config(text="💥 BIRD FLAPPED! Score +1 💥", fg="green")
        def load_game_frame(f):
            tk.Label(f, text="👾 Mini Flappy Bird Simulation", bg="#f0f0f0", font=("Arial", 13, "bold")).pack(pady=5)
            global bird_lbl
            bird_lbl = tk.Label(f, text="Press Tap to keep bird flying!", bg="#f0f0f0", font=("Arial", 11))
            bird_lbl.pack(pady=10)
            tk.Button(f, text="🕹️ Tap Jump", bg="#ffc107", font=("Arial", 11, "bold"), command=play_tap).pack(pady=10)
        make_window(name, load_game_frame)
    def run_antivirus(name):
        def run_scan(): scan_lbl.config(text="🛡️ SCAN COMPLETE: 0 Viruses Found. Clean!", fg="green")
        def load_av_frame(f):
            tk.Label(f, text="🛡️ BlueOS Guard Antivirus", bg="#f0f0f0", font=("Arial", 13, "bold")).pack(pady=5)
            global scan_lbl
            scan_lbl = tk.Label(f, text="System Threat Scan Pending...", bg="#f0f0f0", font=("Arial", 11))
            scan_lbl.pack(pady=10)
            tk.Button(f, text="🔍 Analyze File Trees", bg="#007bff", fg="white", command=run_scan).pack(pady=10)
        make_window(name, load_av_frame)
    def load_content(frame):
        tk.Label(frame, text="📦 BlueOS .BPK PACKAGE INSTALLER", bg="#f0f0f0", fg="#4b0082", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Button(frame, text="📦 Run: flappy_bird.bpk", bg="#e9ecef", anchor="w", font=("Arial", 10), command=lambda: execute_bpk("flappy_bird.bpk", "Flappy Bird", run_flappy)).pack(fill="x", pady=4)
        tk.Button(frame, text="📦 Run: antivirus_pro.bpk", bg="#e9ecef", anchor="w", font=("Arial", 10), command=lambda: execute_bpk("antivirus_pro.bpk", "Antivirus Suite", run_antivirus)).pack(fill="x", pady=4)
    make_window("BPK Installer Runtime", load_content)

installed_apps = {"calculator": False, "book": False, "bootloader": False, "bpk": False}

def open_store():
    def buy_item(item_name, cost, install_func, btn):
        if installed_apps[item_name]: return
        if wallet["balance"] >= cost:
            wallet["balance"] -= cost
            wallet_label.config(text=f"Store Account Credits: ${wallet['balance']}")
            installed_apps[item_name] = True
            btn.config(text="Installed Engine", bg="#6c757d", state="disabled")
            if item_name == "calculator": tk.Button(root, text="Calculator", bg="#0047ab", fg="white", font=("Arial", 11, "bold"), bd=1, command=open_calculator).place(x=150, y=40, width=110, height=55)
            elif item_name == "book": tk.Button(root, text="E-Book", bg="#0047ab", fg="white", font=("Arial", 11, "bold"), bd=1, command=open_book).place(x=150, y=110, width=110, height=55)
            elif item_name == "bootloader": tk.Button(root, text="Bootloader", bg="#8b0000", fg="white", font=("Arial", 11, "bold"), bd=1, command=open_bootloader).place(x=150, y=180, width=110, height=55)
            elif item_name == "bpk": tk.Button(root, text="BPK Installer", bg="#4b0082", fg="white", font=("Arial", 11, "bold"), bd=1, command=open_bpk_installer).place(x=150, y=250, width=110, height=55)
            messagebox.showinfo("Store", "Module Installed to Main Screen!")
        else: messagebox.showerror("Store", "Insufficient Token Balance!")
    def load_content(frame):
        global wallet_label
        wallet_label = tk.Label(frame, text=f"Store Account Credits: ${wallet['balance']}", bg="#f0f0f0", fg="green", font=("Arial", 11, "bold")); wallet_label.pack(anchor="ne", pady=5)
        tk.Label(frame, text="Blue Store App Market", bg="#f0f0f0", font=("Arial", 15, "bold")).pack(pady=10)
        r1 = tk.Frame(frame, bg="#e9ecef", pady=5, padx=10); r1.pack(fill="x", pady=2)
        tk.Label(r1, text="Calculator Panel (Free)", bg="#e9ecef").pack(side="left")
        c_btn = tk.Button(r1, text="Download", bg="#28a745", fg="white", command=lambda: buy_item("calculator", 0, open_calculator, c_btn))
        if installed_apps["calculator"]: c_btn.config(text="Installed", bg="#6c757d", state="disabled")
        c_btn.pack(side="right")
        r2 = tk.Frame(frame, bg="#e9ecef", pady=5, padx=10); r2.pack(fill="x", pady=2)
        tk.Label(r2, text="Coding E-Book ($50)", bg="#e9ecef").pack(side="left")
        b_btn = tk.Button(r2, text="Purchase", bg="#007bff", fg="white", command=lambda: buy_item("book", 50, open_book, b_btn))
        if installed_apps["book"]: b_btn.config(text="Installed", bg="#6c757d", state="disabled")
        b_btn.pack(side="right")
        r3 = tk.Frame(frame, bg="#f8d7da", pady=5, padx=10, borderwidth=1, relief="solid"); r3.pack(fill="x", pady=2)
        tk.Label(r3, text="⚙️ Bootloader Tool ($100)", bg="#f8d7da", fg="#721c24", font=("Arial", 9, "bold")).pack(side="left")
        bl_btn = tk.Button(r3, text="Dev Flash", bg="#dc3545", fg="white", command=lambda: buy_item("bootloader", 100, open_bootloader, bl_btn))
        if installed_apps["bootloader"]: bl_btn.config(text="Installed", bg="#6c757d", state="disabled")
        bl_btn.pack(side="right")
        r4 = tk.Frame(frame, bg="#e0cee8", pady=5, padx=10, borderwidth=1, relief="solid"); r4.pack(fill="x", pady=4)
        tk.Label(r4, text="📦 BPK Installer Suite ($50)", bg="#e0cee8", fg="#4b0082", font=("Arial", 9, "bold")).pack(side="left")
        bpk_btn = tk.Button(r4, text="Get BPK", bg="#4b0082", fg="white", font=("Arial", 9, "bold"), command=lambda: buy_item("bpk", 50, open_bpk_installer, bpk_btn))
        if installed_apps["bpk"]: bpk_btn.config(text="Installed", bg="#6c757d", state="disabled")
        bpk_btn.pack(side="right")
    make_window("Blue Store", load_content)

tk.Button(root, text="Launch Browser", bg="#00285a", fg="white", font=("Arial", 11, "bold"), bd=1, command=open_browser).place(x=20, y=40, width=125, height=55)
tk.Button(root, text="Play Matrix Game", bg="#00285a", fg="white", font=("Arial", 11, "bold"), bd=1, command=open_game).place(x=20, y=115, width=125, height=55)
tk.Button(root, text="Open Blue Store", bg="#00285a", fg="white", font=("Arial", 11, "bold"), bd=1, command=open_store).place(x=20, y=190, width=125, height=55)

taskbar = tk.Frame(root, bg="#00183a", height=45); taskbar.pack(fill="x", side="bottom")
tk.Button(taskbar, text="Start OS", bg="#007bff", fg="white", font=("Arial", 10, "bold"), command=lambda: messagebox.showinfo("Start", "BlueOS Mobile Engine Core Stable.")).pack(side="left", padx=5, pady=5)
fullscreen_btn = tk.Button(taskbar, text="Full Screen OS", bg="#28a745", fg="white", font=("Arial", 10, "bold"), command=toggle_fullscreen); fullscreen_btn.pack(side="left", padx=5, pady=5)
clock_label = tk.Label(taskbar, text="", bg="#00183a", fg="white", font=("Arial", 10, "bold")); clock_label.pack(side="right", padx=10)

def update_time():
    clock_label.config(text=datetime.datetime.now().strftime("%I:%M %p"))
    root.after(1000, update_time)
update_time()
root.mainloop()
