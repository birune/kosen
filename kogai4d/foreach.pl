@a = ("brack", "blue", "red");

print "@a\n";

foreach $i (@a){
	$i = '[' . $i . ']';
}
print "@a\n";
