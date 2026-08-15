// piano.rs — Rust версия
use std::collections::HashMap;
use std::io::{self, Write};
use std::process::Command;

fn main() {
    let mut notes = HashMap::new();
    notes.insert("a", 261.63);
    notes.insert("w", 277.18);
    notes.insert("s", 293.66);
    notes.insert("e", 311.13);
    notes.insert("d", 329.63);
    notes.insert("f", 349.23);
    notes.insert("t", 369.99);
    notes.insert("g", 392.00);
    notes.insert("y", 415.30);
    notes.insert("h", 440.00);
    notes.insert("u", 466.16);
    notes.insert("j", 493.88);
    notes.insert("k", 523.25);
    notes.insert("o", 554.37);
    notes.insert("l", 587.33);
    notes.insert("p", 622.25);
    notes.insert(";", 659.25);

    println!("🎹 Пианино (88 клавиш) — Rust версия");
    println!("Клавиши для игры:");
    println!("  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;");
    println!("  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E");
    println!("Нажмите q для выхода");

    loop {
        print!("Введите ноту: ");
        io::stdout().flush().unwrap();
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let input = input.trim().to_lowercase();
        if input == "q" { break; }
        if let Some(&freq) = notes.get(&input.as_str()) {
            println!("Играем {} -> {:.2} Гц", input, freq);
            // Воспроизведение через beep
            let _ = Command::new("beep")
                .args(&["-f", &freq.to_string(), "-l", "300"])
                .status();
        } else {
            println!("Неизвестная нота.");
        }
    }
}
