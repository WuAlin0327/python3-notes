//提交事件
function $(id) {  //使用id获取对象
    return document.getElementById(id);
}

function present(){
    var title = document.getElementById('title');
    if (title.value == ''){
        alert('请输入内容')
    }else{
        var todo = loadData();
        list = {'title':title.value,'status':false};
        todo.push(list);
        saveData(todo);
        title.value = '';
        clear();
        load();
        }


}
function saveData(data) {
     localStorage.setItem('todo',JSON.stringify(data));
}
function loadData() {
    var localdata = localStorage.getItem('todo');
    if (localdata != null){
        return JSON.parse(localdata)
    }else{
        return []
    }

}

//清除之前todo列表和done列表中的标签，便于重新加载HTML
function clear(){
    $('todo').innerHTML = '';
    $('done').innerHTML = '';
}

function load(){
        var donelist = $('done');
        var todolist = $('todo');
        var data = loadData();
        var donestr = '';
        var todostr = '';
        let todocount = 0;
        let donecount = 0;
        if (data != null){
            for (var i in data){
            if (data[i].status){
                var title = data[i].title;
                //true为已经完成，false为正在进行，通过判断status判断加载在哪个ul列表里面，这里字符串格式化使用的是ES6中的方法
                donestr += `<li class="donelist">
                                <input type="checkbox" onchange='update(${i},"status",false)'>
                                <span id="s-${i}" onclick="alter(${i})">${title}</span>
                                <a href="javascript:remove(${i})">-</a>
                            </li>`;
                donecount +=1;
            } else{
                var title = data[i].title;
                todostr += `<li class="proceed">
                                <input type="checkbox" onchange='update(${i},"status",true)'>
                                <span id="s-${i}" onclick="alter(${i})">${title}</span>
                                <a href="javascript:remove(${i})">-</a>
                            </li>`;
                todocount +=1;
                }
            }
            donelist.innerHTML = donestr;
            todolist.innerHTML = todostr;
            $('todocount').innerHTML = todocount;
            $('donecount').innerHTML = donecount;

        }

}
window.onload = function () {
            load();
};
function update(i,msg,value) {
    var data = loadData();
    var todo = data.splice(i,1)[0];
    console.log(todo);
    todo[msg] = value;
    data.splice(i,0,todo);
    saveData(data);
    load()
}
function remove(i) {
    var data = loadData();
    var todo = data.splice(i,1)[0];
    saveData(data);
    load();

}
function alter(i) {
    var span = $('s-'+i);
    title = span.innerHTML;
    span.innerHTML = "<input id='input-"+i+"' value='"+title+"'/>";
    var input = document.getElementById('input-'+i);
    input.style.width = '300px';//输入框宽度
    input.setSelectionRange(0,input.value.length);
    input.focus();//input输入框获得焦点

    input.onblur = function () {//input输入框失去焦点，失去焦点后更改title内容
        if (input.value.length == 0){
            span.innerHTML = title;
            alter('内容不能为空')
        }else{
            update(i,"title",input.value);
            console.log('更新了内容')
        }
    }
}
//清空缓存
function clear_cache() {
	localStorage.clear();
	load();

}
