open MYFILE, "ls -R @ARGV |";
while(<MYFILE>){
	chomp $_;
	if(@match = ($_ =~ /(.+):$/)){
		$dir = $match[0];
	}elsif($_ =~ /^$/){
	}else{
		$file = $dir."/".$_;
		print "$file\n";
	}
}
close MYFILE;
		
