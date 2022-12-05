package main

import (
	"aoc/code/day05"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_05.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day05.PartOne(inputDataSlice)
	day05.PartTwo(inputDataSlice)
}
