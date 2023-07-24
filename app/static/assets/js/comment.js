const comment_form = document.getElementById('comment-form')
const spinner_box = document.getElementById('spinner-box')

comment_form.addEventListener('submit', e=>{
    e.preventDefault()
    addJobAdvertisment()
})
const addJobAdvertisment = () => {

    const name = document.getElementById('name')
    const email = document.getElementById('email')
    const comment = document.getElementById('comment')
    const blog_id = document.getElementById('blog-id')

    const csrf = document.getElementsByName('csrfmiddlewaretoken')


    const commentForm = new FormData()
    commentForm.append('csrfmiddlewaretoken', csrf[0].value)
    commentForm.append('name', name.value)
    commentForm.append('email', email.value)
    commentForm.append('comment', comment.value)
    commentForm.append('blog_id', blog_id.value)

  

    $.ajax({

        type: 'POST',
        url: '/comment/comment-post',
        data: commentForm,
        beforeSend: function(){
            spinner_box.classList.remove('not-visible')
        },
      complete: function(){
        spinner_box.classList.add('not-visible')
        alert('your comment is recived... after approvel you will see your comment under this post... thanks!..')
        document.getElementById('name').value = ''
        document.getElementById('email').value = ''
        document.getElementById('comment').value = ''
      },
        success: function(response) {
           console.log(response)
        },
        error: function(error) {
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })

}
