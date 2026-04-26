package main

import "fmt"

func main(){
	var x []string;
	x = append(x,"abir");
	x = append(x,"pratice")

	y := x
    z := y
	x = append(x, "expert")
	y = append(y, "beginner")
	x[0] = "nadia"

	fmt.Println(x,len(x),cap(x))
	fmt.Println(y,len(y),cap(y))
	fmt.Println(z,len(z),cap(z))
}