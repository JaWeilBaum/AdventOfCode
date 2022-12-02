package day02

import "fmt"

func PartOne(data []string) {
	/**
	Opponent:
	A = Rock
	B = Paper
	C = Scissor

	Us:
	X, 1 = Rock
	Y, 2 = Paper
	Z, 3 = Scissor
	*/

	shapeMap := map[string]int{
		"A X": 1, "B X": 1, "C X": 1,
		"A Y": 2, "B Y": 2, "C Y": 2,
		"A Z": 3, "B Z": 3, "C Z": 3}
	resultMap := map[string]int{
		"A Z": 0, "B X": 0, "C Y": 0, // Loose
		"A X": 3, "B Y": 3, "C Z": 3, // Draw
		"A Y": 6, "B Z": 6, "C X": 6} // Win

	fmt.Printf("Part One\nTotal score: %v\n\n\n", calcResult(data, shapeMap, resultMap))
}

func PartTwo(data []string) {
	/*
		Opponent:
			A = Rock
			B = Paper
			C = Scissor

		Desired outcome:
			X = Loose
			Y = Draw
			Z = Win
	*/

	shapeMap := map[string]int{
		"A X": 3, "B X": 1, "C X": 2,
		"A Y": 1, "B Y": 2, "C Y": 3,
		"A Z": 2, "B Z": 3, "C Z": 1}

	resultMap := map[string]int{
		"A X": 0, "B X": 0, "C X": 0, // Loose
		"A Y": 3, "B Y": 3, "C Y": 3, // Draw
		"A Z": 6, "B Z": 6, "C Z": 6} // Win

	fmt.Printf("Part two\nTotal score: %v", calcResult(data, shapeMap, resultMap))
}

func calcResult(data []string, shapeMap map[string]int, resultMap map[string]int) int {
	totalScore := 0
	for _, value := range data {
		gameOutcomeValue := resultMap[value]
		shapeValue := shapeMap[value]
		fmt.Printf("'%v' Outcome: %v + %v = %v\n", value, gameOutcomeValue, shapeValue, gameOutcomeValue+shapeValue)
		totalScore += gameOutcomeValue + shapeValue
	}
	return totalScore
}
