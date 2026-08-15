// piano.go — Go версия
package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

var notes = map[string]float64{
	"a": 261.63, "w": 277.18, "s": 293.66, "e": 311.13,
	"d": 329.63, "f": 349.23, "t": 369.99, "g": 392.00,
	"y": 415.30, "h": 440.00, "u": 466.16, "j": 493.88,
	"k": 523.25, "o": 554.37, "l": 587.33, "p": 622.25,
	";": 659.25,
}

func playNote(freq float64) {
	var cmd *exec.Cmd
	switch runtime.GOOS {
	case "windows":
		// Используем winsound через PowerShell
		cmd = exec.Command("powershell", "-Command", fmt.Sprintf("[System.Console]::Beep(%d, 300)", int(freq)))
	case "darwin", "linux":
		cmd = exec.Command("beep", "-f", strconv.Itoa(int(freq)), "-l", "300")
	default:
		return
	}
	cmd.Run()
}

func printPiano() {
	fmt.Println("Клавиши для игры:")
	fmt.Println("  a  w  s  e  d  f  t  g  y  h  u  j  k  o  l  p  ;")
	fmt.Println("  C  C# D  D# E  F  F# G  G# A  A# B  C  C# D  D# E")
	fmt.Println("Нажмите q для выхода")
}

func main() {
	fmt.Println("🎹 Пианино (88 клавиш) — Go версия")
	printPiano()
	for {
		var input string
		fmt.Print("Введите ноту: ")
		fmt.Scanln(&input)
		input = strings.TrimSpace(strings.ToLower(input))
		if input == "q" {
			break
		}
		if freq, ok := notes[input]; ok {
			fmt.Printf("Играем %s -> %.2f Гц\n", input, freq)
			playNote(freq)
		} else {
			fmt.Println("Неизвестная нота.")
		}
	}
}
