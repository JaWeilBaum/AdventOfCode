package day10

import (
	"aoc/helper"
	"fmt"
	"strconv"
	"strings"
)

func PartOne(data []string) {

	instructionQueue := createInstructionList(data)

	relevantCycles := []int{20, 60, 100, 140, 180, 220}

	returnValue := 0

	for _, multi := range relevantCycles {
		returnValue += helper.Sum(instructionQueue[:multi]) * multi
	}
	fmt.Printf("Part One: %v\n", returnValue)
}

func createInstructionList(data []string) []int {
	instructionQueue := []int{1}
	//value := 1

	for _, instruction := range data {
		//fmt.Printf("#: %v ints: %v\n", instructionIndex+1, instruction)

		if strings.Contains(instruction, "addx") {
			parts := strings.Split(instruction, " ")
			opValue, _ := strconv.Atoi(parts[1])
			instructionQueue = append(instructionQueue, 0, opValue)
		} else if strings.Contains(instruction, "noop") {
			instructionQueue = append(instructionQueue, 0)
		}
	}
	return instructionQueue
}

func PartTwo(data []string) {

	instructionQueue := createInstructionList(data)[2:]
	instructionQueue = append(instructionQueue, 0)
	sprintPosition := 1
	pixelCounter := 1
	for cycleNumber, value := range instructionQueue {
		//fmt.Printf("Start cycle: %v, inst: %v\nDrawing Pixel: %v\n", cycleNumber+1, value, pixelCounter)
		if (cycleNumber+1-1)%40 <= sprintPosition && sprintPosition <= (cycleNumber+1+1)%40 {
			fmt.Printf("#")
		} else {
			fmt.Printf(".")
		}
		sprintPosition += value
		pixelCounter++
		if (cycleNumber+1)%40 == 0 {
			fmt.Println()
		}
	}

}
