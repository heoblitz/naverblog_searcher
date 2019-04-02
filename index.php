<?php
	$msg = '';
	if(isset($_POST["login"]))
	{
		if(empty($_POST["user_email"]) || empty($password = $_POST["user_password"]))
		{
		$msg = '<label>빈칸을 채워주세요</label>';
		}

		else
		{
			if($password == "비밀번호 하드코딩")
			{	
				header("Location: " . "http://" . $_SERVER['HTTP_HOST'] . "\\testa.php");
				exit();
			}
			else
			{
				$msg = '<label>잘못된 비밀번호 입니다</label>';
			}
	}
}
		
?>

<!DOCTYPE html>
<html>
<head>
<title>naver blog searcher</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
</head>
<body>
<br />



<div class="container">
<h2 align="center">naver blog searcher</h2>
<br />
<div class="panel panel-default">
<div class="panel-heading">로그인</div>
<div class="panel-body">

<!-- 로그인 폼 -->
<form method = "post">
<span class="text-danger"><?php echo $msg; ?></span>
<div class="form-group">
<label>아이디</label>
<input type="text" name="user_email" id="user_email" class="form-control" />
</div>

<div class="form-group">
<label>비밀번호</label>
<input type="password" name="user_password" id="user_password" class="form-control" />
</div>

<div class="form-group">
<input type="submit" name="login" id="login" class="btn btn-info" value="로그인"/>
</div>
</form>
</div>
</div>
</div>
</div>
</body>
</html>


