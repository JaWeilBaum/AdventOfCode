package day03

import (
	"aoc/helper"
	"fmt"
	"strings"
)

func PartOne(data []string) {
	wronglyPackerLetters := ""

	for _, row := range data {
		stringLen := len(row)
		midPoint := stringLen / 2
		firstPart := row[:midPoint]
		secondPart := row[midPoint:]

		similarLetters := findSameLetters(firstPart, secondPart)
		wronglyPackerLetters += similarLetters
	}
	fmt.Printf("Part One: %v\n", priorityOfLetters(wronglyPackerLetters))
}

func findSameLetters(string1 string, string2 string) string {
	sameLetters := ""

	for _, c := range string1 {
		if strings.Contains(string2, string(c)) && !strings.Contains(sameLetters, string(c)) {
			sameLetters = sameLetters + string(c)
		}
	}
	return sameLetters
}

func priorityOfLetters(matchingLetters string) int {
	// Small letters [97;122]
	// Capital letters [65;90]

	var values []int

	for _, c := range matchingLetters {
		value := 0
		if c >= 97 && c <= 122 {
			value = int(c) - 96
		} else {
			value = int(c) - 64 + 26
		}
		values = append(values, value)
	}

	return helper.Sum(values)
}

func PartTwo(data []string) {

	triplets := make([]string, 0)

	currentString := ""

	for index, row := range data {
		if index%3 == 0 && len(currentString) > 0 {
			triplets = append(triplets, currentString)
			currentString = ""
		}
		finalAppend := ""
		if strings.Count(currentString, ",") < 2 {
			finalAppend = ","
		}
		currentString += row + finalAppend
	}
	triplets = append(triplets, currentString)

	badges := ""

	for _, row := range triplets {
		parts := strings.Split(row, ",")
		firstParts := findSameLetters(parts[0], parts[1])
		similarParts := findSameLetters(firstParts, parts[2])
		badges += similarParts
	}

	fmt.Printf("Part Two: %v", priorityOfLetters(badges))
}
