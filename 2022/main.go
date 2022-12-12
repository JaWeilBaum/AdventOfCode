package main

import (
	"aoc/code/day11"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_11.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n\n")
	day11.PartOne(inputDataSlice)
	day11.PartTwo(inputDataSlice)
}
