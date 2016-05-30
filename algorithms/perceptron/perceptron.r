## NOTE: the function in current file is not perceptron at all
## The intention we do this is to distinguish python & R
## You will find the model of lm or sgd in R gives a confused function for given data
## And this function is so different with Python's
## Why, does R make mistake?
## No!  The package we used here, although it is called linear model, But Please Note That It Is Regression Model Rather Than Classification Model.
## So it surely will give a different model. This is for regression!!!
## On the following topics&algorithms, I will write R script only when we talk about regression algorithms, because I think R is not good at do classification or something else. And one more thing, maybe I love python more.


library(sgd)

## This function will calculate the linear function using SGD
calModelInSGD <- function (features, classes) {

    model <- sgd(y ~ ., data=data.frame(y=classes, x=features), model="lm")
    summary(model)
    model$coefficients[1]
    ''

}

## This function will calculate the linear function using lm
calModelInLm <- function(features, classes) {

    ## A simple linear model
    model <- lm(classes ~ features$x + features$y)
    summary(model)

    sprintf(
        'The function of the model is:
       %f*feature_x + %f*feature_y + %f = 0' ,
       model$coefficients['features$x'],
       model$coefficients['features$y'],
       model$coefficients['(Intercept)'])
}


#The features&classes are same to the data in Py
features <- data.frame(x=c(-1, -2, 1, 2, 0), y=c(-1, -1, 1, 1, 0))
classes <- c(1,1,2,2,1)

cat(calModelInLm(features, classes))
