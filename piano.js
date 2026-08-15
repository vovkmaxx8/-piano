// piano.js — JavaScript версия
const readline = require('readline');
const { exec } = require('child_process');

const notes = {
    'a': 261.63, 'w': 277.18, 's': 293.66, 'e': 311.13,
    'd': 329.63, 'f': 349.23, 't': 369.99, 'g': 392.00,
    'y': 415.30, 'h': 440.00, 'u': 466.16, 'j': 493.88,
    'k': 523.25, 'o': 554.37, 'l': 587.33, 'p': 622.25,
    ';': 659.25
};

function playNote(freq) {
    const cmd = `beep -f ${Math.round(freq)} -l 300`;
    exec(cmd, (err) => {
        if (err) console.log('Ошибка воспроизведения (возможно, нет beep)');
    });
}

function printPiano() {
    console.log('Клавиши для игры:');
    console.log('  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;');
    console.log('  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E');
    console.log('Нажмите q для выхода');
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

console.log('🎹 Пианино (88 клавиш) — JavaScript версия');
printPiano();

rl.on('line', (input) => {
    input = input.trim().toLowerCase();
    if (input === 'q') {
        rl.close();
        return;
    }
    if (notes[input]) {
        const freq = notes[input];
        console.log(`Играем ${input} -> ${freq} Гц`);
        playNote(freq);
    } else {
        console.log('Неизвестная нота.');
    }
});
