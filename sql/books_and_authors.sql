/* SQL: SoloLearn

Books and Authors


You are working with a library database that stores data on books. 
The Books table has the columns id, name, year, author_id. 
The author_id column connects to the Authors table, which stores the id, name columns for the book authors. 
 
You need to select all the books with their authors, ordered by the author name alphabetically, then by the year in ascending order. 
The result set should contain only 3 columns: the book name, year and its author (name the column author). 


Use the full column names, as both tables have a column called name. 


SoloLearn (2023) Books and Authors: https://www.sololearn.com

*/


SELECT 
	Books.name,
	year,
	Authors.name AS author
FROM
	Books,
	Authors
WHERE Authors.id = Books.author_id
ORDER BY 
	Authors.name, 
	year ASC;

	
	
