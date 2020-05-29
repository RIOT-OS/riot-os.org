

jQuery(window).load(function() {

jQuery('#main-menu').visualNav({
	bottomMargin:100
});
 
 jQuery('a.tool_tip').tipsy({fade: true});
 
 jQuery('#slider').nivoSlider({
	effect:'fade' // Specify sets like: 'fold,fade,sliceDown'
 });
 jQuery('#list li a img').animate({'opacity' : 1}).hover(function() {
	jQuery(this).animate({'opacity' : .2});
 }, function() {
	jQuery(this).animate({'opacity' : 1});
 });
 
 jQuery('.thumbnail li a img').animate({'opacity' : 1}).hover(function() {
	jQuery(this).animate({'opacity' : .2});
 }, function() {
	jQuery(this).animate({'opacity' : 1});
 });
 
 jQuery('.fig_highlight img').animate({'opacity' : 1}).hover(function() {
	jQuery(this).animate({'opacity' : .2});
 }, function() {
	jQuery(this).animate({'opacity' : 1});
 });
 
 
 
 //$("#list:first a[rel^='prettyPhoto']").prettyPhoto({animationSpeed:'slow',theme:'light_square',slideshow:2000, autoplay_slideshow: false});
 /*fanybox*/
	if(jQuery.fancybox){
		   jQuery("a[rel=image_group]").fancybox({
				'transitionIn'		: 'elastic',
				'transitionOut'		: 'elastic',
				'titlePosition' 	: 'over',
				'titleFormat'		: function(title, currentArray, currentIndex, currentOpts) {
					return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
				}
			});
			
			jQuery("a[rel=featured_group]").fancybox({
				'transitionIn'		: 'elastic',
				'transitionOut'		: 'elastic',
				'titlePosition' 	: 'over',
				'titleFormat'		: function(title, currentArray, currentIndex, currentOpts) {
					return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
				}
			});
	}
	

	/*DropDown*/
	var drop = jQuery('#top');
	var logo = $('#logo');
	var boolean=false;
	
	drop.click(function(){
		
		if(boolean==false){
			jQuery(this).find('ul').css({
				display: 'block'
			});
			boolean=true;
		}else{
			jQuery(this).find('ul').css({
				display: 'none'
			});
			boolean=false;
		}
	})
	
	logo.click( function(){
		drop.find('.top-link').text('Home');
	})
	
	drop.find('ul li a').click( function() {
	var name = jQuery(this).text();
	drop.find('.top-link').text(name);
	jQuery('#top').find('ul').css({
		display: 'none'
	});
	boolean=false;	
	});
	
	
	
	
	
	
	
	
});


(function($) {
	
	$.fn.sorted = function(customOptions) {
		var options = {
			reversed: false,
			by: function(a) {
				return a.text();
			}
		};
		$.extend(options, customOptions);
	
		$data = $(this);
		arr = $data.get();
		arr.sort(function(a, b) {
			
		   	var valA = options.by($(a));
		   	var valB = options.by($(b));
			if (options.reversed) {
				return (valA < valB) ? 1 : (valA > valB) ? -1 : 0;				
			} else {		
				return (valA < valB) ? -1 : (valA > valB) ? 1 : 0;	
			}
		});
		return $(arr);
	};

})(jQuery);

$(function() {
  
  var read_button = function(class_names) {
    var r = {
      selected: false,
      type: 0
    };
    for (var i=0; i < class_names.length; i++) {
      if (class_names[i].indexOf('selected-') == 0) {
        r.selected = true;
      }
      if (class_names[i].indexOf('segment-') == 0) {
        r.segment = class_names[i].split('-')[1];
      }
    };
    return r;
  };
  
  var determine_sort = function($buttons) {
    var $selected = $buttons.parent().filter('[class*="selected-"]');
    return $selected.find('a').attr('data-value');
  };
  
  var determine_kind = function($buttons) {
    var $selected = $buttons.parent().filter('[class*="selected-"]');
    return $selected.find('a').attr('data-value');
  };
  
  var $preferences = {
    duration: 800,
    easing: 'easeInOutQuad',
    adjustHeight: false
  };
  
  var $list = $('#list');
  var $data = $list.clone();
  
  var $controls = $('ul.splitter ul');
  
  $controls.each(function(i) {
    
    var $control = $(this);
    var $buttons = $control.find('a');
    
    $buttons.bind('click', function(e) {
      
      var $button = $(this);
      var $button_container = $button.parent();
      var button_properties = read_button($button_container.attr('class').split(' '));      
      var selected = button_properties.selected;
      var button_segment = button_properties.segment;

      if (!selected) {

        $buttons.parent().removeClass('selected-0').removeClass('selected-1').removeClass('selected-2').removeClass('selected-3').removeClass('selected-4');
        $button_container.addClass('selected-' + button_segment);
        
        var sorting_type = determine_sort($controls.eq(1).find('a'));
        var sorting_kind = determine_kind($controls.eq(0).find('a'));
        
        if (sorting_kind == 'all') {
          var $filtered_data = $data.find('li');
        } else {
          var $filtered_data = $data.find('li.' + sorting_kind);
        }
        
        if (sorting_type == 'size') {
          var $sorted_data = $filtered_data.sorted({
            by: function(v) {
              return parseFloat($(v).find('span').text());
            }
          });
        } else {
          var $sorted_data = $filtered_data.sorted({
            by: function(v) {
              return $(v).find('strong').text().toLowerCase();
            }
          });
        }
        //// add function for lightbox and fade in and out for image.
        $list.quicksand($sorted_data, $preferences, 
		function(){
			//end callback
			imageHoverFade();
			setLightbox();
			
			}
			);
        
      }
      
      e.preventDefault();
    });
    
  }); 

  var high_performance = true;  
  var $performance_container = $('#performance-toggle');
  var $original_html = $performance_container.html();
  
  $performance_container.find('a').live('click', function(e) {
    if (high_performance) {
      $preferences.useScaling = false;
      $performance_container.html('CSS3 scaling turned off. Try the demo again. <a href="#toggle">Reverse</a>.');
      high_performance = false;
    } else {
      $preferences.useScaling = true;
      $performance_container.html($original_html);
      high_performance = true;
    }
    e.preventDefault();
  });
});


// set the prettyphoto lightbox.
function setLightbox(){
	 //$("#list:first a[rel^='prettyPhoto']").prettyPhoto({animationSpeed:'slow',theme:'light_square',slideshow:2000, autoplay_slideshow: false});
	 /*fanybox*/
	if(jQuery.fancybox){
		   jQuery("a[rel=image_group]").fancybox({
				'transitionIn'		: 'elastic',
				'transitionOut'		: 'elastic',
				'titlePosition' 	: 'over',
				'titleFormat'		: function(title, currentArray, currentIndex, currentOpts) {
					return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
				}
			});
	}
}

// set the the fade in and out of images
function imageHoverFade(){
	
	$('#list li a img').animate({'opacity' : 1}).hover(function() {
		$(this).animate({'opacity' : .2});
	}, function() {
		$(this).animate({'opacity' : 1});
	});
}
