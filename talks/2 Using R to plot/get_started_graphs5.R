plot(dose, drugA, type="b",
     col="red", lty=2, pch=2, lwd=2,
     main="Clinical Trials for Drug A",
     sub="This is hypothetical data",
     xlab="Dosage", ylab="Drug Response",
     xlim=c(0, 60), ylim=c(0, 70))

title(main="My Title", col.main="red",
       sub="My Subtitle", col.sub="blue",
       xlab="My X label", ylab="My Y label",
       col.lab="green", cex.lab=0.75)