function toggle_menu() {
    console.log('in')

    const list_id = document.getElementById('list');
    console.log(list_id)
    console.log('in')

    if (list_id.style.display === 'none') {
        list_id.className.add('clicked');
        console.log('in')

    }
}