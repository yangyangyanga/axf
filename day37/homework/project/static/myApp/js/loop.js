$(document).ready(function(){
	$("#loop ul li:first").css("background-color", "yellow")
//	$("#loop ul li:eq(1)").css("background-color", "yellow")
	
	var currentPage = 1
	var timer = setInterval(startloop, 1000);
	function startloop(){
		currentPage++;
		changePage();
	}
	function changePage(){
		if(currentPage == 4){
			currentPage = 1;
		}else if(currentPage == 0){
			currentPage = 3;
		}
//		console.log(currentPage)
		$("#loop img").attr("src", "/static/myApp/img/"+ currentPage + ".jpg")
		$("#loop ul li").css("background-color", "white")
		$("#loop ul li").eq(currentPage-1).css("background-color", "yellow")
	}
	$("#loop").hover(function(){
		clearInterval(timer)
	},function(){
		timer = setInterval(startloop, 1000)
	})
})
