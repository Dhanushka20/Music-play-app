# Simple Music Player

This Python-based Simple Music Player application allows users to play, pause, stop, and navigate through their music tracks. It is built using Tkinter for the GUI and Pygame for music playback.

## Features

- Play, pause, and stop music tracks.
- Navigate to the next track.
- Adjust the volume.
- Display the current track name.

## Requirements

- Python 3.x
- `tkinter` (for GUI)
- `pygame` (for music playback)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/simple-music-player.git
    cd simple-music-player
    ```

2. Install the required Python packages:
    ```sh
    pip install pygame
    ```

## Usage

1. Update the `music_folder` path in the `MusicPlayer` class to point to your music directory:
    ```python
    self.music_folder = r"D:\Music\Dance English"
    ```

2. Run the application:
    ```sh
    python main.py
    ```

3. Use the buttons to control music playback:
    - **Play:** Start or resume the current track.
    - **Pause:** Pause the current track.
    - **Stop:** Stop the current track.
    - **Next:** Skip to the next track.

4. Adjust the volume using the volume slider.

