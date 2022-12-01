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
