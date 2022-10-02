<!DOCTYPE HTML>
<html lang="en">

<head>
    <title>Cognitio - All-In-One Gateway Platform to EO Learning</title>
    <link rel="stylesheet" href="resources/app_css.css" />
    <link rel="stylesheet" href="resources/w3.css" />
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-highway.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" >
    
    <script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-metro.css">
    <link rel="shortcut icon" href="favicon.png" type="image/x-icon" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="title" content="Cognitio - All-In-One Gateway Platform to EO Learning" />
    <meta name="description" content="Cognitio is your all-in-one gateway platform to Earth Observations (EO) learning. We bridge the gap between training and learning to enable policymakers and decision makers around the world have access to the most relevant trainings and courses and empower them with the knowledge and skills in addressing the world's most pressing social problems." />
    <meta property="og:url" content="https://dataquest.opendata.org.ph" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Cognitio - All-In-One Gateway Platform to EO Learning" />
    <meta property="og:description" content=" Cognitio is your all-in-one gateway platform to Earth Observations (EO) learning. We bridge the gap between training and learning to enable policymakers and decision makers around the world have access to the most relevant trainings and courses and empower them with the knowledge and skills in addressing the world's most pressing social problems." />
    <meta property="og:image" content="images/cognitio_white_resized.jpg" />
	
</head>

<body class="Roboto">
    <header class="w3-top w3-black w3-row-padding">
        <div class="w3-bar w3-container w3-col l12 m12">
            <div id ="screen-logo" class="w3-padding w3-bar-item w3-hide-medium w3-hide-small">
                <a href ="./?page=home" style="margin-left: 140px;"> 
                <img src="images/cognitio_white_resized.jpg" height=100px   alt="Cognitio" /></a>
            </div>
			<div id ="mobile-logo" class="w3-bar-item w3-hide-large">
                <a href ="./?page=home" class= ""> 
                <img src="images/cognitio_white_resized.jpg" height=50px   alt="Cognitio" /></a>
            </div>
            <div class="w3-hide-large w3-bar-item w3-button w3-right w3-hover-text-white w3-hover-none" style="padding: 15px;" onclick="toggle('navBar');">
                <i class="w3-xxlarge fa fa-bars"></i>
            </div>
            <div id = "main" class="w3-padding w3-hide-small w3-hide-medium">
                <a href="http://courses-gateway-cognitio.xyz/courses" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-center" style="height: 100px; padding-top: 45px;   margin-left: 60px;">Course Catalog</a>
                <a href="./?page=competitions" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-center" style="height: 100px; padding-top: 45px;">Competitions</a>
                <a href="./?page=blog" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-center" style="height: 100px; padding-top: 45px;">Blog</a>
                <a href="./?page=community" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-center" style="height: 100px; padding-top: 45px;  ">Community</a>
                 <a href="http://courses-gateway-cognitio.xyz/auth/login" class="w3-bar-item w3-button w3-black w3-border w3-round-large w3-hover-light-blue w3-center" style="max-width: 150px; margin:35px 15px 25px 150px; padding-bottom: 8px">Sign In</a>
                 <a href="http://courses-gateway-cognitio.xyz/auth/register" class="w3-bar-item w3-button w3-highway-blue w3-round-large w3-hover-light-blue w3-center" style="max-width: 150px; margin:35px 20px 25px 0px; padding-bottom: 8px">Get Started</a>
               
               
