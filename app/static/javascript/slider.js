$(function(){
var number = 2;
var id_2_2 = 'slider-out-2';
var slider = document.getElementsByName('slider_style');
var output = document.getElementsByName('slider_out');

var input = document.getElementsByName('slider_button');
var root = document.documentElement;
var dragging = new Array(number);
var value = new Array(number);
var width = new Array(number);
for(var i = 0; i<number ;i++){
	dragging[i]=false;
	value[i] = output[i].value;
	width[i] = input[i].clientWidth/2;
}

var i= 0;
var set_value = function(){
	input[i].style.left = (value[i] -input[i].clientWidth/2) + 'px';
	//console.log(value[i]);
	output[i].value = value[i];
};
set_value();

for(var j=0;j<number;j++){
slider[j].onclick = function(evt){
	document.onmousemove(evt);
	document.onmouseup();
};
}
for(var j=0;j<number;j++){
input[j].onmousedown = function(evt){
	dragging[j] = true;
	i=j;
	//console.log("88");
	return false;
};
}

document.onmouseup = function(evt){
	dragging[i] = false;
	output[i].value = value[i];
};

document.onmousemove = function(evt){
	if(dragging[i]){
		if(!evt){
			evt = window.event;
		}
		var left = evt.clientX;
		//console.log(slider[i].getBoundingClientRect());
		var rect = slider[i].getBoundingClientRect();
		value[i] = Math.round(left - rect.left - width[i]);
 		if (value[i] < 0){
			value[i] = 0;
		}else if (value[i] > slider[i].clientWidth){
			value[i] = slider[i].clientWidth;
		}
		set_value();
		return false;
	}
};
});
