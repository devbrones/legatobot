
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

_.Vk = function fUk(a) // i cant for the love of god find out how vk is a fucking function and a variable at the same time
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







JTc(2415,25,I4m,eUk);


function JTc(a, b, c) { 					// lets crack this one out shall we?
  var d = HTc, i;						// sets d to be HTc and i . HOW
  var e = d[a];							// sets e to be the a:th entry of d
  var g = e instanceof Array ? e[0] : null;			// sets g to be a boolean returned after testing e against the value returned by the turnary operation that checks if array is true and if it is true it uses e[0] and else it sets the value to be null
  if (e && !g) {						// 
    _ = e							// 
  } else {							// 
    _ = (i = b && b.prototype, !i && (i = HTc[b]), MTc(i));	// 
    _.Xp = c;							// 
    !b && (_.Yp = OTc);						// 
    d[a] = _							// 
  }					
  for (var h = 3; h < arguments.length; ++h) {			// 	
    arguments[h].prototype = _					// 
  } 
  g && (_.Wp = g)						// 
}



//next is code from chrome that is the XMLGET handler
//

function v3c(b, c) {
    console.log("v3c_b: ", b);
    console.log("v3c_c: ", c);
    var d, e, g, h, i;
    h = null;
    d = null;
    try {
        g = c.a.responseText;
        i = c.a.status;
        !!$stats && j4c(i4c(b.d, b.b, g.length, 'responseReceived'));
        i != 200 ? (d = new j$c(i, c.a.statusText, g)) : g == null ? (d = new IZc('No response payload from ' + b.b)) : Wyd(g.substr(0, 4), '//OK') ? (h = b.c.Dh(Ti(b.e, g))) : Wyd(g.substr(0, 4), '//EX') ? (d = HN(R2c(Ti(b.e, g)), 136)) : (d = new IZc(g + A1m + b.b));
	consol
    } catch (a) {
        a = eTc(a);
        if (PN(a, 42)) {
            e = a;
            d = new EZc(e)
        } else if (PN(a, 136)) {
            e = a;
            d = e
        } else throw fTc(a)
    } finally {
        !!$stats && j4c(k4c(b.d, b.b, 'responseDeserialized'))
    }
    try {
        !d ? b.a.Le(h) : b.a.Ke(d)
    } finally {
        !!$stats && j4c(k4c(b.d, b.b, 'end'))
    }
}



var o = new XMLHttpRequest;
o.onreadystatechange = function()
{
	o.readyState===4&&a.Sp(o.response)
};
o.open('POST',c);o.send(i)}








function R5k(a, b, c, d) {
    N5k();
    var e, g, h, i, j, k;
    i = HN(pDd(F5k, a.i), 106);
    if (d.a.status != 200) {
        FJm();
        !BJm && (BJm = new GJm);
        ++AJm;
        if (!i) {
            sDd(F5k, a.i, Uxd(1));
            a6k(a, b)
        } else if (i.a < 2) {
            i = Uxd(i.a + 1);
            sDd(F5k, a.i, i);
            j = new A6k(a,b);
            Ei(j, i.a * i.a * i.a)
        } else {
            k = a.i.lastIndexOf('RPC');
            h = _yd(a.i, '|', k) + 1;
            g = _yd(a.i, '|', h);
            e = lzd(a.i, h, g);
            M5k ? ki(HTn + CBm(M5k) + ' after ' + A5k + ITn + G5k + JTn + d.a.status + KTn + e) : ki('RPC Invocation failed for unknown user after ' + A5k + ITn + G5k + JTn + d.a.status + KTn + e);
            if (d.a.status == 0) {
                !BJm && (BJm = new GJm);
                fRm((Zq(),
                !$Qm && ($Qm = new hRm),
                Zq(),
                $Qm), (lRm(),
                new qRm(LTn,(ddl(),
                MTn),(ddl(),
                NTn),false,false,false)), 30);
                uDd(F5k, a.i);
                v3c(b, d)
            } else {
                v3c(b, d)
            }
        }
    } else {
        !!i && uDd(F5k, a.i);
        FJm();
        !BJm && (BJm = new GJm);
        ++EJm;
        dRm((Zq(),
        !$Qm && ($Qm = new hRm),
        Zq(),
        $Qm), (lRm(),
        new qRm(LTn,(ddl(),
        MTn),(ddl(),
        NTn),false,false,false)));
        v3c(b, d)
    }
}















//OK[0,0,13,29,7,0,2,0,2021,10,28,0,27,"XsI4XsA",23,2,26,0,-16,-16,1,25,0,25,2,0,0,17,0,2024,1,0,2,2,2,2,2,2,2,2,2,2,2,24,"XsLO5dO",23,22,0,0,2,21,20,0,0,0,0,14,19,15,18,15,2,17,0,17,2,0,0,0,1,0,0,14,7,15,16,15,1,14,2,0,13,1,0,0,0,0,12,2,1,0.0,0.0,11,0,10,9,2147483644,8,0,0,0,7,0,0,2,6,5,0,0,0,4,0,3,2,1,["schoolutil.client.StudentData/2466792438","","schoolutil.shared.objects.XUserInfo/3016209171","SIMRISHAMNSVÄGEN 13 LGH 0901","+46732630271","JOHANNESHOV","s0f7BuY","Jonas","8DEAED6C-D143-41E6-827D-8A30714D036A","https://www.schoolity.com/app/cloudstorage/MediaGymnasiet/t129/D46CCED8-22A5-4CA8-B56B-9DB7A91D6F47","Cronholm Gudmundsson","Stockholm","java.util.HashSet/3273092938","java.util.HashMap/1797211028","java.lang.String/2004016611","MediaGymnasiet","java.util.ArrayList/4159755760","ahNlfnNjaG9vbGl0eS1saXZlLWV1cjMLEglYVXNlckluZm8iJEUwRDk5Q0M5LUE1NjgtNEJENC05RTVCLUQ5NTMxNzQ0NDY4NQyiARZNZWRpYUd5bW5hc2lldF9jb25jZXJu","ahNlfnNjaG9vbGl0eS1saXZlLWV1cjMLEglYVXNlckluZm8iJEJERTg2RkU4LTNEMjgtNDk0OC1BRTJGLTE5NTFFOUZEQjlDOQyiARZNZWRpYUd5bW5hc2lldF9jb25jZXJu","200505051177","21jogudm@mediagymnasiet.se","121 53","java.util.Date/3385151746","dF0491BCF-FF5E-4F7F-B8D6-CD50D1A60BB1","java.lang.Boolean/476441737","o6","5Y1j2s","java.lang.Integer/3438268394","Jonas Cronholm Gudmundsson"],0,7]    this is a response that the server gives 
