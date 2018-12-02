$(function () {
    //加载页面内容
    // load();

    $('.bar-a').mouseenter(function () {
        $(this).addClass('header-bar-active');
        $(this).css('text-decoration','none');
    });
    $('.bar-a').mouseleave(function (){
        $(this).removeClass('header-bar-active');
    });
    $('.active').click(function () {
        $('#login-background').show(500)

    });
    $('.close').click(function () {
        $('#login-background').hide(500)

    });
    //选中topbar上的a标签然后设置样式为有背景图片
    $('.daf-style').click(function () {
        $(this).addClass('bg-style').parent('li').siblings('li').children('a').removeClass('bg-style')
    });

    //单击发布之后弹出发布框（模态框）
    $('.main-top-button').click(function () {
        $('#issue').show(500);
    });
    $('.issue-header span').click(function () {
        $('#issue').hide(500)
    });

    $('.issue-type-list').click(function () {
        $(this).addClass('issue-type-pitch-on').siblings('li').removeClass('issue-type-pitch-on')
    });

    //发布框中链接发布的发布到哪个区
    $('.issue-to-class').click(function () {
        $(this).addClass('btn-image').siblings('.issue-to-class').removeClass('btn-image');
    });

    $('#link').click(function () {
        $('#link-issue').addClass('content-show');
        $('#text-issue').removeClass('content-show');
        $('#img-issue').removeClass('content-show');
    });

    $('#text').click(function () {
        $('#text-issue').addClass('content-show');
        $('#link-issue').removeClass('content-show');
        $('#img-issue').removeClass('content-show');
    });

    $('#image').click(function () {
       $('#img-issue').addClass('content-show');
       $('#link-issue').removeClass('content-show');
       $('#text-issue').removeClass('content-show')
    });

    $('#text-btn').click(function () {
        if ($('.input-text')==null) {
            alter('请输入内容')
        }else {
            let text = $('.input-text').val();
            let likecount = 0;
            let comment = 0;
            let newList = {
                text:text,
                likecount:likecount,
                comment:comment,
            };
            data = loadData();
            data.push(newList);
            saveData(data);
             $('#issue').css('display','none');
             $('.input-text').val('');
            load()
        }
        });

});
    function load() {
        var data_reverse = loadData();
        var data = data_reverse.reverse();
        var Html = '';
        var content = document.getElementById('content');
        for (var i in data) {
            var text = data[i].text;
            var likeCount = data[i].likecount;
            var commentCount = data[i].comment;
            Html += `<li class="item">
                           <div class="digest">
                               <a href="#">${text}</a>
                               <img src="./images/car1.png" alt="" class="profile-photo">
                           </div>
                           <div class="little-btn-bar">
                               <a href="javascript:update(${i},'likecount',1)" id="like-${i}">👍 <b>${likeCount}</b></a>
                               <div class="review">
                                    <a href="#">💬<b>${commentCount}</b></a>  
                               </div>
                                   <a href="#">❤️私藏</a>
                                
                              
                               <span>来自我自己发布</span>
                           </div>
                            <div class="pinglun">

                            </div>
                            <div class="review">
                                   <div class="review-box">
                                       评论框
                                   </div>
                            </div>
                        </li>`;
            }
        content.innerHTML = Html;
    };
    function saveData(data) {
     localStorage.setItem('local-content',JSON.stringify(data));
}

    function loadData() {
        var localdata = localStorage.getItem('local-content');
        if (localdata != null){
            return JSON.parse(localdata)
        }else{
            return []
        }
    }
    function update(i,msg,value) {
        var data = loadData().reverse();
        var newContent = data.splice(i,1)[0];
        console.log(newContent);
        newContent[msg] += value;
        data.splice(i,0,newContent);
        saveData(data.reverse());
        load()
        }



