import { deleteButton, addItem } from './api.js';

window.addEventListener('load', () => {
    
    console.log('Javascripte loaded'); 



    document.querySelector('.top ul').
    addEventListener('click', async e => deleteButton(e));
    




    document.querySelector('.bott button').
    addEventListener('click', async () => addItem());

    document.querySelector('.bott input').
    addEventListener('keypress', async e => {
        if (e.key === 'Enter') addItem(); 
    })



});