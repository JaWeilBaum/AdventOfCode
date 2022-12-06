package day06

import "fmt"

func PartOne(data string) {
	inputData := data
	currentIndex := 4
	for i := 0; i < len(inputData)-4; i++ {

		partString := inputData[i : i+4]
		isStringUnique := uniqueChars((partString))

		if isStringUnique {
			break
		}

		//fmt.Printf("%v unique: %v\n", partString, uniqueChars(partString))
		currentIndex++
	}

	fmt.Printf("Part One: %v\n", currentIndex)
}

func uniqueChars(inputString string) bool {
	hashMap := make(map[string]int)
	for _, char := range inputString {
		value, exists := hashMap[string(char)]
		if exists {
			hashMap[string(char)] = value + 1
		} else {
			hashMap[string(char)] = 1
		}
	}

	returnValue := true
	for _, value := range hashMap {
		returnValue = returnValue && value == 1
	}
	return returnValue
}

func PartTwo(data string) {
	inputData := data
	currentIndex := 14
	for i := 0; i < len(inputData)-14; i++ {

		partString := inputData[i : i+14]
		isStringUnique := uniqueChars((partString))

		if isStringUnique {
			break
		}

		//fmt.Printf("%v unique: %v\n", partString, uniqueChars(partString))
		currentIndex++
	}

	fmt.Printf("Part One: %v\n", currentIndex)
}
