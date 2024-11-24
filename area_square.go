package main
import "fmt"

func largest_area(x,y int) {
	var perfect_square int
	var i int
	i=0
	perfect_square=0
	while(i*i<y)
	{
		perfect_square=i*i
		i+=1
	}
	return perfect_square
}

func main(){
var side, tiles int
fmt.Print("Enter the value of the side of the square\n")
fmt.Scanln(&sides)
fmt.Print("Enter the number of tiles\n")
fmt.Scanln(&tiles)

var area int
area=largest_area(side,tiles)
fmt.Printf("Area of largest possible square is:%d\n",area)
}
