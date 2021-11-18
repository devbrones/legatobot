
// this part alledgedly generates the url


function QPk(a,b)
{
	var c;
	c=bzd(Ct(),NSn,'') + '/icalendar'; //maybe https://schoolity.com/icalendar so we do not need to trace bzd() however we need to trace who uses this funtion and what b is passed
	c += '?'; //add url query separator using addition assignment so it is now https://schoolity.com/icalendar? 
	return c += a + '=' + b //returns https://schoolity.com/icalendar.com/icalendar?id=[+b]
}
