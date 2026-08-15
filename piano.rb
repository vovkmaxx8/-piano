# piano.rb — Ruby версия
notes = {
  'a' => 261.63, 'w' => 277.18, 's' => 293.66, 'e' => 311.13,
  'd' => 329.63, 'f' => 349.23, 't' => 369.99, 'g' => 392.00,
  'y' => 415.30, 'h' => 440.00, 'u' => 466.16, 'j' => 493.88,
  'k' => 523.25, 'o' => 554.37, 'l' => 587.33, 'p' => 622.25,
  ';' => 659.25
}

def play_note(freq)
  system("beep -f #{freq.to_i} -l 300")
end

puts "🎹 Пианино (88 клавиш) — Ruby версия"
puts "Клавиши для игры:"
puts "  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;"
puts "  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E"
puts "Нажмите q для выхода"

loop do
  print "Введите ноту: "
  input = gets.chomp.downcase
  break if input == 'q'
  if notes.key?(input)
    freq = notes[input]
    puts "Играем #{input} -> #{freq} Гц"
    play_note(freq)
  else
    puts "Неизвестная нота."
  end
end
