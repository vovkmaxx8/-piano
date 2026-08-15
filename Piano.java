// Piano.java — Java версия
import java.util.HashMap;
import java.util.Scanner;

public class Piano {
    private static final HashMap<String, Double> notes = new HashMap<>();
    static {
        notes.put("a", 261.63);
        notes.put("w", 277.18);
        notes.put("s", 293.66);
        notes.put("e", 311.13);
        notes.put("d", 329.63);
        notes.put("f", 349.23);
        notes.put("t", 369.99);
        notes.put("g", 392.00);
        notes.put("y", 415.30);
        notes.put("h", 440.00);
        notes.put("u", 466.16);
        notes.put("j", 493.88);
        notes.put("k", 523.25);
        notes.put("o", 554.37);
        notes.put("l", 587.33);
        notes.put("p", 622.25);
        notes.put(";", 659.25);
    }

    private static void playNote(double freq) {
        // Java: используем Toolkit.beep() или консоль
        // Но для частот используем внешнюю команду beep
        try {
            Runtime.getRuntime().exec(new String[]{"beep", "-f", String.valueOf((int)freq), "-l", "300"});
        } catch (Exception e) {
            System.out.println("Ошибка воспроизведения (возможно, нет beep)");
        }
    }

    private static void printPiano() {
        System.out.println("Клавиши для игры:");
        System.out.println("  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;");
        System.out.println("  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E");
        System.out.println("Нажмите q для выхода");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("🎹 Пианино (88 клавиш) — Java версия");
        printPiano();
        while (true) {
            System.out.print("Введите ноту: ");
            String input = scanner.nextLine().trim().toLowerCase();
            if (input.equals("q")) break;
            if (notes.containsKey(input)) {
                double freq = notes.get(input);
                System.out.printf("Играем %s -> %.2f Гц%n", input, freq);
                playNote(freq);
            } else {
                System.out.println("Неизвестная нота.");
            }
        }
        scanner.close();
    }
}
