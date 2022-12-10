package day07

import (
	"aoc/helper"
	"fmt"
	"strconv"
	"strings"
)

type Item struct {
	name   string
	isFile bool
	size   int
}

func PartOne(data string) {
	commands := helper.StringToSliceOfStrings(data, "$")

	files := make(map[string]int)

	currentWorkingDir := "root"

	for _, command := range commands[1:] {
		// fmt.Printf("---- Current dir: %v\n", currentWorkingDir)
		originalCommand := "$" + command

		commandParts := helper.StringToSliceOfStrings(originalCommand, "\n")

		if commandParts[len(commandParts)-1] == "" {
			commandParts = commandParts[:len(commandParts)-1]
		}
		prompt := commandParts[0]
		// fmt.Printf("responseRows: %v Prompt: %v \n", len(commandParts)-1, prompt)

		if strings.Contains(prompt, "$ cd") {
			currentWorkingDir = updateDir(currentWorkingDir, prompt)
		} else if strings.Contains(prompt, "$ ls") {
			filesInDir := getFiles(commandParts[1:])
			// fmt.Printf("Files in dir: %v\n", filesInDir)
			allSubDirs := allDirectories(currentWorkingDir)
			for _, value := range filesInDir {
				updateMap(files, allSubDirs, value)
			}
		}
	}
	sum := 0
	for _, value := range files {
		if value < 100_000 {
			sum += value
		}
	}

	//fmt.Println(files)
	fmt.Printf("Part one: %v\n", sum)

	minimumDeletionDiskSpace := 30_000_000 - (70_000_000 - files["root"])

	smallestSizeValue := 70_000_000

	for _, value := range files {
		if value >= minimumDeletionDiskSpace && value < smallestSizeValue {
			smallestSizeValue = value
		}
	}
	fmt.Printf("Part two: %v\n", smallestSizeValue)
}

func getFiles(lines []string) map[string]int {
	files := make(map[string]int)
	for _, line := range lines {
		parts := strings.Split(line, " ")
		if parts[0] == "dir" {
			continue
		}
		size, _ := strconv.Atoi(parts[0])
		files[parts[1]] = size
	}
	return files
}

func allDirectories(directoryString string) []string {
	allDirs := make([]string, 0)
	dirParts := strings.Split(directoryString, "/")
	for i := 1; i < len(dirParts)+1; i++ {
		allDirs = append(allDirs, strings.Join(dirParts[0:i], "/"))
	}
	return allDirs
}

func updateDir(currentDir string, newCommand string) string {
	command := strings.Replace(newCommand, "$ cd ", "", 1)
	if command == "/" {
		return "root"
	} else if command == ".." {
		parts := strings.Split(currentDir, "/")
		return strings.Join(parts[:len(parts)-1], "/")
	} else {
		if currentDir == "" {
			return command
		}
		return currentDir + "/" + command
	}
}

func updateMap(dirSizeMap map[string]int, keys []string, newValue int) {
	for _, key := range keys {
		keyValue, exist := dirSizeMap[key]
		if exist {
			dirSizeMap[key] = keyValue + newValue
		} else {
			dirSizeMap[key] = newValue
		}
	}
}

func PartTwo(data string) {

}
