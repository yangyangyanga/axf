$(document).ready(function(){
    $('#btn').bind("click", function(){
        $('p').toggle(1000)
        $.ajax({
            type:"get",
            url:"/studentsinfo/",
            dataType: "json",
            success:function(data, status){
                console.log(data)
                var d = data["data"]

                for(var i = 0; i < d.length; i++){
                    $p = $("<p>" + d[i][0] + "  " + d[i][1] +  "</p>")
                    $('#btn').after($p)
//                    document.write("<p>" + d[i][0] +"</p>")
                }
            }
        })
    })

})