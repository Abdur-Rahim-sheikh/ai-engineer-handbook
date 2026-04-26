package main

import "fmt"
func changeSlice(a []int) []int{
	a = append(a,11)
	a[0] = 10
	return a
}
func main(){
	x:=[]int{1,2,3}
	x = append(x,6)
	x = append(x,7)
	a := x[2:]

	y := changeSlice(a)

	fmt.Println(x)
	fmt.Println(y)
}