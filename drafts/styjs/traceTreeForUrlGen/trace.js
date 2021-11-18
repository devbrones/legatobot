
JTc(2414,11,I4m,aUk);_.Vk=function cUk(a){_Tk(this,JN(a,152))};_.Uk=function bUk(a){y5k();Vve(a)};var Myc=Uwd(FSn,'Methods/38',2414);

function dUk(a,b){var c;c=QPk('id',b);a.a.Vk(c)}

JTc(2372,11,I4m,gUk);_.Vk=function iUk(a){var b;(b=this,$N(a),b).a.qj((Uvd(),true))};_.Uk=function hUk(a){this.a.qj((Uvd(),false))};var bzc=Uwd(FSn,'Methods/4',2372);



function QPk(a,b)
{
	var c;
	c=bzd(Ct(),NSn,'') + '/icalendar'; //maybe https://schoolity.com/icalendar so we do not need to trace bzd() however we need to trace who uses this funtion and what b is passed
	c += '?'; //add url query separator using addition assignment so it is now https://schoolity.com/icalendar? 
	return c += a + '=' + b //returns https://schoolity.com/icalendar.com/icalendar?id=[+b]
}



function dUk(a,b)
{
	var c;
	c=QPk('id',b);
	a.a.Vk(c) // i assume this creates the window box popup
}

function jUk(a,b)
{
	var c;
	c=QPk('e',b);
	a.a.Vk(c) // probably also creates a box popup
}

JTc(2415,25,I4m,eUk);

_.Vk = function fUk(a)
{
	dUk(this,ON(a))
};


function ON(a)
{
	kVd(a==null||WN(a)); // this cunt in parentheses is a logical OR, so this returns null | true or null | false, now we need to now what kVd does with this value
	return a //if a is a string then return a or throw an exception
}

function WN(a)
{
	return typeof a===rRm // rRm is 'string' , so it returns either true or false depending on whether a is a string
}


function kVd(a) //exception thrower
{
	if(!a) //if a is not a string (see ON()) then
	{
		throw cTc(new ixd) //throws an exception so we dont need to investigate
	}
}










var Nyc = Uwd(FSn,'Methods/39',2415);

