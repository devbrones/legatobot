function bzd(a,b,c)
{
	var d,e;
	d=czd((cVd(b),b),'([/\\\\\\.\\*\\+\\?\\|\\(\\)\\[\\]\\{\\}$^])','\\\\$1');
	e=czd(czd(NTc(c),'\\\\','\\\\\\\\'),'\\$','\\\\$');
	return czd(a,d,e)
}
