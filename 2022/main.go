package main

import (
	"aoc/helper"
	"fmt"
)

func main() {
	fileContent := helper.ReadTxtFile("day_00.txt")
	rows := helper.TxtFileToSliceOfStrings(fileContent, "\n")
	fmt.Println("Welcome to advent of code 2022")

	for index, row := range rows {
		fmt.Printf("Row: %v Value: %v \n", index, row)
	}

	intRows := helper.TxtFileToSliceOfInt(fileContent, "\n")
	fmt.Println(intRows)
}
