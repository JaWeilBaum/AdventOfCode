package day05

import (
	"fmt"
	"regexp"
	"strconv"
)

type Move struct {
	from   int
	to     int
	amount int
}

func PartOne(data []string) {
	initialPart := data[:8]
	inputs := data[10:]

	stacks := parseStacks(initialPart, 9)
	moves := parseMoves(inputs)

	for _, move := range moves {

		for i := 0; i < move.amount; i++ {
			lastIndex := len(stacks[move.from]) - 1
			x := ""
			x, stacks[move.from] = stacks[move.from][lastIndex], stacks[move.from][:lastIndex]

			stacks[move.to] = append(stacks[move.to], x)
		}
	}

	resultString := ""

	for _, stack := range stacks {
		resultString += stack[len(stack)-1]
	}
	fmt.Printf("Part One: %v\n", resultString)
}

func parseMoves(data []string) []Move {
	moves := make([]Move, 0)

	for _, row := range data {
		r := regexp.MustCompile(`move (\d+) from (\d+) to (\d+)`)
		subMatch := r.FindStringSubmatch(row)
		amount, _ := strconv.Atoi(subMatch[1])
		from, _ := strconv.Atoi(subMatch[2])
		to, _ := strconv.Atoi(subMatch[3])

		move := Move{from: from - 1, to: to - 1, amount: amount}
		moves = append(moves, move)
		// fmt.Printf("%#v \n", move)
	}

	return moves
}

func parseStacks(data []string, numStacks int) [][]string {

	var stacks = make([][]string, numStacks)
	/*
			0 1 2 3 4 5 6 7 8 9
			  X       X       X
		1 + (j * 4)
	*/
	for i := len(data) - 1; i >= 0; i-- {
		row := data[i]
		for j := 0; j < numStacks; j++ {
			char := string(row[1+(j*4)])
			// fmt.Printf("%v, ", char)

			if char != " " {
				stacks[j] = append(stacks[j], char)
			}
		}

		//fmt.Printf("%v \n", data[i])
	}
	/*
		fmt.Println()
		for index, stack := range stacks {
			fmt.Printf("%v, %v \n", index, stack)
		}
	*/
	return stacks
}

func PartTwo(data []string) {
	initialPart := data[:8]
	inputs := data[10:]

	stacks := parseStacks(initialPart, 9)
	moves := parseMoves(inputs)

	for _, move := range moves {

		lastIndex := len(stacks[move.from]) - 1
		x := make([]string, 0)
		splitPoint := lastIndex + 1 - move.amount
		x, stacks[move.from] = stacks[move.from][splitPoint:], stacks[move.from][:splitPoint]

		for i := 0; i < len(x); i++ {
			stacks[move.to] = append(stacks[move.to], x[i])

		}

	}

	resultString := ""

	for _, stack := range stacks {
		resultString += stack[len(stack)-1]
	}
	fmt.Printf("Part Two: %v\n", resultString)
}
