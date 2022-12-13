package day11

import (
	"aoc/helper"
	"fmt"
	"strings"
)

type PrimeMonkey struct {
	items             [][]int64
	plus              bool
	operationValue    int
	testValue         int
	trueNextIndex     int
	falseNextIndex    int
	numInspectedItems int
}

type Monkey struct {
	items             []int64
	plus              bool
	operationValue    int
	testValue         int
	trueNextIndex     int
	falseNextIndex    int
	numInspectedItems int
}

func parsePrimeMonkeyInformation(data string) PrimeMonkey {
	parts := strings.Split(data, "\n")
	itemsString := strings.Replace(parts[1], "  Starting items: ", "", 1)
	items := helper.AstoIs(strings.Split(itemsString, ", "))
	itemsAsPrimes := make([][]int64, 0)
	for _, value := range items {
		itemsAsPrimes = append(itemsAsPrimes, helper.PrimeFactors(int64(value)))
	}
	operationString := strings.Split(strings.Replace(parts[2], "  Operation: new = old ", "", 1), " ")
	operation := operationString[0] == "+"
	operationValue := helper.AtoI(operationString[1])
	testString := helper.AtoI(strings.Replace(parts[3], "  Test: divisible by ", "", 1))
	trueString := helper.AtoI(strings.Replace(parts[4], "    If true: throw to monkey ", "", 1))
	falseString := helper.AtoI(strings.Replace(parts[5], "    If false: throw to monkey ", "", 1))
	return PrimeMonkey{items: itemsAsPrimes, plus: operation, operationValue: operationValue, testValue: testString, trueNextIndex: trueString, falseNextIndex: falseString, numInspectedItems: 0}
}

func parseMonkeyInformation(data string) Monkey {
	parts := strings.Split(data, "\n")
	itemsString := strings.Replace(parts[1], "  Starting items: ", "", 1)
	items := helper.AstoIs(strings.Split(itemsString, ", "))
	itemsAsPrimes := make([]int64, 0)
	for _, value := range items {
		itemsAsPrimes = append(itemsAsPrimes, int64(value))
	}
	operationString := strings.Split(strings.Replace(parts[2], "  Operation: new = old ", "", 1), " ")
	operation := operationString[0] == "+"
	operationValue := helper.AtoI(operationString[1])
	testString := helper.AtoI(strings.Replace(parts[3], "  Test: divisible by ", "", 1))
	trueString := helper.AtoI(strings.Replace(parts[4], "    If true: throw to monkey ", "", 1))
	falseString := helper.AtoI(strings.Replace(parts[5], "    If false: throw to monkey ", "", 1))
	return Monkey{items: itemsAsPrimes, plus: operation, operationValue: operationValue, testValue: testString, trueNextIndex: trueString, falseNextIndex: falseString, numInspectedItems: 0}
}

func simulatePrimeMonkey(monkey *PrimeMonkey) map[int][][]int64 {

	newItemDistribution := map[int][][]int64{
		0: make([][]int64, 0),
		1: make([][]int64, 0),
		2: make([][]int64, 0),
		3: make([][]int64, 0),
		4: make([][]int64, 0),
		5: make([][]int64, 0),
		6: make([][]int64, 0),
		7: make([][]int64, 0),
	}

	for _, value := range monkey.items {
		newValue := make([]int64, len(value))
		copy(newValue, value)
		if monkey.operationValue == 0 {
			// newValue *= newValue
			newValue = append(newValue, newValue...)
		} else if monkey.plus {
			trueValue := helper.Multi(newValue)
			trueValue += int64(monkey.operationValue)
			newValue = helper.PrimeFactors(trueValue)
		} else {
			// newValue *= monkey.operationValue
			newValue = append(newValue, int64(monkey.operationValue))
		}
		// newValue = newValue / 3
		indexOfThree := helper.IndexOf(newValue, 3)
		if indexOfThree != -1 {
			newValue = append(newValue[:indexOfThree], newValue[indexOfThree+1:]...)
		} else {
			testValue := helper.Multi(newValue)
			testValue = testValue / 3
			newValue = helper.PrimeFactors(testValue)
		}

		newIdx := monkey.falseNextIndex

		// newValue%monkey.testValue == 0
		if helper.Contains(newValue, int64(monkey.testValue)) {
			newIdx = monkey.trueNextIndex
		}
		newItemDistribution[newIdx] = append(newItemDistribution[newIdx], newValue)
	}
	// fmt.Println(newItemDistribution)
	monkey.numInspectedItems += len(monkey.items)
	monkey.items = make([][]int64, 0)
	return newItemDistribution
}

func simulateMonkey(monkey *Monkey, ggt int) map[int][]int64 {

	newItemDistribution := map[int][]int64{
		0: make([]int64, 0),
		1: make([]int64, 0),
		2: make([]int64, 0),
		3: make([]int64, 0),
		4: make([]int64, 0),
		5: make([]int64, 0),
		6: make([]int64, 0),
		7: make([]int64, 0),
	}

	for _, value := range monkey.items {
		newValue := value
		if monkey.operationValue == 0 {
			newValue *= newValue
		} else if monkey.plus {
			newValue += int64(monkey.operationValue)
		} else {
			newValue *= int64(monkey.operationValue)
		}

		newIdx := monkey.falseNextIndex

		// Keep the numbers small with the multiplication of all test variables.
		// This will ensure that all numbers will contain their property of being
		// div by the test value with the expected rest, while keeping the numbers
		// <= than the product of these numbers.
		newValue = newValue % int64(ggt)

		mod := newValue % int64(monkey.testValue)
		if mod == 0 {
			newIdx = monkey.trueNextIndex
		}
		newItemDistribution[newIdx] = append(newItemDistribution[newIdx], newValue)
	}
	// fmt.Println(newItemDistribution)
	monkey.numInspectedItems += len(monkey.items)
	monkey.items = make([]int64, 0)
	return newItemDistribution
}

func PartOne(data []string) {

	monkeys := make([]PrimeMonkey, 0)

	for _, monkeyInfo := range data {
		monkeys = append(monkeys, parsePrimeMonkeyInformation(monkeyInfo))
	}

	// Don't use for a lot of iterations, int will overflow and Go just don't care...
	for i := 0; i < 20; i++ {
		for j := 0; j < len(data); j++ {
			newItems := simulatePrimeMonkey(&monkeys[j])

			for key, value := range newItems {
				if len(value) == 0 {
					continue
				}
				for _, item := range value {
					monkeys[key].items = append(monkeys[key].items, item)
				}
			}
		}
	}
	fmt.Println("Part One")
	for idx, monkey := range monkeys {
		fmt.Printf("Monkey %v inspectedItems %v\n", idx, monkey.numInspectedItems)
	}
}

func PartTwo(data []string) {
	monkeys := make([]Monkey, 0)

	ggt := 1

	for _, monkeyInfo := range data {
		monkey := parseMonkeyInformation(monkeyInfo)
		monkeys = append(monkeys, monkey)
		ggt *= monkey.testValue
	}

	for i := 0; i < 10_000; i++ {
		for j := 0; j < len(data); j++ {
			newItems := simulateMonkey(&monkeys[j], ggt)

			for key, value := range newItems {
				if len(value) == 0 {
					continue
				}
				for _, item := range value {
					monkeys[key].items = append(monkeys[key].items, item)
				}
			}
		}
	}
	fmt.Println("Part Two")
	for idx, monkey := range monkeys {
		fmt.Printf("Monkey %v inspectedItems %v\n", idx, monkey.numInspectedItems)
	}
}
