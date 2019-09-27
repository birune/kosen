sub above_average{
	my($sum, $count, $ave, $result, $i);
	$sum = 0;
	$count = 0;
	for $i (@_){
		$sum += $i;
	}
	$count = scalar @_;
	$ave = $sum / $count;
	$result[0] = "ave";
	$result[1] = " = ";
	$result[2] = $ave;
	$result[3] = "\n";
	$result[4] = "result: ";
	
	for $i (@_){
		if($i >= $ave){
			push @result, $i;
		}
	}
	
	return @result;
}

@result = &above_average(10, 80, 32, 58, 13, 3);
print "@result\n";
