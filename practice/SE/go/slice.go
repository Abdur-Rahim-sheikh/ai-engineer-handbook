package main

import "fmt"

func main(){
	s:=[]int{1,3,9}

	s[0] = 5;
	s = append(s,12)

	fmt.Println(s, len(s), cap(s))

	var x []int;
	fmt.Println(x)
}