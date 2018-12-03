 function loadreview(i) {
        var review_btn = $('#review-'+i);
        var review_box = $('#pinglun-'+i);
        review_btn.click(function () {
            review_box.stop().toggle();
            return false
        })
    }
    function clase(i) {
        $('#pinglun-'+i).click(function () {
            $(this).hide()
        })
    }

    function load() {
        var data_reverse = loadData('local-content');
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
                                    <a href="javascript:loadreview(${i})" id="review-${i}">💬<b>${commentCount}</b></a>  
                               </div>
                               <a href="#">❤️私藏</a>
                                
                              
                               <span>来自我自己发布</span>
                           </div>
                           <div class="pinglun-box" id="pinglun-${i}">
                               <div class="pinglun">
                                </div>
                                <div class="review">
                                       <div class="review-box">
                                           <div class="review-details">
                                           <span class="review-details-title">最新评论</span><span class="review-close" onclick="clase(${i})">x</span>
                                           <ul>
                                               <li>
                                                   <p>admin: <span>这是评论详情</span></p>
                                               </li>
                                           </ul>
                                       </div>
                                       <div class="review-box-input">
                                           <input type="text" placeholder="请输入..." class="review-input" id="msg-${i}"><a href="javascript:gain_review(${i})" class="review-box-input-btn" id="b-${i}">评论</a>
                                       </div>
                                       </div>
                                </div>
                            </div>
                            
                        </li>`;
            }
        content.innerHTML = Html;
    };
    function saveData(data,obj) {
     localStorage.setItem(obj,JSON.stringify(data));
}

    function loadData(obj) {
        var localdata = localStorage.getItem(obj);
        if (localdata != null){
            return JSON.parse(localdata)
        }else{
            return []
        }
    }
    function update(i,msg,value) {
        var data = loadData('local-content').reverse();
        var newContent = data.splice(i,1)[0];
        console.log(newContent);
        newContent[msg] += value;
        data.splice(i,0,newContent);
        saveData(data.reverse(),'local-content');
        load()
        }
