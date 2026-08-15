# piano.py — Python версия
import sys
import os
import platform
import time
import threading

# Карта клавиш на ноты (частоты)
NOTES = {
    'a': 261.63,  # C4
    'w': 277.18,  # C#4
    's': 293.66,  # D4
    'e': 311.13,  # D#4
    'd': 329.63,  # E4
    'f': 349.23,  # F4
    't': 369.99,  # F#4
    'g': 392.00,  # G4
    'y': 415.30,  # G#4
    'h': 440.00,  # A4
    'u': 466.16,  # A#4
    'j': 493.88,  # B4
    'k': 523.25,  # C5
    'o': 554.37,  # C#5
    'l': 587.33,  # D5
    'p': 622.25,  # D#5
    ';': 659.25,  # E5
}

def play_note(freq, duration=0.3):
    """Воспроизводит звук заданной частоты."""
    system = platform.system()
    if system == 'Windows':
        import winsound
        winsound.Beep(int(freq), int(duration * 1000))
    else:
        # Linux/Mac: используем beep или play
        try:
            os.system(f'beep -f {int(freq)} -l {int(duration * 1000)}')
        except:
            print(f'\a')  # fallback

def print_piano():
    """Выводит ASCII-клавиатуру."""
    keys = ['a', 'w', 's', 'e', 'd', 'f', 't', 'g', 'y', 'h', 'u', 'j', 'k', 'o', 'l', 'p', ';']
    print("Клавиши для игры:")
    print("  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;")
    print("  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E")
    print("Нажмите q для выхода")

def main():
    print("🎹 Пианино (88 клавиш) — упрощённая версия")
    print_piano()
    while True:
        ch = input("Введите ноту: ").strip().lower()
        if ch == 'q':
            break
        if ch in NOTES:
            freq = NOTES[ch]
            print(f"Играем {ch} -> {freq:.2f} Гц")
            play_note(freq)
        else:
            print("Неизвестная нота. Используйте клавиши из списка.")

if __name__ == "__main__":
    main()
