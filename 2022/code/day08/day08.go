package day08

import (
	"aoc/helper"
	"fmt"
	"strconv"
)

func PartOne(data []string) {
	grid := inputToGrid(data)
	visibleGrid := createEmptyGrid(len(grid), len(grid[0]))

	for i := 0; i < len(visibleGrid); i++ {
		for j := 0; j < len(visibleGrid[i]); j++ {
			if i == 0 || j == 0 || i == len(visibleGrid)-1 || j == len(visibleGrid[i])-1 {
				visibleGrid[i][j] = 1
			}
		}
	}

	for rowCounter := 0; rowCounter < len(grid); rowCounter++ {
		leftToRightStartTree := grid[rowCounter][0]
		leftToRightCurrentHeight := leftToRightStartTree

		rightToLeftStartTree := grid[rowCounter][len(grid[rowCounter])-1]
		rightToLeftCurrentHeight := rightToLeftStartTree
		// left -> right
		for columnCounter := 0; columnCounter < len(grid[rowCounter]); columnCounter++ {
			if leftToRightCurrentHeight < grid[rowCounter][columnCounter] {
				visibleGrid[rowCounter][columnCounter] = 1
				leftToRightCurrentHeight = grid[rowCounter][columnCounter]
			}
		}
		// right -> left
		for columnCounter := len(grid[rowCounter]) - 1; columnCounter > 0; columnCounter-- {
			if rightToLeftCurrentHeight < grid[rowCounter][columnCounter] {
				visibleGrid[rowCounter][columnCounter] = 1
				rightToLeftCurrentHeight = grid[rowCounter][columnCounter]
			}
		}
	}

	for columnCounter := 0; columnCounter < len(grid[0]); columnCounter++ {
		topToBottomCurrentHeight := grid[0][columnCounter]
		bottomToTopCurrentHeight := grid[len(grid)-1][columnCounter]

		for rowCounter := 0; rowCounter < len(grid); rowCounter++ {
			if topToBottomCurrentHeight < grid[rowCounter][columnCounter] {
				visibleGrid[rowCounter][columnCounter] = 1
				topToBottomCurrentHeight = grid[rowCounter][columnCounter]
			}
		}

		for rowCounter := len(grid) - 1; rowCounter > 0; rowCounter-- {
			if bottomToTopCurrentHeight < grid[rowCounter][columnCounter] {
				visibleGrid[rowCounter][columnCounter] = 1
				bottomToTopCurrentHeight = grid[rowCounter][columnCounter]
			}
		}
	}

	// fmt.Println(visibleGrid)

	result := 0

	for row := 0; row < len(visibleGrid); row++ {
		result += helper.Sum(visibleGrid[row])
	}
	fmt.Printf("Part One: %v\n", result)
}

func createEmptyGrid(numRows int, numColumns int) [][]int {
	grid := make([][]int, 0)
	for i := 0; i < numRows; i++ {
		row := make([]int, 0)
		for j := 0; j < numColumns; j++ {
			row = append(row, 0)
		}
		grid = append(grid, row)
	}
	return grid
}

func inputToGrid(data []string) [][]int {
	grid := make([][]int, 0)

	for _, row := range data {
		intRow := make([]int, 0)
		for _, element := range row {
			intValue, _ := strconv.Atoi(string(element))
			intRow = append(intRow, intValue)
		}
		grid = append(grid, intRow)
	}
	return grid
}

func scenicScoreForLocation(grid [][]int, rowIndex int, columnIndex int) int {
	row := make([]int, len(grid[rowIndex]))

	copy(row, grid[rowIndex])

	column := make([]int, 0)
	for i := 0; i < len(grid); i++ {
		column = append(column, grid[i][columnIndex])
	}
	treeHeight := grid[rowIndex][columnIndex]

	lToR := row[columnIndex+1:]
	rToL := row[:columnIndex]
	helper.Reverse(rToL)

	tToB := column[rowIndex+1:]
	bToT := column[:rowIndex]
	helper.Reverse(bToT)

	// fmt.Printf("LeftToRight %v\n", lToR)
	// fmt.Printf("lToR: VisibleTrees: %v\n", visibleTrees(treeHeight, lToR))
	// fmt.Printf("RightToLeft %v\n", rToL)
	// fmt.Printf("RtoL: VisibleTrees: %v\n", visibleTrees(treeHeight, rToL))
	//
	// fmt.Printf("TopToBottom %v\n", tToB)
	// fmt.Printf("tToB: VisibleTrees: %v\n", visibleTrees(treeHeight, tToB))
	// fmt.Printf("BottomToTop %v\n", bToT)
	// fmt.Printf("bToT: VisibleTrees: %v\n", visibleTrees(treeHeight, bToT))

	return visibleTrees(treeHeight, lToR) * visibleTrees(treeHeight, rToL) * visibleTrees(treeHeight, tToB) * visibleTrees(treeHeight, bToT)
}

func visibleTrees(startTreeHeight int, line []int) int {
	counter := 0
	for _, value := range line {
		// fmt.Println(value)
		if value < startTreeHeight {
			counter += 1
		} else {
			return counter + 1
		}
	}
	return counter
}

func PartTwo(data []string) {
	grid := inputToGrid(data)

	maxScore := 0

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			scoreAtLocation := scenicScoreForLocation(grid, i, j)
			fmt.Printf("(%v,%v) = %v\n", i, j, scoreAtLocation)
			if scoreAtLocation > maxScore {
				maxScore = scoreAtLocation
			}
		}
	}
	fmt.Printf("%v\n", scenicScoreForLocation(grid, 3, 2))
	fmt.Printf("Part Two: %v", maxScore)
}
