document.addEventListener("click", function(e){
    if (e.target.matches(".likes")) {
        let el = e.target;
        let nextEl = el.nextElementSibling;
        let pk = el.parentNode.dataset.id
        getLikes(pk);
        if (nextEl.classList.contains("selected")){
            nextEl.classList.remove("selected");
            nextEl.innerText = +nextEl.textContent - 1
        }
        el.classList.toggle("selected");
        if (el.classList.contains("selected")) {
            el.innerText = +e.target.textContent + 1
        } else {
            el.innerText = +e.target.textContent - 1
        }
    };
    if (e.target.matches(".dislikes")) {
        let el = e.target;
        let prevEl = el.previousElementSibling;
        let pk = el.parentNode.dataset.id
        getDislikes(pk);
        if (prevEl.classList.contains("selected")){
            prevEl.classList.remove("selected");
            prevEl.innerText = +prevEl.textContent - 1
        }
        el.classList.toggle("selected");
        if (el.classList.contains("selected")) {
            el.innerText = +e.target.textContent + 1
        } else {
            el.innerText = +e.target.textContent - 1
        }
    }
})

const baseUri = window.location.origin;


async function getLikes(pk) {
    response = await fetch(`${baseUri}/add_like/${pk}`, {
        method: "POST",
        headers: {
            'X-CSRFToken': getCookie("csrftoken"),
        }
    });

    if (!response.ok){
        alert("Неа, нельзя! Зарегистрируйтесь или войдите");
    }
}

async function getDislikes(pk) {

    response = await fetch(`${baseUri}/add_dislike/${pk}`, {
        method: "POST",
        headers: {
            'X-CSRFToken': getCookie("csrftoken"),
        }
    });

    if (!response.ok){
        alert("Неа, нельзя! Зарегистрируйтесь или войдите");
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// edit comment

let toggleEdit = true;
function editComment(elemForEdit, pk) {
    let btns = document.querySelectorAll(".comment-edit");
    let btn;
    btns.forEach(brn => {
        if (brn.previousElementSibling.dataset.id == pk) {
            btn = brn;
        }
    })
    if (toggleEdit){
        elemForEdit.setAttribute('contentEditable', true);
        const range = document.createRange();
        range.selectNodeContents(elemForEdit);
        range.collapse(false);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        btn.innerText = "Сохранить";
    } else {
        elemForEdit.removeAttribute('contentEditable', false);
        // console.log(elemForEdit.innerText.trim());
        btn.innerText = "Редактировать";
        fetch(`${baseUri}/comment_edit/${pk}`, {
            method: "POST",
            headers: {
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body: JSON.stringify({
                "body": elemForEdit.innerText,
            }),
        })
    }
    toggleEdit = !toggleEdit;
}

document.addEventListener("click", function(e) {
    if (e.target.matches(".comment-edit")) {
        el = e.target.parentNode.previousElementSibling;
        pk = e.target.previousElementSibling.dataset.id;
        editComment(el, pk);
    }
})


// delete comment

document.addEventListener("click", function(e) {
    if (e.target.matches(".comment-delete")) {
        let pk = e.target.parentNode.firstElementChild.dataset.id;
        deleteComment(pk);
    }
})


async function deleteComment(pk) {
    let item = confirm("Вы уверены?");

    if (item) {
        const response = await fetch(`${baseUri}/comment_delete/${pk}`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            }
        })
        if (response.ok) {
            location.reload();
        }
    }
}
