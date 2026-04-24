# Interview preperations for Golang

### Resources

- [Go with habib (beginner)](https://www.youtube.com/playlist?list=PLpCqPSEm2Xe8sEY2haMDUVgwbkIs5NCJI)

## Content

1. [Internal Memory](#internal-memory)
2. [Closure](#closure)

#### Internal Memory

There are 4 basic types of memory

- **Code segment**
  - Functions, constant are kept here as binary
- **Data segment**
  - All global veriables are kept here
- **Stack**
  - During runtime the running blocks (actually only reference of the code segment) and scoped variables are kept here
  - as soon as the function is done that part is removed from stack
- **Heap**
  - It keeps the value **escaped** during execution of closure, more later
  - Managed by gorutine garbage collector.

#### Closure

If a function's inner function needs a variable from that function, then it keeps the
varialbe outside of scope, called closure.

```go
int a=3;
const PI=3.1416;

func outer(){
    int b=8;
    int result = 0;

    func inner(){
        result:=result+a+b;
        return result;
    }
    return inner;
}

func main(){
    x:=outer()
    x()
    x()
    y:=outer()
    y()
}
```

Here during compilation,

- Code Block has: Const PI, outer function, main function
- Data block has: variable a

Then during execution,
in Stack:

- finds init -> not found no isue
- find main -> found
  - finds outer -> execute returns inner, escapes `b and result to heap`
  - executes inner taking data b and result from heap (by the way currently outer function is not present in stack just those escapped values)
  - executes inner second time
  - finds outer again -> escapes the b and result to heap again
  - gets another inner
  - executes that another inner again
  - exits main
