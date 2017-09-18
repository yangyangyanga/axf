$(document).ready(function(){
    $("#btn").click(function(){
        $.ajax({
            type: "get",
            url: "/studentsinfo/",
            typeof: "json",
            success:function(data, status){
                console.log(data)
                var d = data["indd"]

                for(var i = 0; i < d.length; i++){
                    console.log(d[i][0] + "--" + d[i][1])
                }

            }
        })
    })
})