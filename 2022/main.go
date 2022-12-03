package main

import (
	"aoc/code/day03"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_03.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day03.PartOne(inputDataSlice)
	day03.PartTwo(inputDataSlice)
}
