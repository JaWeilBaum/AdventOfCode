package main

import (
	"aoc/code/day09"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_09.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day09.PartOne(inputDataSlice)
	day09.PartTwo(inputDataSlice)
}
