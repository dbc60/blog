'use strict';

const btn = document.getElementById('toggle-grid');

function toggleGrid() {
  document.body.classList.toggle('grid');
}

btn.addEventListener('click', toggleGrid);
