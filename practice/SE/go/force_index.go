
package main
import "fmt"

func main(){
	a:=[]int{1,2,3,4,5}
	b := a[1:4]
	// during slicing it can access the value of `a`
	// which was not necessarily it's but we cannot directly access it.
	// we will get runtime error.
	fmt.Println(b, b[:4])
	// fmt.Println(b[3])
}
