function addToCart(product_id) {
	$.ajax({
		// Link to the add-to-cart ajax view passing the user token and the product id
		url:  '/add-to-cart/'+product_id+'/',
		success: function  (data) {
			// Select span with id="cart-text" and update value using ajax response data
			$('#cart-text').html(data.cart_text);
		},
		error: function (data) {
			alert("Failure!");
		}
	});
}


// TODO: transform into AJAX function that actually updates database
// TODO: Update cart total
function updateTotal(quantity, item_price, item_id) {
	// Calculate new price with two decimal places
	var new_price = Number(item_price * quantity).toFixed(2);
	// Select tag with class price-<item_id> generated in the template
	$('.price-'+item_id).text(new_price);
}

$(document).ready(function () {
	// Selector for quantity number input
	$('.cart-item-quantity').change(function (data) {
		// The quantity will be exactly the current input value
		var quantity = data.target.valueAsNumber;
		/*
		* The item price is passed through the 'data-initial-value' attribute on the template
		* to make it easier for us to calculate the new total price
		*/
		var item_price = $(this).attr('data-initial-value');
		/*
		* The item id is passed through the 'data-index' attribute on the template
		* to make it easier for us to select the corresponding item's total price div
		*/
		var item_id = $(this).attr('data-index');
		var price_tag = $(this).parent().next().children('.price-wrap');
		updateTotal(quantity, item_price, item_id)
	});
})