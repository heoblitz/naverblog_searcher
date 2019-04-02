<!DOCTYPE html>
<?php
        $msg = date("Y-m-d h:i:s");
?>
<html>
<head>
<title> naver blog searcher
</title>
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
<div class="panel-heading"><?php echo "$msg"; ?></div>
<div class="panel-body">

<!-- 검색 폼 -->
<form class="form-inline">
  <div class="form-group">
    <label for="exampleInputName2">키워드</label>
    <input type="text" name="keyword"class="form-control" id="keyword" value="<?php echo isset($_GET['keyword']) ? $_GET['keyword'] : '' ?>"
 placeholder="안국 어니언">
  </div>
  <div class="form-group">
    <label for="exampleInputName2">검색 기간 설정</label>
    <input type="date" class="form-control" name = "start_date" id="start_date" value="<?php echo isset($_GET['start_date']) ? $_GET['start_date'] : '' ?>"  placeholder="20190301">
  </div>
  <div class="form-group">
    <input type="date" class="form-control" name = "end_date" id="end_date" value="<?php echo isset($_GET['end_date']) ? $_GET['end_date'] : '' ?>" placeholder="20190301">
  </div>

  <div class="form-group">
    <label for="exampleInputName2">검색 방법</label>
	<select name="select" class="form-control" >
		<option value ="sim" <?php if($_GET['select'] == 'sim') {echo "selected=selected"; } ?>>관련도순</option>
		<option value ="date" <?php if($_GET['select'] == 'date') {echo "selected=selected"; } ?>>최신순</option>
	</select>
  </div>
  <button type="submit" name="search" id="serach" class="btn btn-default">검색</button>
  <button type="button" class="btn btn-default" onclick="location.href='testa.php' ">초기화</button>
</form>
</div>
</form>
</div>
</div>
</div>
</div>

<div class="return">
<h1>
<div class="container">
<div class="panel panel-default">
<div class="panel-body">
<form class="form-inline">
<?php

if(isset($_GET["search"]))
{
$keyword = $_GET['keyword'];
$start_date = $_GET['start_date'];
$end_date = $_GET['end_date'];
$select = $_GET['select'];

$cmd = "/usr/bin/pypy3.5-v7.0.0-linux64/bin/pypy3 ./main.py \"$keyword\" $start_date $end_date $select";
ob_implicit_flush(true);
ob_end_flush();

$env = array('PATH' => 'usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/bin/pypy3.5-v7.0.0-linux64/bin',
'LANG' => 'ko_KR.UTF-8');

$descriptorspec = array(
   0 => array("pipe", "r"),   // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),   // stdout is a pipe that the child will write to
   2 => array("pipe", "w"),    // stderr is a pipe that the child will write to
);
flush();

$process = proc_open($cmd, $descriptorspec, $pipes, realpath('./'), $env);

if (is_resource($process)){
    while ($s = fgets($pipes[1])){
        print "$s";
        flush();

    // Could be done better? Only here to prevent runaway CPU
    sleep(0.1);
    }
}
}
?>
</form>
</div>
</div>
</div>
 </h1>
 </div>
</body>
</html>
