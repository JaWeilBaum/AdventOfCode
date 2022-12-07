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

	currentWorkingDir := ""

	files := make(map[string]int)

	for _, command := range commands[1:] {
		fmt.Printf("---- Current dir: %v\n", currentWorkingDir)
		originalCommand := "$" + command

		commandParts := helper.StringToSliceOfStrings(originalCommand, "\n")

		if commandParts[len(commandParts)-1] == "" {
			commandParts = commandParts[:len(commandParts)-1]
		}
		prompt := commandParts[0]
		fmt.Printf("responseRows: %v Prompt: %v \n", len(commandParts)-1, prompt)

		if strings.Contains(prompt, "$ cd") {
			currentWorkingDir = updateDir(currentWorkingDir, prompt)
		} else if strings.Contains(prompt, "$ ls") {
			filesInDir := getFiles(commandParts[1:])
			fmt.Printf("Files in dir: %v\n", filesInDir)
			for key, value := range filesInDir {
				fileKey := currentWorkingDir + "/" + key
				if currentWorkingDir == "" {
					fileKey = key
				}
				files[fileKey] = value
			}
		}
	}
	fmt.Println(currentWorkingDir)
	// Do divide and conquer here!
	for key, value := range files {
		if strings.Contains(key, "d/") {
			fmt.Printf("%v = %v\n", key, value)
		}
	}
}

func getFiles(lines []string) map[string]int {
	files := make(map[string]int)
	for _, line := range lines {
		parts := strings.Split(line, " ")
		if parts[0] == "dir" {
			files[parts[1]] = -1
			continue
		}
		size, _ := strconv.Atoi(parts[0])
		files[parts[1]] = size
	}
	return files
}

func updateDir(currentDir string, newCommand string) string {
	command := strings.Replace(newCommand, "$ cd ", "", 1)
	if command == "/" {
		return ""
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

func PartTwo(data string) {

}
