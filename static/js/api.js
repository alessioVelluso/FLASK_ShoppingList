const deleteButton = async e => {
    
    if(e.target.tagName != 'BUTTON') return


    const button = e.target;
    const id = button.parentElement.parentElement.attributes['data-id'].value
    
    try {

        await fetch(`/api/items/${id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },

        }).then(async res => {

            if (!res.ok) throw new Error('errore');
            else {
                const deleteTarget = document.querySelector(`li[data-id="${id}"]`);
                deleteTarget.remove();
            }
        });

    } catch(err) {
        console.error(err);
        alert('Delete item failed');
    }
}




const addItem = async () => {
    
    const input = document.querySelector('.bott input');

    try {

        await fetch(`/api/items/`, {
            method: 'POST',
            body: JSON.stringify({ item: input.value }),
            headers: { 'Content-Type': 'application/json' },

        }).then(async res => {

            if (!res.ok) throw new Error(res.json().message);
            else {
                const responseContent = await res.json()

                const newLi = document.createElement('li');
                newLi.innerHTML = input.value + '<div><button>x</button></div>';
                newLi.setAttribute('data-id', responseContent.id);

                const list = document.querySelector('.top ul');
                list.appendChild(newLi);

                input.value = '';
            }
        });

    } catch(err) {
        console.error(err);
        alert('Failed to add item');
    }
}


export { deleteButton, addItem }