package day11

import (
	"aoc/helper"
	"fmt"
	"strings"
)

type Monkey struct {
	items             []int
	plus              bool
	operationValue    int
	testValue         int
	trueNextIndex     int
	falseNextIndex    int
	numInspectedItems int
}

func parseMonkeyInformation(data string) Monkey {
	parts := strings.Split(data, "\n")
	itemsString := strings.Replace(parts[1], "  Starting items: ", "", 1)
	items := helper.AstoIs(strings.Split(itemsString, ", "))
	operationString := strings.Split(strings.Replace(parts[2], "  Operation: new = old ", "", 1), " ")
	operation := operationString[0] == "+"
	operationValue := helper.AtoI(operationString[1])
	testString := helper.AtoI(strings.Replace(parts[3], "  Test: divisible by ", "", 1))
	trueString := helper.AtoI(strings.Replace(parts[4], "    If true: throw to monkey ", "", 1))
	falseString := helper.AtoI(strings.Replace(parts[5], "    If false: throw to monkey ", "", 1))
	return Monkey{items: items, plus: operation, operationValue: operationValue, testValue: testString, trueNextIndex: trueString, falseNextIndex: falseString, numInspectedItems: 0}
}

func simulateMonkey(monkey *Monkey) map[int][]int {

	newItemDistribution := map[int][]int{
		0: make([]int, 0),
		1: make([]int, 0),
		2: make([]int, 0),
		3: make([]int, 0),
		4: make([]int, 0),
		5: make([]int, 0),
		6: make([]int, 0),
		7: make([]int, 0),
	}

	for _, value := range monkey.items {
		newValue := value
		if monkey.operationValue == 0 {
			newValue *= newValue
		} else if monkey.plus {
			newValue += monkey.operationValue
		} else {
			newValue *= monkey.operationValue
		}
		newValue = newValue / 3

		newIdx := monkey.falseNextIndex
		if newValue%monkey.testValue == 0 {
			newIdx = monkey.trueNextIndex
		}
		newItemDistribution[newIdx] = append(newItemDistribution[newIdx], newValue)
	}
	fmt.Println(newItemDistribution)
	monkey.numInspectedItems += len(monkey.items)
	monkey.items = []int{}
	return newItemDistribution
}

func PartOne(data []string) {

	monkeys := make([]Monkey, 0)

	for _, monkeyInfo := range data {
		monkeys = append(monkeys, parseMonkeyInformation(monkeyInfo))
	}

	for i := 0; i < 20; i++ {
		for j := 0; j < len(data); j++ {
			newItems := simulateMonkey(&monkeys[j])

			for key, value := range newItems {
				if len(value) == 0 {
					continue
				}
				for _, item := range value {
					monkeys[key].items = append(monkeys[key].items, item)
				}
			}

			//fmt.Println(newItems)
		}
		//fmt.Println()
	}
	for idx, monkey := range monkeys {
		fmt.Printf("Monkey %v inspectedItems %v\n", idx, monkey.numInspectedItems)
	}
}

func PartTwo(data []string) {

}
