package helper

type Number interface {
	int | float32 | float64
}

func Sum[V Number](input []V) V {
	var result float64 = 0.0
	for _, value := range input {
		result = result + float64(value)
	}
	return V(result)
}

func Reverse(input []int) {
	for i, j := 0, len(input)-1; i < j; i, j = i+1, j-1 {
		input[i], input[j] = input[j], input[i]
	}
}
