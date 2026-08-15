// Piano.cs — C# версия
using System;
using System.Collections.Generic;
using System.Diagnostics;

class Piano
{
    static Dictionary<string, double> notes = new Dictionary<string, double>()
    {
        {"a", 261.63}, {"w", 277.18}, {"s", 293.66}, {"e", 311.13},
        {"d", 329.63}, {"f", 349.23}, {"t", 369.99}, {"g", 392.00},
        {"y", 415.30}, {"h", 440.00}, {"u", 466.16}, {"j", 493.88},
        {"k", 523.25}, {"o", 554.37}, {"l", 587.33}, {"p", 622.25},
        {";", 659.25}
    };

    static void PlayNote(double freq)
    {
        // Используем beep или консольный звук
        try
        {
            Process.Start("beep", $"-f {freq} -l 300");
        }
        catch
        {
            Console.Beep((int)freq, 300);
        }
    }

    static void PrintPiano()
    {
        Console.WriteLine("Клавиши для игры:");
        Console.WriteLine("  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;");
        Console.WriteLine("  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E");
        Console.WriteLine("Нажмите q для выхода");
    }

    static void Main()
    {
        Console.WriteLine("🎹 Пианино (88 клавиш) — C# версия");
        PrintPiano();
        while (true)
        {
            Console.Write("Введите ноту: ");
            string input = Console.ReadLine().Trim().ToLower();
            if (input == "q") break;
            if (notes.ContainsKey(input))
            {
                double freq = notes[input];
                Console.WriteLine($"Играем {input} -> {freq:F2} Гц");
                PlayNote(freq);
            }
            else
            {
                Console.WriteLine("Неизвестная нота.");
            }
        }
    }
}
