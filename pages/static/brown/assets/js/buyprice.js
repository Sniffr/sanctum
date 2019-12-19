var coin = $("#coin-amount");
var price = $("#price-to-pay");
var updated_price;
var updated_coins;
try {
    var btc_price = JSON.parse($("#buy-price").text());
} catch (e) {
    console.log(e);
}
updated_price = btc_price * 1.10;


price.on("change paste keyup", function () {
    updated_coins = price.val() / updated_price;
    coin.val(parseFloat(updated_coins.toFixed(8)));
});

coin.on("change paste keyup", function () {
    price.val(Math.round(coin.val() * updated_price));
});

var coin_sell = $("#coin-amount-buy");
var price_sell = $("#price-to-sell");
var updated_price_sell;
var updated_coins;


updated_price_sell = btc_price * 0.9;


price_sell.on("change paste keyup", function () {
    updated_coins = price_sell.val() / updated_price_sell;
    coin_sell.val(parseFloat(updated_coins.toFixed(8)));
});

coin_sell.on("change paste keyup", function () {
    price_sell.val(Math.round(coin_sell.val() * updated_price_sell));
});


var started_button = $("#get-started-btn");
var started_input = $("#get-started-email");
var email

started_button.on("click", function () {
    email = started_input.val();
    window.localStorage.setItem('mail', email);
});

var buy_button = $("#buy-button");
var sell_button = $("#sell-button");

buy_button.on("click", function () {
    var coin_amount = coin.val();
    window.localStorage.setItem('prefill_buy', coin_amount);
});

sell_button.on("click", function () {
    var coin_amount = coin_sell.val();
    window.localStorage.setItem('prefill_sell', coin_amount);
});

$(document).ready(function () {
    var coins;

    if (window.localStorage.getItem("prefill_buy")) {
        coins = window.localStorage.getItem("prefill_buy");
        coins = parseFloat(coins);
        coin.val(parseFloat(coins.toFixed(8)));
        price.val(Math.round(coin.val() * updated_price));
        window.localStorage.removeItem("prefill_buy");


    } else if (window.localStorage.getItem("prefill_sell")) {
        coins = window.localStorage.getItem("prefill_sell");
        coins = parseFloat(coins);
        coin_sell.val(parseFloat(coins.toFixed(8)));
        price_sell.val(Math.round(coin_sell.val() * updated_price_sell));
        window.localStorage.removeItem("prefill_sell");

    }
});



