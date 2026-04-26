package main

import "fmt"

func main(){
	var x []int;
	x = append(x,1);
	x = append(x,2)
	x = append(x,3)

	y := x
	x = append(x,4)
	y = append(y, 5)
	x[0] = 10

	fmt.Println(x,y, cap(y))

	var z []int;
	tem:=0
	for i:=0;i<2000;i++{
		z = append(z,i)
		if tem<cap(z){
			fmt.Println(cap(z))
			tem = cap(z)
		}
	}
}