open COUNTI,"count.txt";
$count = <COUNTI>;
close COUNTI;

$count++;

open COUNTO,">count.txt";
print COUNTO $count;
close COUNTO;

$body = $body."あなたは $count 人目のお客様です\n";

$input = <STDIN>;

open OUT,">thread.txt";
print OUT $input;
close OUT;

open IN,"thread.txt";
while(<IN>){
	chomp $_;
	$body = $body . $_ . "\n";
}
close IN;

print $body;
