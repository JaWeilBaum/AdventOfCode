package main

import (
	"aoc/code/day04"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_04.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day04.PartOne(inputDataSlice)
	day04.PartTwo(inputDataSlice)
}
