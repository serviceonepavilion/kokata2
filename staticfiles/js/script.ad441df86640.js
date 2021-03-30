if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'))
    totalCartUpdate()
}

if (localStorage.getItem('totalprice') == null) {
    var totalprice = localStorage.getItem('totalprice');
} else {
    totalprice = parseInt(localStorage.getItem('totalprice'));
    totalCartUpdate()
}


function totalCartUpdate() {
    // Cart Item Update
    if (localStorage.getItem('cart')) {
        document.querySelectorAll('#totalcart').forEach(cartitem => {
            cartitem.innerHTML = Object.keys(JSON.parse(localStorage.getItem('cart'))).length;
        });
    }
    // 
    // If Cart Is Empty
    if (localStorage.getItem('cart') == null || localStorage.getItem('cart') == '{}' && document.querySelector('.cartitems')) {
        document.querySelector('.cartitems').innerHTML = "<div class='empty'>Cart is Empty</div>";
    }
    // 
    if (document.querySelector('.totalprice')) {
        if (document.querySelector('.item')) {
            var totalprice = 0;
        } else {
            var totalprice = parseInt(localStorage.getItem('totalprice'));
        }
        for (var carttiems in cart) {
            if (document.querySelector(`.item${carttiems}`)) {
                document.querySelector(`.item${carttiems}`).style.height = "auto";
                document.querySelector(`.item${carttiems}`).style.padding = "10px 0px";
                totalprice += (parseInt(String(document.querySelector(`.item${carttiems} .menu-price .price`).innerHTML)) * cart[carttiems])
            }
            localStorage.setItem('totalprice', totalprice)
        }
        document.querySelectorAll('.totalprice').forEach(totalprice => {
            totalprice.innerHTML = `₹${localStorage.getItem('totalprice')}`;
        })
    }
}

function updateAddCartButton() {
    const addcarts = document.querySelectorAll('.addcart');
    addcarts.forEach(addcart => {
        if (cart[addcart.id]) {
            addcart.querySelector('#cartcount').innerHTML = cart[addcart.id];
            addcart.querySelector('.ctrlcart').style.display = "block";
            addcart.querySelector('.add').style.display = "none";
        }
        addcart.querySelector('.add').addEventListener('click', () => {
            if (cart[addcart.id] != undefined) {
                cart[addcart.id] = cart[addcart.id] + 1;
            } else {
                cart[addcart.id] = 1
            }
            localStorage.setItem('cart', JSON.stringify(cart))
            addcart.querySelector('#cartcount').innerHTML = cart[addcart.id];
            addcart.querySelector('.ctrlcart').style.display = "block";
            addcart.querySelector('.add').style.display = "none";
            totalCartUpdate();
        });
        addcart.querySelector('#minus').addEventListener('click', () => {
            if (cart[addcart.id] == "1") {
                console.log(cart[addcart.id])
                addcart.querySelector('.ctrlcart').style.display = "none";
                addcart.querySelector('.add').style.display = "block";
                delete cart[addcart.id];
            } else {
                cart[addcart.id] = cart[addcart.id] - 1;
            }
            localStorage.setItem('cart', JSON.stringify(cart))
            addcart.querySelector('#cartcount').innerHTML = cart[addcart.id];
            totalCartUpdate();
        });
        addcart.querySelector('#plus').addEventListener('click', () => {
            if (cart[addcart.id] != undefined) {
                cart[addcart.id] = cart[addcart.id] + 1;
            } else {
                cart[addcart.id] = 1
            }
            localStorage.setItem('cart', JSON.stringify(cart))
            addcart.querySelector('#cartcount').innerHTML = cart[addcart.id];
            addcart.querySelector('.ctrlcart').style.display = "block";
            addcart.querySelector('.add').style.display = "none";
            totalCartUpdate()
        });
    });
}