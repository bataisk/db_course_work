postersButton = document.getElementById('selectPosters');
backdropsButton = document.getElementById('selectBackdrops');

viewAllPosters = document.getElementById('view-all-posters');
viewAllBackdrops = document.getElementById('view-all-backdrops');

posters = document.getElementById('posters');
backdrops = document.getElementById('backdrops');


postersButton.onclick = function () {
    backdropsButton.classList.remove('selected');
    postersButton.classList.add('selected');

    viewAllBackdrops.classList.add('hide');
    viewAllPosters.classList.remove('hide');

    backdrops.classList.add('hide');
    posters.classList.remove('hide');

    return false;
};


backdropsButton.onclick = function () {
    backdropsButton.classList.add('selected');
    postersButton.classList.remove('selected');

    viewAllBackdrops.classList.remove('hide');
    viewAllPosters.classList.add('hide');

    backdrops.classList.remove('hide');
    posters.classList.add('hide');

    return false;
};