function addToCart(product_id) {
	$.ajax({
		// Link to the add-to-cart ajax view passing the user token and the product id
		url:  '/add-to-cart/'+product_id+'/',
		success: function  (data) {
			// Select span with id="cart-text" and update value using ajax response data
			$('#cart-text').html(data.cart_text);
		},
		error: function (data) {
			console.log('Failed to add product to cart');
		}
	});
}

function updateItemQuantity(product_id, product_price, quantity) {
	$.ajax({
		// Link to the add-to-cart ajax view passing the user token and the product id
		url:  '/update-item-quantity/'+product_id+'/'+quantity+'/',
		success: function  (data) {
			// Calculate new total price for current item
			let new_price = (quantity * product_price).toFixed(2);
			// Update current item's total value
			$('.price-'+product_id).html(new_price)
			// Calculate new cart's total value
			let cart_total = data.cart_total.toFixed(2);
			// Update cart's total value with the value returned from ajax view
			$('#cart-total').html(cart_total);
		},
		error: function (data) {
			console.log('Failed to add product to cart');
		}
	});
}

$(document).ready(function () {
	// Selector for quantity number input
	$('.cart-item-quantity').change(function (data) {
		// The quantity will be exactly the current input value
		let quantity = data.target.valueAsNumber;
		// Limit quantity to a realistic value between 1 and 1000
		if(quantity < 1) {
			quantity = 1;
			data.target.valueAsNumber = 1;
		}
		else if(quantity > 1000) {
			quantity = 1000;
			data.target.valueAsNumber = 1000;
		}
		let product_id = $(this).attr('data-index');
		let product_price = $(this).attr('data-initial-value');
		// Update item quantity and refresh page
		updateItemQuantity(product_id, product_price, quantity);
	});
})