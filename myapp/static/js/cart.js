var updateBtn = document.getElementsByClassName('update-cart')

// add to cart logic
for (i = 0; i < updateBtn.length; i++){
	updateBtn[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
        console.log('USER:', user)

        if(user == 'NotLoggedIn'){
            console.log('User not logged in')
        }else{
            updateUserOrder(productId, action)
        }
	})
}

function updateUserOrder(productId, action){
		var url = '/update_item/'
        console.log('URL: ', url)
		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
            location.reload()
		});
}