function JTc(a,b,c)
{
	var d=HTc,i;
	var e=d[a];
	var g=e instanceof Array?e[0]:null;
	if(e&&!g)
	{
		_=e
	}
	else
	{
		_=(i=b&&b.prototype,!i&&(i=HTc[b]),MTc(i));
		_.Xp=c;
		!b&&(_.Yp=OTc);
		d[a]=_
	}
	for(var h=3;h<arguments.length;++h)
	{
		arguments[h].prototype=_
	}
	g&&(_.Wp=g)
}
