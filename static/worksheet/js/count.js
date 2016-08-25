var client_cn = ['安卓端','苹果端','平台侧','web','PC端'],
    type_cn =['上传','下载','解绑','换绑','客户端异常','账号异常','VIP开通','客户端bug','文件损坏','网络故障','dns问题'],
    client_list = [],
    type_list=[],
    datetimepicker = $('#datetimepicker'),
    datetimepicker2 = $('#datetimepicker2'),
    today = new Date().getFullYear() + '-' + (new Date().getMonth()+1) + '-' + new Date().getDate();

function createList(data,cn,list) {
    for(var i = 0; i < cn.length; i++) {
        var one = [cn[i],data[i]];
        list.push(one);
    }
}

function createTr(array,tbody){
    for(var i = 0; i < array.length; i++) {
        var tr = "<tr><td >"+array[i][0]+"</td><td>"+array[i][1]+"</td></tr>"
        $(tbody).children().append(tr)
    }
}

function createPieRenderer(id,array){
    $.jqplot(id, array, {
        seriesDefaults: {
            color: 'white',
            renderer: $.jqplot.PieRenderer,
            rendererOptions: {
                showDataLabels: true
            }
        },
        legend: {
            show: true,
            location: "e"
        },
        grid:{
            background: "transparent",
            borderColor: "transparent",
            shadow: false
        }
    });
}

function isEmpty(list){
    var sum = 0;
    for(var i = 0; i < list.length; i++) {
        if(list[i][1]>0){sum++}
    }
    if(sum == 0) {
        return true
    } else{return false}
}

function addPieRenderer(list,div_id,table){
    if(! isEmpty(list)){
        $(table).after('<div id="' + div_id + '"></div>')
        createPieRenderer(div_id,[list])
    } else{
        $(table).after('<div class="no_data col-md-6">暂无数据</div>')
    }
}


createList(client,client_cn,client_list)
createTr(client_list,'.client_count')
createList(type,type_cn,type_list)
createTr(type_list,'.type_count')

addPieRenderer(client_list,'chart','.client_count')
addPieRenderer(type_list,'type','.type_count')


$('#datetimepicker,#datetimepicker2,.date').datetimepicker({
    language:  'zh-CN',
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0,
    endDate: today
});

$('.submit').click(function(){
    var flag = true;
    $(".error").children().text("")
    //验证日期
    var start_date = datetimepicker.val().split('-');
    var end_date = datetimepicker2.val().split('-');
    if((!datetimepicker.val() && datetimepicker2.val())|| (datetimepicker.val() && !datetimepicker2.val())){
        datetimepicker.parent().siblings('.error').children().text('格式不正确');
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
        $('#count_form').submit();
    }
})