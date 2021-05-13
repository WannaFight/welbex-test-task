const icons = {
    minus: 'fa-minus',
    asc: 'fa-caret-up',
    desc: 'fa-caret-down'
}

const columns = document.querySelectorAll('.icon-text');

for (let column of columns) {
    column.addEventListener('click', function (e) {
        // console.log(Array.from(columns).indexOf(this))
        let other_columns = document.querySelectorAll(`.icon-text:not(#${this.id})`);

        //setting minus icon for other columns
        for (let other_column of other_columns) {
            let iTagOther = other_column.querySelector('i')
            iTagOther.classList.toggle(icons.asc, false);
            iTagOther.classList.toggle(icons.desc, false);
            iTagOther.classList.toggle(icons.minus, true);
            // other_column.querySelector('i').classList = `fas ${icons.minus}`;
        }

        let i_tag = this.querySelector('i');

        if (i_tag.classList.contains(icons.asc)) {
            i_tag.classList.toggle(icons.asc);
            i_tag.classList.toggle(icons.desc);
        } else if (i_tag.classList.contains(icons.desc)) {
            i_tag.classList.toggle(icons.desc);
            i_tag.classList.toggle(icons.asc);
        } else {
            i_tag.classList.toggle(icons.minus, false);
            i_tag.classList.toggle(icons.asc)
        }
    });
}