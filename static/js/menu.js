function toggle_menu() {

    const list_id = document.getElementById('list');
    console.log(list_id.style)
    if (list_id.style.display === 'none') {
        list_id.className.add('clicked');
        console.log('in')

    }
}