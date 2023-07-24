


if(localStorage.getItem('cart') == null){
  var cart = {}
  console.log('cart is created')
}

else{

    cart = JSON.parse(localStorage.getItem('cart'))
    console.log("exists")

document.getElementById('desktop-cart').innerHTML = Object.keys(cart).length;
document.getElementById('mobile-cart').innerHTML = Object.keys(cart).length;


}

// small add to cart button 
$('.small-cart-btn').click(function(){

  var product_id = this.id.toString()
  console.log(product_id)
  

  if(cart[product_id] != undefined){
      console.log("product already exists")
  }
  else{
      cart[product_id] = 1;
      document.getElementById('desktop-cart').innerHTML = Object.keys(cart).length;
      document.getElementById('mobile-cart').innerHTML = Object.keys(cart).length;
     
      UpdateCart(cart)
              
  }
  localStorage.setItem('cart', JSON.stringify(cart))
  console.log(cart)
})
// large add to cart button 
$('.add-cart-btn').click(function(){

    var product_id = this.id.toString()
    console.log(product_id)
    

    if(cart[product_id] != undefined){
      alert('product allready exists in the cart')
        console.log("product already exists")
    }
    else{
        cart[product_id] = 1;
        document.getElementById('desktop-cart').innerHTML = Object.keys(cart).length;
        document.getElementById('mobile-cart').innerHTML = Object.keys(cart).length;
       
        UpdateCart(cart)
                
    }
    localStorage.setItem('cart', JSON.stringify(cart))
    console.log(cart)
})



  // Close the dropdown menu if the user clicks outside of it


  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }




// setting items name to cart 

function UpdateCart(cart){

  document.getElementById('mobile-dropdown-list').innerHTML =``
  document.getElementById('desktop-dropdown-list').innerHTML =``

 
  var cart_list = ""
  var slug = ""
  var count = 1
  for(var item in cart){

var btn = document.getElementById(item)
btn.classList.add('bg-color-update')
btn.innerHTML = 'Already In Cart'
console.log(btn.classList)
  // console.log('pr'+item)
  cart_list =  document.getElementById('name' + item).innerHTML
  slug =  document.getElementById('slug' + item)

  document.getElementById('desktop-dropdown-list').innerHTML += `<li style="margin-left:10px" class="dropdown-item cart-list-itmes">
  <a href="${slug}"> <span>${count}) ${cart_list}</a>   `

document.getElementById('mobile-dropdown-list').innerHTML += `<li style="margin-left:10px; font-size:13px" class="dropdown-item cart-list-itmes">
  <a href="${slug}" style="width:auto"'> <span>${count}) ${cart_list}</a>   </span></li> `

    count +=1;
  }
  document.getElementById('mobile-dropdown-list').innerHTML += `<hr style="color:silver"><button class="cart-item-remove-btn remove" style="margin-left:70px; margin-top:2px;">
  <ion-icon name="trash"></ion-icon>
</button>`

document.getElementById('desktop-dropdown-list').innerHTML += `<hr style="color:silver"><button class="cart-item-remove-btn remove" style="margin-left:120px; margin-top:5px" ><ion-icon name="trash"></ion-icon>
</button></span></li> `


}


UpdateCart(cart)


$('.remove').click(function(){
  console.log("helllooooo")

  localStorage.removeItem('cart', JSON.stringify(cart))
  document.getElementById('desktop-cart').innerHTML = `0`
document.getElementById('mobile-cart').innerHTML = `0`
document.getElementById('desktop-dropdown-list').innerHTML =``
document.getElementById('mobile-dropdown-list').innerHTML =``

  
  console.log(cart)
})
     

// showing products name on the cart list 




