package day09

import (
	"aoc/helper"
	"fmt"
	"math"
	"strconv"
	"strings"
)

type FollowUpMethod int64

const (
	Straight FollowUpMethod = 1
	Diagonal                = 2
)

type Point struct {
	x                int
	y                int
	visitedLocations []string
}

func PartOne(data []string) {

	hPosition := Point{0, 0, make([]string, 0)}
	hPosition.visitedLocations = append(hPosition.visitedLocations, "0,0")

	tPosition := Point{0, 0, make([]string, 0)}
	tPosition.visitedLocations = append(tPosition.visitedLocations, "0,0")

	for _, row := range data {
		fmt.Println("------------------------------------------------")
		parts := strings.Split(row, " ")
		direction := parts[0]
		distance, _ := strconv.Atoi(parts[1])
		performMove(direction, distance, &hPosition, &tPosition)
	}
	//fmt.Println(tPosition.visitedLocations)
}

func performMove(direction string, distance int, hPosition *Point, tPosition *Point) {
	for i := 0; i < distance; i++ {
		fmt.Printf("Direction %v distance %v\n", direction, distance)
		hX, hY := directionMove(direction)
		hPosition.x += hX
		hPosition.y += hY

		tX, tY := determineFollowUpMethod(*hPosition, *tPosition)
		tPosition.x += tX
		tPosition.y += tY
		newLocationHash := strconv.Itoa(tPosition.x) + "," + strconv.Itoa(tPosition.y)
		if !helper.Contains(tPosition.visitedLocations, newLocationHash) {
			tPosition.visitedLocations = append(tPosition.visitedLocations, newLocationHash)
		}
		fmt.Printf("hPosition: (%v, %v) = %v\ntPosition: (%v, %v) = %v\n", hPosition.x, hPosition.y, len(hPosition.visitedLocations), tPosition.x, tPosition.y, len(tPosition.visitedLocations))
	}
}

func performMoves(direction string, distance int, hPosition *Point, tPositions []*Point) {
	for i := 0; i < distance; i++ {
		fmt.Printf("Direction %v distance %v\n", direction, distance)
		hX, hY := directionMove(direction)
		hPosition.x += hX
		hPosition.y += hY
		for knotIndex, tPosition := range tPositions {
			if knotIndex == 0 {
				tX, tY := determineFollowUpMethod(*hPosition, *tPosition)
				tPosition.x += tX
				tPosition.y += tY
			} else {
				tX, tY := determineFollowUpMethod(*tPositions[knotIndex-1], *tPosition)
				tPosition.x += tX
				tPosition.y += tY
			}
			newLocationHash := strconv.Itoa(tPosition.x) + "," + strconv.Itoa(tPosition.y)
			if !helper.Contains(tPosition.visitedLocations, newLocationHash) {
				fmt.Printf("Knot: %v moved!", knotIndex+1)
				tPosition.visitedLocations = append(tPosition.visitedLocations, newLocationHash)
			}
		}
		fmt.Printf("hPosition: (%v, %v) = %v\ntPosition: (%v, %v) = %v\n", hPosition.x, hPosition.y, len(hPosition.visitedLocations), tPositions[8].x, tPositions[8].y, len(tPositions[8].visitedLocations))
	}
}

func directionMove(direction string) (int, int) {
	if direction == "R" {
		return 1, 0
	} else if direction == "L" {
		return -1, 0
	} else if direction == "U" {
		return 0, 1
	} else if direction == "D" {
		return 0, -1
	}
	return 0, 0
}

func determineFollowUpMethod(pos1 Point, pos2 Point) (int, int) {
	yDiff := pos1.y - pos2.y
	xDiff := pos1.x - pos2.x
	if xDiff == 0 && math.Abs(float64(yDiff)) > 1 {
		fmt.Println(">>> Same Column")
		if yDiff > 1 {
			return 0, 1
		} else if yDiff < -1 {
			return 0, -1
		}
	} else if yDiff == 0 && math.Abs(float64(xDiff)) > 1 {
		fmt.Println(">>> Same Row")
		if xDiff > 1 {
			return 1, 0
		} else if xDiff < -1 {
			return -1, 0
		}
	} else if math.Abs(float64(yDiff)) == 1 && math.Abs(float64(xDiff)) == 1 {
		fmt.Println(">>> Not moving - still adjacent!")
		return 0, 0
	} else if xDiff >= 1 && yDiff >= 1 {
		fmt.Println(">>> Diagonal Top Right")
		return 1, 1
	} else if xDiff >= 1 && yDiff <= -1 {
		fmt.Println(">>> Diagonal Bottom Right")
		return 1, -1
	} else if xDiff <= -1 && yDiff >= 1 {
		fmt.Println(">>> Diagonal Top Left")
		return -1, 1
	} else if xDiff <= -1 && yDiff <= -1 {
		fmt.Println(">>> Diagonal Bottom Left")
		return -1, -1
	}
	fmt.Println(">>> Not moving - still adjacent!")
	return 0, 0
}

func PartTwo(data []string) {
	hPosition := Point{0, 0, make([]string, 0)}
	hPosition.visitedLocations = append(hPosition.visitedLocations, "0,0")

	tPositions := make([]*Point, 0)

	for i := 0; i < 9; i++ {
		newTailPosition := Point{0, 0, make([]string, 0)}
		newTailPosition.visitedLocations = append(newTailPosition.visitedLocations, "0,0")
		tPositions = append(tPositions, &newTailPosition)
	}

	for _, row := range data {
		fmt.Println("------------------------------------------------")
		parts := strings.Split(row, " ")
		direction := parts[0]
		distance, _ := strconv.Atoi(parts[1])
		performMoves(direction, distance, &hPosition, tPositions)
	}
	fmt.Println(len(tPositions[8].visitedLocations))
}
