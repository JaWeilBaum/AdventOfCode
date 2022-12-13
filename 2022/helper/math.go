package helper

import (
	"fmt"
	"github.com/johncgriffin/overflow"
)

type Number interface {
	int | float32 | float64 | int64
}

func Sum[V Number](input []V) V {
	var result float64 = 0.0
	for _, value := range input {
		result = result + float64(value)
	}
	return V(result)
}

func Multi(input []int64) int64 {
	var result int64 = 1
	ok := false
	for _, value := range input {
		result, ok = overflow.Mul64(result, value)
		if !ok {
			fmt.Println()
		}
	}
	return result
}

func Reverse(input []int) {
	for i, j := 0, len(input)-1; i < j; i, j = i+1, j-1 {
		input[i], input[j] = input[j], input[i]
	}
}

func Contains[V comparable](slice []V, searchValue V) bool {
	for _, value := range slice {
		if value == searchValue {
			return true
		}
	}
	return false
}

func IndexOf[V comparable](slice []V, searchValue V) int {
	for index, value := range slice {
		if value == searchValue {
			return index
		}
	}
	return -1
}

// Stolen from https://siongui.github.io/2017/05/09/go-find-all-prime-factors-of-integer-number/
func PrimeFactors(n int64) (pfs []int64) {
	// Get the number of 2s that divide n

	for n%2 == 0 {
		pfs = append(pfs, 2)
		n = n / 2
	}

	// n must be odd at this point. so we can skip one element
	// (note i = i + 2)
	for i := int64(3); i*i <= n; i = i + 2 {
		// while i divides n, append i and divide n
		for n%i == 0 {
			pfs = append(pfs, i)
			n = n / i
		}
	}

	// This condition is to handle the case when n is a prime number
	// greater than 2
	if n > 2 {
		pfs = append(pfs, n)
	}

	if pfs == nil {
		fmt.Println()
	}

	return
}
