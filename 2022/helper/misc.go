package helper

import "strconv"

func AtoI(input string) int {
	value, _ := strconv.Atoi(input)
	return value
}

func AstoIs(input []string) []int {
	returnValues := make([]int, 0)
	for _, value := range input {
		returnValues = append(returnValues, AtoI(value))
	}
	return returnValues
}
