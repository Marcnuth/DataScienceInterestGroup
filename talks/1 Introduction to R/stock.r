## In this file, we will use the data(stock.csv) to plot the histograms


## 1. Process Data
data.frompast <- read.csv(file='stock.csv', header=TRUE, sep=",")
summary(data.frompast)

## reoder the data, make it from past to now
data <- data[c(nrow(data.frompast):1),]
summary(data)

data.date.start <- toString(data$date[1])
data.date.start.year <- as.numeric(strsplit(data.date.start, "-")[[1]][1])
data.date.start.month <- as.numeric(strsplit(data.date.start, "-")[[1]][2])
data.date.start.day <- as.numeric(strsplit(data.date.start, "-")[[1]][3])


## 2. Plot graphs
par(mfrow = c(2, 2))

## 2.1 trend of closing price

## Why we do not use ts?
## Because the data is daily recorded.
##closeprice.ts <- ts(data$closePrice,frequency = 365, start=c(data.date.start.year, data.date.start.month))

plot(x=as.Date(data$date), y=data$closePrice, type="l", xlab="date", ylab="closing price", main="Trend of closing price")

## 2.2 histogram of closing price
hist(x=data$closePrice, xlab="closing price", breaks=nrow(data)/50, main="histogram of closing price(step=50)")


## 2.3 histogram of change amount
hist(x=as.numeric(as.character(data$changeAmount)), xlab="change amount", breaks=nrow(data)/20, main="histogram of change amount(step=20)")
hist(x=as.numeric(as.character(data$changeAmount)), xlab="change amount", breaks=nrow(data)/100, main="histogram of change amount(step=100)")





