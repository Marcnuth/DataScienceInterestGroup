# Specifies data
x <- c(1:10)
y <- x
z <- 10/x
opar <- par(no.readonly=TRUE)

# Increases margins
par(mar=c(5, 4, 4, 8) + 0.1)

# Plots x vs. y, suppressing annotations
plot(x, y, type="b",
     pch=21, col="red",
     yaxt="n", lty=3, ann=FALSE)
# Adds an x versus 1/x line
lines(x, z, type="b", pch=22, col="blue", lty=2)

# draw axes
axis(2, at=x, labels=x, col.axis="red", las=2)
axis(4, at=z, labels=round(z, digits=2),
     col.axis="blue", las=2, cex.axis=1.2, tck=-.01)

#Adds titles and text
mtext("y=1/x", side=4, line=3, cex.lab=1, las=2, col="blue")
title("An Example of Creative Axes",
      xlab="X values",
      ylab="Y=X")

par(opar)