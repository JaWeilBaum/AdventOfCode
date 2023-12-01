package main

import (
	"aoc/code/day12"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_12.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day12.PartOne(inputDataSlice)
	day12.PartTwo(inputDataSlice)
}
