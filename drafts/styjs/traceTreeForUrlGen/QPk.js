
// this part alledgedly generates the url


function QPk(a,b)
{
	var c;
	c=bzd(Ct(),NSn,'') + '/icalendar'; //maybe https://schoolity.com/icalendar 
	c+='?'; //add url query separator
	return c+=a+'='+b //returns https://schoolity.com/icalendar.com/icalendar?id=[+b]
}
