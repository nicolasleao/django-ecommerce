function add_to_cart(el) {
	$.ajax({
		url:  '/store/list-cart-items',
		type:  'get',
		dataType:  'json',
		success: function  (data) {
			data.items.forEach(item => {
				console.log('item'+item.name+'added to shopping cart');
			});
		}
	});
}