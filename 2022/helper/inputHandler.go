package helper

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func ReadTxtFile(fileName string) string {
	content, error := os.ReadFile("data/" + fileName)

	if error != nil {
		fmt.Println(error)
	}
	return string(content)
}

func TxtFileToSliceOfStrings(content string, sep string) []string {
	return strings.Split(content, sep)
}

func TxtFileToSliceOfInt(content string, sep string) []int {
	rows := TxtFileToSliceOfStrings(content, sep)
	var intValue = make([]int, 0)
	for index, value := range rows {
		if len(value) == 0 {
			continue
		}
		intVar, err := strconv.Atoi(value)
		if err != nil {
			log.Println("Error @ index " + strconv.Itoa(index))
			log.Fatal(err)
		}
		intValue = append(intValue, intVar)
	}
	return intValue
}
