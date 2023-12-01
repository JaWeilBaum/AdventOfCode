package day12

import (
	"fmt"
	"math"
)

func createGrid(data []string) [][]int {
	grid := make([][]int, 0)
	for _, row := range data {
		rowChars := make([]int, 0)
		for _, char := range row {
			value := int(char) - 97
			if string(char) == "S" {
				value = -1
			} else if string(char) == "E" {
				value = math.MaxInt32
			}
			rowChars = append(rowChars, value)
		}
		grid = append(grid, rowChars)
	}
	return grid
}

func createEmptyGrid(x int, y int) [][]int {
	grid := make([][]int, 0)
	for i := 0; i < y; i++ {
		row := make([]int, 0)
		for j := 0; j < x; j++ {
			row = append(row, math.MaxInt64-1)
		}
		grid = append(grid, row)
	}
	return grid
}

func PartOne(data []string) {
	grid := createGrid(data)

	for _, row := range grid {
		fmt.Println(row)
	}
}

func PartTwo(data []string) {

}
