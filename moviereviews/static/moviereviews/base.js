document.addEventListener('DOMContentLoaded', function () {


  let div = document.createElement('div')
  div.innerHTML = "well shit it's a new div"
  document.body.append(div)

  document.querySelectorAll('a').forEach(a => {
    if (this.dataset.index) {
      div.innerHTML = "this guy has an index"
      this.parent.append(div)
      a.onclick = function () {
        alert(this.dataset.index)
      }
    }
  })



})