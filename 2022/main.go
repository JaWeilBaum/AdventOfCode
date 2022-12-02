package main

import (
	"aoc/code/day02"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_02.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day02.PartOne(inputDataSlice)
	day02.PartTwo(inputDataSlice)
}
