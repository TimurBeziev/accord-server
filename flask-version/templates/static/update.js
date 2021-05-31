import {updateChats} from './index.js';

function infinite_update() {
    setInterval(function () {
        updateChats();
    }, 50);
}