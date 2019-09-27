print "start >>> ";
$start = <STDIN>;
chomp($start);
print "end >>> ";
$end = <STDIN>;
chomp($end);

$sum = 0;

while($start <= $end){
	$sum += $start;
	$start++;
}

print "sum = $sum\n";
