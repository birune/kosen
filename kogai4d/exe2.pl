@day = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");

@num = <STDIN>;
chomp(@num);

@sorted = sort @num;

for $i (@sorted){
	print "day[".$i."] : ".$day[$i]."\n";
}
