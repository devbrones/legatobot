function rzd(a)
{
	var b;
	b=0;
	while(0<=(b=a.indexOf('\\',b)))
	{
		jVd(b+1,a.length);
		a.charCodeAt(b+1)==36?(a=a.substr(0,b)+'$'+hzd(a,++b)):(a=a.substr(0,b)+(''+hzd(a,++b)))
	}
	return a
}
