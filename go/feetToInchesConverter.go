/* Go: SoloLearn

Feet To Inches Converter

You need to create a program that converts feet to inches and outputs the resulting value.
The feet value is provided as the input to the program.
1 foot = 12 inches.

Sample Input:
5

Sample Output:
60


The input is an integer.


SoloLearn (2023) Feet To Inches Converter: https://www.sololearn.com

*/

package main

import "fmt"

func main() {
	var input int
	fmt.Scanln(&input)
	fmt.Println(input * 12)
}
