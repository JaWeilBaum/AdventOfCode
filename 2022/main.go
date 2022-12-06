package main

import (
	"aoc/code/day06"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_06.txt")
	//inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day06.PartOne(inputData)
	day06.PartTwo(inputData)
}
