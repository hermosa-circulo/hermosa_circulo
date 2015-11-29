
jQuery( function(){
	jQuery( '#jquery-ui-slider-1').slider({
		range: 'min',
		value: 45,
		min: 0,
		max: 100,
		step: 1,
		slide: function(event,ui){
			jQuery('#jquery-ui-slider-value-1').val(ui.value);
		}
	});
	jQuery('#jquery-ui-slider-value-1').val(jQuery('#jquery-ui-slider-1').slider('value'));
});

jQuery( function(){
	jQuery( '#jquery-ui-slider-2').slider({
		range: 'min',
		value: 10,
		min: 0,
		max: 100,
		step: 1,
		slide: function(event,ui){
			jQuery('#jquery-ui-slider-value-2').val(ui.value);
		}
	});
	jQuery('#jquery-ui-slider-value-2').val(jQuery('#jquery-ui-slider-2').slider('value'));
});

jQuery( function(){
	jQuery( '#jquery-ui-slider-3').slider({
		range: 'min',
		value: 60,
		min: 0,
		max: 100,
		step: 1,
		slide: function(event,ui){
			jQuery('#jquery-ui-slider-value-3').val(ui.value);
		}
	});
	jQuery('#jquery-ui-slider-value-3').val(jQuery('#jquery-ui-slider-3').slider('value'));
});

jQuery( function(){
	jQuery( '#jquery-ui-slider-4').slider({
		range: 'min',
		value: 30,
		min: 20,
		max: 60,
		step: 1,
		slide: function(event,ui){
			jQuery('#jquery-ui-slider-value-4').val(ui.value);
		}
	});
	jQuery('#jquery-ui-slider-value-4').val(jQuery('#jquery-ui-slider-4').slider('value'));
});

jQuery( function(){
	jQuery( '#jquery-ui-slider-5').slider({
		range: 'min',
		value: 0.5,
		min: 0,
		max: 1,
		step: 0.01,
		slide: function(event,ui){
			jQuery('#jquery-ui-slider-value-5').val(ui.value);
		}
	});
	jQuery('#jquery-ui-slider-value-5').val(jQuery('#jquery-ui-slider-5').slider('value'));
});

