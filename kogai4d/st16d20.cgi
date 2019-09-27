#!/usr/bin/perl
use CGI;
$cgi = CGI->new();

$title = "Hello!";

foreach $key(sort keys %ENV){
	$body = $body . "$key:$ENV{$key}<br>\n";
}
open COUNTI,"st16d20_count.txt";
$count = <COUNTI>;
close COUNTI;

$count++;

open COUNTO,">st16d20_count.txt";
print COUNTO $count;
close COUNTO;

$body = $body."あなたは $count 人目のお客様です<br>\n";

if($cgi->param("send") eq "送信"){
	$body = $body . $cgi->param("message") . " が入力されました<br>\n";
}

open IN,"st16d20_thread.txt";
@lines = <IN>;
close IN;
unshift @lines, $cgi->param("message")."<br>\n";

open OUT,">st16d20_thread.txt";
print OUT @lines; 
close OUT;
foreach $in(@lines){
	$body = $body.$in;
}

print << "EOT";
Content-Type: text/html

<html>
<head><meta charset= "UTF-8" />
<title>$title</title>
</head>
<body>

<form method="POST" action="st16d20.cgi">
<input type="text" name="message">
<input type="submit" name="send" value="送信">
<input type="reset" name="reset" value="取消">
</form>

$body
</body>
</html>
EOT
