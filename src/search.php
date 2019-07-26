<!DOCTYPE html>
<?php $msg = date("Y-m-d h:i:s"); ?>
<html lang="ko">
<head>
    
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="http://bootstrapk.com/favicon.ico">

    <title>Naver blog searcher</title>
<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<style>
        /* Sticky footer styles-------------------------------------------------- */
        html {
          position: relative;
          min-height: 100%;
        }
        body {
          /* Margin bottom by footer height */
          margin-bottom: 60px;
        }
        .footer {
          position: absolute;
          bottom: 0;
          width: 100%;
          /* Set the fixed height of the footer here */
          height: 60px;
          background-color: #f5f5f5;
        }

</style>

          </head>
<link rel="canonical" href="https://getbootstrap.com/docs/3.3.7/examples/sticky-footer-navbar/">

  <body>

    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="http://211.249.60.117/testa.php">Naver blog searcher <?php echo($msg); ?></a>
        </div>
      </div>



    </nav>
        <br><br>
    <!-- Begin page content -->
    <div class="container">
      <div class="page-header">
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


      <p class="lead">
   <?php
if(isset($_GET["search"]))
{
$keyword = $_GET['keyword'];
$start_date = $_GET['start_date'];
$end_date = $_GET['end_date'];
$select = $_GET['select'];
$cmd = "python3 ./main.py \"$keyword\" $start_date $end_date $select";
ob_implicit_flush(true);
ob_end_flush();
$env = array('PATH' => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games',
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
      </p>
      
    </div>




</body></html>
