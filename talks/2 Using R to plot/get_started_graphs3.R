# if (FALSE) {
#   library(RColorBrewer)
#   n <- 7
#   mycolors <- brewer.pal(n, "Set1")
#   barplot(rep(1,n), col=mycolors)
# }
# 

n <- 10
mycolors <- rainbow(n)
#pie(rep(1, n), labels=mycolors, col=mycolors)
mygrays <- gray(0:n/n)
pie(rep(1, n), labels=mygrays, col=mygrays)