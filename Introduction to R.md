# Introduction to R
*2016/5/25 Alvin*

##Data structure
###variable
*variable is global*
x <- 123

###vector
vector.x <- c(1:50)
vector.y <- 1:50
vector.z <- c(1, "c", FALSE)
*code style: using vector/vec/v as a prefix to mean vector*
*. is a valid variable name*
*c is a function for creating vector*
*vector is fast*
####Operate on vector
*add 1 for all elements in vector*
vector.x + 1



###matrix
matrix.x <- matrix(data = vector.x, nrow=5, ncol=10, byrow=FALSE)
matrix.y <- matrix(data = vector.x, nrow=5, ncol=12, byrow=FALSE)
*most used in algorithms*
*Usually, we use datafram. Dataframe allow every column to be
different type, but matrix only allow numbers*
matrix.x[1,2]
matrix.x[1,]



###dataframe
dataframe.x <- data.frame(age=c(1,2,3), name=c("x", "y", "z"))
dataframe.x[2]
dataframe.x[2,1]
dataframe.x$name

###list
list.x <- list(c(1:2), "x", 2, FALSE)
list.y <- list(value=c(1,23,4), "x")
*list's element is a 'object'*
*we could see it as a map, but you can define the key or not. if not
	,use 1,2,3 default*

###array
array.x <- vector.x
*array is a mutliple dimension matrix*

###factor
factor.x <- c(1,23,4,5,6,7)
factor.x <- factor(factor.x)
*factor will know the count the every element*


##function
###define a function
*you can write return or not*
*you can return function*
*you can define function in function body*
*R is a function programming languaage*
function.name <- function(param1 = default_value, parama2) {
	x <- 1
	vector.x
}


###frequently used functions
- summary : show the statistics
summary(vector.x)
- str : show the description, type...
str(vector.x)
- dim: show the dimension
- length
- names : show the names of OBJECT!
- order
- rank
- rbind: bind two dataframe into one. REQUIRE: both columns's type are
  equal and same number of columns.
- cbind: bind two dataframe into one. REQUEIRE: row's equal.
- rnorm : genreate normal distribution



##FAQ
###See help
Use ? + function namexs

##Operators
%% 取余数


##Reference
*All references are in folder ./references/*
- 2061042-dzone-refcardz-ressentials.pdf


##Practice
- Download stock information
- Do some statistics on the information
- Calculate the distribution of stock
？YQL/Yahoo finance API



