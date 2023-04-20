# rs232vkeyboard
The program is used to download data from RS232 and insert values directly in real time to e.g. Excel, Notepad
The program can be used, for example, to collect data from electronic scales and save them to a file.


Wymagania
-----------

Ten program wymaga zainstalowania bibliotek PySerial i PyNput.

Funkcje
-------

serial_to_keyboard(keyboard, serial_port)
    Funkcja odbiera dane z portu szeregowego i wprowadza je do klawiatury.

Parametry:
    - keyboard (pynput.keyboard.Controller): obiekt kontrolera klawiatury PyNput.
    - serial_port (str): numer portu szeregowego (np. "COM1").

Wersja
-------

1.0 (20.04.2023)
