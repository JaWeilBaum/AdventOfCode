package main

import (
	"aoc/code/day01"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_01.txt")
	inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	//day01.PartOne(inputDataSlice)
	day01.PartTwo(inputDataSlice)
}
