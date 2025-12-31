import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import keyboard
import threading
import time
import json
import os

class jpXcodeAutoClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("jpXcode Auto Clicker v1.0")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        
        # Variables
        self.is_clicking = False
        self.click_thread = None
        self.hotkey = 'F6'
        self.recorded_actions = []
        self.is_recording = False
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        self.setup_hotkey()
        
    def setup_ui(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = tk.Label(main_frame, text="jpXcode Auto Clicker", 
                              font=("Arial", 16, "bold"), fg="#2c3e50")
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Click Interval Section
        interval_frame = ttk.LabelFrame(main_frame, text="Interval Klik", padding="10")
        interval_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(interval_frame, text="Jam:").grid(row=0, column=0, padx=5)
        self.hours_var = tk.StringVar(value="0")
        ttk.Entry(interval_frame, textvariable=self.hours_var, width=8).grid(row=0, column=1)
        
        ttk.Label(interval_frame, text="Menit:").grid(row=0, column=2, padx=5)
        self.minutes_var = tk.StringVar(value="0")
        ttk.Entry(interval_frame, textvariable=self.minutes_var, width=8).grid(row=0, column=3)
        
        ttk.Label(interval_frame, text="Detik:").grid(row=1, column=0, padx=5, pady=5)
        self.seconds_var = tk.StringVar(value="0")
        ttk.Entry(interval_frame, textvariable=self.seconds_var, width=8).grid(row=1, column=1)
        
        ttk.Label(interval_frame, text="Milidetik:").grid(row=1, column=2, padx=5)
        self.milliseconds_var = tk.StringVar(value="100")
        ttk.Entry(interval_frame, textvariable=self.milliseconds_var, width=8).grid(row=1, column=3)
        
        # Click Options Section
        options_frame = ttk.LabelFrame(main_frame, text="Opsi Klik", padding="10")
        options_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(options_frame, text="Tombol Mouse:").grid(row=0, column=0, sticky=tk.W)
        self.mouse_button = tk.StringVar(value="left")
        ttk.Radiobutton(options_frame, text="Kiri", variable=self.mouse_button, 
                       value="left").grid(row=0, column=1, sticky=tk.W)
        ttk.Radiobutton(options_frame, text="Kanan", variable=self.mouse_button, 
                       value="right").grid(row=0, column=2, sticky=tk.W)
        ttk.Radiobutton(options_frame, text="Tengah", variable=self.mouse_button, 
                       value="middle").grid(row=0, column=3, sticky=tk.W)
        
        ttk.Label(options_frame, text="Jenis Klik:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.click_type = tk.StringVar(value="single")
        ttk.Radiobutton(options_frame, text="Tunggal", variable=self.click_type, 
                       value="single").grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(options_frame, text="Ganda", variable=self.click_type, 
                       value="double").grid(row=1, column=2, sticky=tk.W)
        ttk.Radiobutton(options_frame, text="Tiga Kali", variable=self.click_type, 
                       value="triple").grid(row=1, column=3, sticky=tk.W)
        
        # Repeat Options
        repeat_frame = ttk.LabelFrame(main_frame, text="Pengulangan Klik", padding="10")
        repeat_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        self.repeat_mode = tk.StringVar(value="infinite")
        ttk.Radiobutton(repeat_frame, text="Ulangi tanpa batas", 
                       variable=self.repeat_mode, value="infinite").grid(row=0, column=0, sticky=tk.W)
        ttk.Radiobutton(repeat_frame, text="Jumlah tertentu:", 
                       variable=self.repeat_mode, value="limited").grid(row=1, column=0, sticky=tk.W)
        
        self.repeat_count = tk.StringVar(value="10")
        ttk.Entry(repeat_frame, textvariable=self.repeat_count, width=10).grid(row=1, column=1, padx=5)
        
        # Cursor Position
        position_frame = ttk.LabelFrame(main_frame, text="Posisi Kursor", padding="10")
        position_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        self.position_mode = tk.StringVar(value="current")
        ttk.Radiobutton(position_frame, text="Lokasi kursor saat ini", 
                       variable=self.position_mode, value="current").grid(row=0, column=0, sticky=tk.W)
        ttk.Radiobutton(position_frame, text="Lokasi spesifik:", 
                       variable=self.position_mode, value="specific").grid(row=1, column=0, sticky=tk.W)
        
        ttk.Label(position_frame, text="X:").grid(row=1, column=1)
        self.pos_x = tk.StringVar(value="0")
        ttk.Entry(position_frame, textvariable=self.pos_x, width=8).grid(row=1, column=2)
        
        ttk.Label(position_frame, text="Y:").grid(row=1, column=3)
        self.pos_y = tk.StringVar(value="0")
        ttk.Entry(position_frame, textvariable=self.pos_y, width=8).grid(row=1, column=4)
        
        ttk.Button(position_frame, text="Ambil Posisi", 
                  command=self.capture_position).grid(row=1, column=5, padx=5)
        
        # Hotkey Section
        hotkey_frame = ttk.LabelFrame(main_frame, text="Hotkey (Mulai/Stop)", padding="10")
        hotkey_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(hotkey_frame, text="Hotkey saat ini:").grid(row=0, column=0)
        self.hotkey_label = tk.Label(hotkey_frame, text=self.hotkey, 
                                     font=("Arial", 10, "bold"), fg="#e74c3c")
        self.hotkey_label.grid(row=0, column=1, padx=10)
        ttk.Button(hotkey_frame, text="Ubah Hotkey", 
                  command=self.change_hotkey).grid(row=0, column=2)
        
        # Record & Playback
        record_frame = ttk.LabelFrame(main_frame, text="Rekam & Putar Ulang", padding="10")
        record_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        self.record_btn = ttk.Button(record_frame, text="Mulai Rekam (F7)", 
                                     command=self.toggle_recording)
        self.record_btn.grid(row=0, column=0, padx=5)
        
        ttk.Button(record_frame, text="Putar Ulang", 
                  command=self.playback_recording).grid(row=0, column=1, padx=5)
        
        ttk.Button(record_frame, text="Simpan", 
                  command=self.save_recording).grid(row=0, column=2, padx=5)
        
        ttk.Button(record_frame, text="Muat", 
                  command=self.load_recording).grid(row=0, column=3, padx=5)
        
        self.record_status = tk.Label(record_frame, text="Siap", fg="#27ae60")
        self.record_status.grid(row=1, column=0, columnspan=4, pady=5)
        
        # Control Buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=7, column=0, columnspan=3, pady=15)
        
        self.start_btn = tk.Button(control_frame, text="MULAI (F6)", 
                                   command=self.toggle_clicking, 
                                   bg="#27ae60", fg="white", 
                                   font=("Arial", 12, "bold"),
                                   width=15, height=2)
        self.start_btn.grid(row=0, column=0, padx=10)
        
        tk.Button(control_frame, text="KELUAR", 
                 command=self.quit_app, 
                 bg="#e74c3c", fg="white", 
                 font=("Arial", 12, "bold"),
                 width=15, height=2).grid(row=0, column=1, padx=10)
        
        # Status
        self.status_label = tk.Label(main_frame, text="Status: Siap", 
                                     font=("Arial", 10), fg="#7f8c8d")
        self.status_label.grid(row=8, column=0, columnspan=3, pady=5)
        
    def setup_hotkey(self):
        keyboard.add_hotkey(self.hotkey, self.toggle_clicking)
        keyboard.add_hotkey('F7', self.toggle_recording)
        
    def get_interval(self):
        try:
            hours = float(self.hours_var.get() or 0)
            minutes = float(self.minutes_var.get() or 0)
            seconds = float(self.seconds_var.get() or 0)
            milliseconds = float(self.milliseconds_var.get() or 0)
            
            total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
            return max(0.001, total_seconds)
        except ValueError:
            return 0.1
            
    def capture_position(self):
        self.root.after(3000, self._get_mouse_position)
        messagebox.showinfo("Ambil Posisi", 
                          "Posisikan kursor Anda dalam 3 detik...")
        
    def _get_mouse_position(self):
        x, y = pyautogui.position()
        self.pos_x.set(str(x))
        self.pos_y.set(str(y))
        self.position_mode.set("specific")
        
    def change_hotkey(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Ubah Hotkey")
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        
        tk.Label(dialog, text="Tekan tombol baru untuk hotkey:", 
                font=("Arial", 10)).pack(pady=20)
        
        key_label = tk.Label(dialog, text="Menunggu...", 
                            font=("Arial", 12, "bold"), fg="#e74c3c")
        key_label.pack(pady=10)
        
        def on_key(event):
            new_key = event.keysym
            if new_key not in ['Escape', 'Return']:
                keyboard.remove_hotkey(self.hotkey)
                self.hotkey = new_key
                keyboard.add_hotkey(self.hotkey, self.toggle_clicking)
                self.hotkey_label.config(text=self.hotkey)
                dialog.destroy()
                
        dialog.bind('<Key>', on_key)
        dialog.focus()
        
    def perform_click(self):
        clicks = {'single': 1, 'double': 2, 'triple': 3}[self.click_type.get()]
        button = self.mouse_button.get()
        
        if self.position_mode.get() == "specific":
            try:
                x = int(self.pos_x.get())
                y = int(self.pos_y.get())
                pyautogui.click(x, y, clicks=clicks, button=button)
            except:
                pyautogui.click(clicks=clicks, button=button)
        else:
            pyautogui.click(clicks=clicks, button=button)
            
    def clicking_loop(self):
        interval = self.get_interval()
        count = 0
        max_count = int(self.repeat_count.get()) if self.repeat_mode.get() == "limited" else -1
        
        while self.is_clicking:
            if max_count > 0 and count >= max_count:
                self.is_clicking = False
                break
                
            self.perform_click()
            count += 1
            self.status_label.config(text=f"Status: Berjalan (Klik: {count})")
            time.sleep(interval)
            
        self.status_label.config(text="Status: Berhenti")
        self.start_btn.config(text="MULAI (F6)", bg="#27ae60")
        
    def toggle_clicking(self):
        if not self.is_clicking:
            self.is_clicking = True
            self.start_btn.config(text="STOP (F6)", bg="#e74c3c")
            self.click_thread = threading.Thread(target=self.clicking_loop, daemon=True)
            self.click_thread.start()
        else:
            self.is_clicking = False
            
    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.recorded_actions = []
            self.record_btn.config(text="Stop Rekam (F7)")
            self.record_status.config(text="Merekam...", fg="#e74c3c")
            threading.Thread(target=self.record_loop, daemon=True).start()
        else:
            self.is_recording = False
            self.record_btn.config(text="Mulai Rekam (F7)")
            self.record_status.config(text=f"Selesai ({len(self.recorded_actions)} aksi)", fg="#27ae60")
            
    def record_loop(self):
        import mouse
        last_time = time.time()
        
        def on_click(event):
            if self.is_recording:
                current_time = time.time()
                delay = current_time - last_time
                self.recorded_actions.append({
                    'type': 'click',
                    'button': event.button,
                    'x': event.x,
                    'y': event.y,
                    'delay': delay
                })
                
        mouse.hook(on_click)
        
        while self.is_recording:
            time.sleep(0.1)
            
        mouse.unhook(on_click)
        
    def playback_recording(self):
        if not self.recorded_actions:
            messagebox.showwarning("Peringatan", "Tidak ada rekaman untuk diputar!")
            return
            
        def play():
            for action in self.recorded_actions:
                time.sleep(action['delay'])
                pyautogui.click(action['x'], action['y'], button=action['button'])
                
        threading.Thread(target=play, daemon=True).start()
        
    def save_recording(self):
        if not self.recorded_actions:
            messagebox.showwarning("Peringatan", "Tidak ada rekaman untuk disimpan!")
            return
            
        filename = "recording.json"
        with open(filename, 'w') as f:
            json.dump(self.recorded_actions, f)
        messagebox.showinfo("Sukses", f"Rekaman disimpan ke {filename}")
        
    def load_recording(self):
        filename = "recording.json"
        if not os.path.exists(filename):
            messagebox.showwarning("Peringatan", "File rekaman tidak ditemukan!")
            return
            
        with open(filename, 'r') as f:
            self.recorded_actions = json.load(f)
        self.record_status.config(text=f"Dimuat ({len(self.recorded_actions)} aksi)", fg="#3498db")
        messagebox.showinfo("Sukses", "Rekaman berhasil dimuat!")
        
    def quit_app(self):
        self.is_clicking = False
        self.is_recording = False
        keyboard.unhook_all()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = jpXcodeAutoClicker(root)
    root.mainloop()
