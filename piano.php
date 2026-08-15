<?php
// piano.php — PHP версия
$notes = [
    'a' => 261.63, 'w' => 277.18, 's' => 293.66, 'e' => 311.13,
    'd' => 329.63, 'f' => 349.23, 't' => 369.99, 'g' => 392.00,
    'y' => 415.30, 'h' => 440.00, 'u' => 466.16, 'j' => 493.88,
    'k' => 523.25, 'o' => 554.37, 'l' => 587.33, 'p' => 622.25,
    ';' => 659.25
];

function play_note($freq) {
    exec("beep -f " . round($freq) . " -l 300");
}

echo "🎹 Пианино (88 клавиш) — PHP версия\n";
echo "Клавиши для игры:\n";
echo "  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;\n";
echo "  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E\n";
echo "Нажмите q для выхода\n";

while (true) {
    echo "Введите ноту: ";
    $input = trim(fgets(STDIN));
    $input = strtolower($input);
    if ($input == 'q') break;
    if (array_key_exists($input, $notes)) {
        $freq = $notes[$input];
        echo "Играем $input -> $freq Гц\n";
        play_note($freq);
    } else {
        echo "Неизвестная нота.\n";
    }
}
?>
