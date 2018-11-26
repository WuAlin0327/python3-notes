//提交事件
function present(){
    var title = document.getElementById('title');
    if (title.value == ''){
        alert('请输入内容')
    }else{
        var todo = loadData();
        list = {'title':title.value,'status':false};
        todo.push(list);
        addtodo(title.value);
        localStorage.setItem('todo',JSON.stringify(todo));
        title.value = '';
    }
}
function loadData() {
    var localdata = localStorage.getItem('todo');
    if (localdata != null){
        return JSON.parse(localdata)
    }else{
        return []
    }

}
function load() {

}
function addtodo(title){
    var Li = document.createElement('li');
    var Bnt = document.createElement('button');
    var Span = document.createElement('span');
    var Delete_A = document.createElement('a');
    var todoUl = document.getElementById('todo');

    Li.appendChild(Bnt);
    Li.appendChild(Span);
    Li.appendChild(Delete_A);
    Li.className = 'proceed';
    Bnt.id = "btn1";
    Delete_A.innerHTML = '-';
    Span.innerHTML = title;
    todoUl.appendChild(Li);

}
window.onload = function () {
    var date = JSON.parse(localStorage.getItem('todo'));
    for (var i in date){
        addtodo(date[i].title)
    }
};