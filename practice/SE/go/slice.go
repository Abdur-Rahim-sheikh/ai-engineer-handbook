package main

import "fmt"

func main(){
	var x []int;
	x = append(x,1);
	x = append(x,2)
	x = append(x,3)

	y := x
    z := y
	x = append(x, 4)
	y = append(y, 5)
	x[0] = 10

	fmt.Println(x,len(x),cap(x))
	fmt.Println(y,len(y),cap(y))
	fmt.Println(z,len(z),cap(z))

	// var a []int;
	// tem:=0
	// for i:=0;i<2000;i++{
	// 	a = append(a,i)
	// 	if tem<cap(a){
	// 		fmt.Println(cap(a))
	// 		tem = cap(a)
	// 	}
	// }
}