package main

import (
	"aoc/code/day07"
	"aoc/helper"
)

func main() {
	inputData := helper.ReadTxtFile("day_07.txt")
	//inputDataSlice := helper.StringToSliceOfStrings(inputData, "\n")
	day07.PartOne(inputData)
	day07.PartTwo(inputData)
}
