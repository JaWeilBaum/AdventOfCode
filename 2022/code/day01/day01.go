package day01

import (
	"aoc/helper"
	"fmt"
	"log"
	"sort"
	"strconv"
)

func PartOne(data []string) {

	count := 0
	maxCount := 0
	for _, value := range data {
		if value == "" {
			if count > maxCount {
				maxCount = count
			}
			count = 0
		} else {
			intVar, err := strconv.Atoi(value)
			if err != nil {
				fmt.Println("Error")
				log.Fatal(err)
			}
			count += intVar
		}
	}
	fmt.Printf("Max cal value: %v", maxCount)
}

func PartTwo(data []string) {

	count := 0
	maxCount := 0

	sumValues := make([]int, 0)

	for _, value := range data {
		if value == "" {
			if count > maxCount {
				maxCount = count
			}
			sumValues = append(sumValues, count)
			count = 0
		} else {
			intVar, err := strconv.Atoi(value)
			if err != nil {
				fmt.Println("Error")
				log.Fatal(err)
			}
			count += intVar
		}
	}
	//MAGIC
	sort.Sort(sort.Reverse(sort.IntSlice(sumValues)))

	fmt.Printf("%v + %v + %v = %v", sumValues[0], sumValues[1], sumValues[2], helper.Sum(sumValues[0:3]))

}