</div>
		<nav id="navBar" class="w3-bar-block w3-xlarge w3-center w3-hide">
			<a href="http://courses-gateway-cognitio.xyz/courses" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none">Course Catalog</a>
			<a href="./?page=competitions" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none">Competitions</a>
			<a href="./?page=blog" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none">Blog</a>
			<a href="./?page=community" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none">Community</a>
            <a href="http://courses-gateway-cognitio.xyz/auth/login" class="w3-bar-item w3-button w3-black w3-border w3-round-large w3-hover-light-blue">Sign In</a>
            <a href="http://courses-gateway-cognitio.xyz/auth/register" class="w3-bar-item w3-button w3-highway-blue w3-round-large w3-hover-light-blue" style="margin: 10px 0px 10px 0px;">Get Started</a>
        </nav>			
			
			
    </div>
    </header>

    
    <div class="w3-row">

    <?php
		include ('home.php');
		include ('team.php');
		include ('about.php');
		include ('blog.php');
		include ('community.php');
		include ('competitions.php');
		
		if (isset($_GET["page"])) {
			$page = $_GET["page"];
			switch ($page) {
				case "home":
					showHome();
					break;
				case "team":
					showTeam();
					break;
				case "about":
					showAbout();
					break;
				case "blog":
					showBlog();
					break;
				case "community":
					showCommunity();
					break;
				case "competitions":
					showCompetitions();
					break;
		} 
		} else {
			showHome();
		}
		?>


    </div>









    <footer class="w3-light-gray  w3-medium w3-bar">
        <div class="w3-bar w3-container w3-col l12 m12">
        <div style="height: 20px;"></div>
            <div id ="screen-logo_footer" class="w3-padding w3-bar-item w3-hide-medium w3-hide-small">
                <a href ="./?page=home" style="margin-left: 120px;"> 
                <img src="images/cognitio_logo_resized.jpg" height=120px   alt="Cognitio"/>
                <p class="w3-center w3-small" style="margin-left: 90px;"> &copy; 2022 CirroLytix Research Services</p></a>
            </div>
            <div id = "main-footer" class="w3-padding w3-hide-small w3-hide-medium">
                <a href="./?page=about" class="w3-bar-item w3-button w3-hover-none w3-center" style="height: 100px; padding-top: 45px; margin-left: 60px; margin-right: 80px;">About</a>
                <a href="./?page=team" class="w3-bar-item w3-button w3-hover-none w3-center" style="height: 100px; padding-top: 45px; margin-right: 80px;">Team</a>
                <div class="w3-bar-item w3-button w3-hover-none w3-center" style="height: 100px; padding-top: 45px;">Connect with Us</div>    
                <div class ="w3-bar-item w3-button w3-hover-none w3-center" style="height: 100px; padding-top: 45px; margin-right: 3px;">
                <a href="https://www.facebook.com/cirrolytix"> <img src="images/fb_icon.jpg" height=25px   alt="" />&nbsp;</a>  
                <a href="https://www.twitter.com/cirrolytix"><img src="images/twitter_icon.jpg" height=25px   alt="" />&nbsp;</a>
                <a href="mailto:support@cirrolytix.com"><i class="fa fa-envelope" style="font-size:24px"></i></a>
                </div>
            </div>

            <div id ="mobile-logo" class="w3-bar-item w3-hide-large">
                <a href ="./?page=home" class= ""> 
                <img src="images/cognitio_logo_resized.jpg" height=100px   alt="Cognitio" />
                <p class="w3-small" style="margin: auto;"> &copy; 2022 CirroLytix Research Services</p></a>
            </div>

            <nav id="navBarFooter" class="w3-bar-block w3-left w3-hide-large">
			<a href="./?page=about" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none ">About</a>
			<a href="./?page=team" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none">Team</a>
			<a href="" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none">Connect with Us</a>

			<div class="w3-bar-item w3-button w3-hover-text-white w3-hover-none">
            <a href ="https://www.facebook.com/cirrolytix">  <img src="images/fb_icon.jpg" height=25px   alt="" />&nbsp;</a>
            <a href ="https://www.twitter.com/cirrolytix"><img src="images/twitter_icon.jpg" height=25px   alt="" />&nbsp;</a>
            <a href ="mailto:support@cirrolytix.com"> <i class="fa fa-envelope" style="font-size:24px"></i></a>
            
            <div>
        </nav>			

        </div>
      
    </footer>


    

    <script src="resources/app_js.js"></script>
</body>

</html>