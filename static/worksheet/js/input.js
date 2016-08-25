/*
 * 日期选择器初始化
 * 语言
 * 选择后自动关闭
 * 今天高亮
 * 首先显示的视图
 * 日期时间选择器所能够提供的最精确的时间选择视图
 * 当选择器关闭的时候，是否强制解析输入框中的值
 */
$('#datetimepicker').datetimepicker({
    language:  'zh-CN',
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0
});


$('#type,#client').bind('change',function () {
    $(this).children("option[value='0']").remove();
})


var account = $('#account'),
    content = $('#content'),
    method = $('#method'),
    client = $('#client'),
    type = $('#type'),
    datetimepicker = $('#datetimepicker'),
    input_list = [account,content,method,client,type,datetimepicker],
    flag = true;
//    表单验证
$('.submit').click(function(){
    var flag = true;
    $(".error").children().text("")
    //验证非空
    for(var i in input_list) {
        if(parseInt(input_list[i].val())==0 || !input_list[i].val()) {
            input_list[i].parent().siblings('.error').children().text('请输入');
            flag = false;
        }
    }
    //验证电话号码
    if(!(/^1[3|4|5|7|8]\d{9}$/.test(account.val()))){
        account.parent().siblings('.error').children().text('格式不正确');
        flag = false;
    }
    if(flag) {
        $('#input_form').submit()
    }
})