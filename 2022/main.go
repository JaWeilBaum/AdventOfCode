package main

import (
	"aoc/code/day10"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_10.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day10.PartOne(inputDataSlice)
	day10.PartTwo(inputDataSlice)
}
