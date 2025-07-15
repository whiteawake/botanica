<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Login - Botanica</title>
	<meta name="author" content="Asha" />
	<link rel="stylesheet" type="text/css" media="screen" href="login.css" />
	<link rel="icon"type="image/x-icon" href="../../resources/images/tree.png" />
	<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
	<meta http-equiv="refresh" content="7; url=/botanica/welcome.py">
    	<script type="text/javascript">
    	$(document).ready(function(){
  			animate();
		});
		function animate(){
			$(".progress_bar").width("0px");
			$(".progress_bar").animate({
				width: '99%'
			}, 6000, function(){
				setTimeout('animate()',9900);
			});
		}
	</script>
</head>
<body>
	<link href='http://fonts.googleapis.com/css?family=Noto+Sans' rel='stylesheet' type='text/css'>
	<div class="window">
		<div class="middle">
		</div>
	</div>
	<h1>Asha</h1>
	<p>Welcome</p>
	<div id="loader" class="loading">
		<div class="progress">
			<div class="progress_bar">
			</div>
			<div id="prog_status">
				Loading...
			</div>
		</div>
	</div>
</body>
</html>