package day04

import (
	"fmt"
	"strconv"
	"strings"
)

type interval struct {
	start int
	end   int
}

func createInterval(input string) interval {
	parts := strings.Split(input, "-")
	start, _ := strconv.Atoi(parts[0])
	end, _ := strconv.Atoi(parts[1])
	newInterval := interval{start: start, end: end}
	return newInterval
}

func createIntervals(input string) []interval {
	parts := strings.Split(input, ",")
	return []interval{createInterval(parts[0]), createInterval(parts[1])}
}

func PartOne(data []string) {
	containedIntervals := 0
	for _, row := range data {
		intervals := createIntervals(row)

		contained := intervalContains(intervals[0], intervals[1])
		if contained {
			containedIntervals += 1
		}
		// fmt.Printf("%v %v Contains: %v \n", intervals[0], intervals[1], contained)
	}
	fmt.Printf("Part One: %v\n", containedIntervals)
}

func PartTwo(data []string) {
	overlappingIntervals := 0
	for _, row := range data {
		intervals := createIntervals(row)

		overlap := intervalOverlap(intervals[0], intervals[1])
		if overlap {
			overlappingIntervals += 1
		}
		// fmt.Printf("%v %v Overlapping: %v \n", intervals[0], intervals[1], overlap)
	}
	fmt.Printf("Part Two: %v\n", overlappingIntervals)
}

func intervalOverlap(interval1 interval, interval2 interval) bool {
	if interval1.end >= interval2.start && interval1.start <= interval2.end {
		return true
	} else if interval2.end >= interval1.start && interval2.start <= interval1.end {
		return true
	}
	return false
}

func intervalContains(interval1 interval, interval2 interval) bool {
	if interval1.start == interval2.start || interval1.end == interval2.end {
		// Start or end == then they contain each other!
		return true
	} else if interval1.start < interval2.start && interval1.end >= interval2.end {
		// Interval 2 contained by interval 2
		return true
	} else if interval1.start > interval2.start && interval2.end >= interval1.end {
		// Interval 1 contained by interval 2
		return true
	}
	return false
}
