package main

import (
	"aoc/code/day08"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_08.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day08.PartOne(inputDataSlice)
	day08.PartTwo(inputDataSlice)
}
