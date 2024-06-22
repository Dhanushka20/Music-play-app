import tkinter as tk
import pygame
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Music Player")
        self.master.geometry("400x200")

        # Specify the full path to the music folder
        self.music_folder = r"D:\Music\Dance English"
        self.music_files = [f for f in os.listdir(self.music_folder) if f.endswith(".mp3")]
        self.current_track = 0

        self.init_player()
        self.create_widgets()

    def init_player(self):
        pygame.mixer.init()

    def create_widgets(self):
        self.track_label = tk.Label(self.master, text="Track: ")
        self.track_label.grid(row=0, column=0, padx=10, pady=10)

        self.track_name = tk.Label(self.master, text="")
        self.track_name.grid(row=0, column=1, padx=10, pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_music, bg="green")
        self.play_button.grid(row=1, column=0, padx=10, pady=10)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_music, bg="yellow")
        self.pause_button.grid(row=1, column=1, padx=10, pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music, bg="red")
        self.stop_button.grid(row=1, column=2, padx=10, pady=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_track, bg="blue")
        self.next_button.grid(row=2, column=1, padx=10, pady=10)

        self.volume_label = tk.Label(self.master, text="Volume: ")
        self.volume_label.grid(row=3, column=0, padx=10, pady=10)

        self.volume_scale = tk.Scale(self.master, from_=0, to=100, orient="horizontal", command=self.change_volume)
        self.volume_scale.set(50)
        self.volume_scale.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        self.progress_bar = tk.Scale(self.master, from_=0, to=100, orient="horizontal")
        self.progress_bar.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def play_music(self):
        if hasattr(self, 'paused') and self.paused:
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_pos(self.paused_time)
            self.paused = False
        else:
            pygame.mixer.music.load(os.path.join(self.music_folder, self.music_files[self.current_track]))
            pygame.mixer.music.play()
            self.update_track_name()

    def pause_music(self):
        self.paused = True
        self.paused_time = pygame.mixer.music.get_pos() // 1000
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.music_files)
        self.play_music()

    def change_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

    def update_track_name(self):
        # Get the first three words of the track name
        track_name = " ".join(self.music_files[self.current_track].split()[:4])
        self.track_name.config(text=track_name)

def main():
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
