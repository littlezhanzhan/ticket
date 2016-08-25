
var account = $('#account'),
    client_select = $('.client'),
    type_select = $('.type');
    datetimepicker = $('#datetimepicker'),
    datetimepicker2 = $('#datetimepicker2');



//初始化日期插件
$('#datetimepicker,#datetimepicker2,.date').datetimepicker({
    language:  'zh-CN',
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0
});

//删除请选择
$('#type,#client').bind('change',function () {
    $(this).children("option[value='0']").remove();
})

//提交表单
$('.submit').click(function(){
    var flag = true;
    $(".error").children().text("")
    //验证电话号码
    if(account.val() && !(/^1[3|4|5|7|8]\d{9}$/.test(account.val()))){
        account.parent().siblings('.error').children().text('格式不正确');
        flag = false;
    }
    //验证日期
    var start_date = datetimepicker.val().split('-');
    var end_date = datetimepicker2.val().split('-');

    if((!$('#datetimepicker').val() && $('#datetimepicker2').val())|| ($('#datetimepicker').val() && !$('#datetimepicker2').val())){
        $('#search_form').children(':eq(3)').children('.error').children().text('格式不正确');
        flag = false;
    }

    for(var i = 0; i < 3; i++) {
        if(parseInt(end_date[i]) - parseInt(start_date[i]) <0){
            flag = false;
            datetimepicker.parent().siblings('.error').children().text('格式不正确');
        }
    }
    //提交
    if(flag) {
        $('#search_form').submit();
    }
})

//修改
$('.modify').bind('click',function(){
    var data = [];
    var tr = $(this).parent().parent();
    data[0] = tr.data('id');
    for(var i = 0; i < 6; i++){
        if(i == 0) {
            data.push(parseInt(tr.children('td').eq(i).children().text()));
        }
        else {
            if(i==3|| i==4) {
                data.push(parseInt(tr.children('td').eq(i).children().val()));
            } else{
                data.push(tr.children('td').eq(i).children().val());
            }
        }
    }
    console.log(data)
    $.ajax({
        type:'POST',
        url:'./modify',
        data:{
            id:data[0],
            account:data[1],
            content:data[2],
            method:data[3],
            client:data[4],
            type:data[5],
            date:data[6],
            customerid:data[7]
        },
        success:function(){
            alert('修改成功');
            window.location.reload();
        }
    })
})

