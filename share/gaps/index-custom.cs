<html lang="en">
	<head>
		<title>Amplify EGS Monitoring</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<meta name="description" content="GAPS <?cs var:GAPS.version ?> frontpage, &copy; gempa GmbH"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
		<link rel="icon" type="image/x-icon" href="share/favicon.ico">
		<link rel="stylesheet" href="share/css/font-opensans.css">
	</head>
	<style>
		html {
			font-family: "Open Sans";
		}

		html, body {
			margin: 0;
		}

		.container {
			max-width: 1200px;
			margin: 1rem auto;
		}

		.container.flex {
			display: flex;
			flex-direction: row;
			flex-wrap: wrap;
		}

		.container > .card {
			width: 25%;
		}

		.button {
			padding: 0.5em 1em;
			background: #7AD4E2;
			color: #222;
			border-radius: 0.25em;
			text-decoration: none;
			transition: background 0.3s;
		}

		.button:hover {
			background: #bce9f0;
			transition: background 0.3s;
		}

		.card {
			text-align: center;
			padding: 2rem;
			box-sizing: border-box;
			color: #555;
		}

		.card > h1 {
			font-weight: 100;
			font-size: 1.7rem;
			margin-top: 0;
		}

		.card p {
			margin: 2em 0;
		}

		.carousel {
			position: relative;
		}

		.carousel > ol {
			display: flex;
			margin: 0;
			padding: 0;
			overflow: hidden;
		}

		.carousel > ol > li {
			position: relative;
			display: block;
			list-style: none;
			width: 100%;
			box-sizing: border-box;
			flex-shrink: 0;
		}

		.carousel > ol > li > img {
			width: 100%;
			height: auto;
		}

		.carousel > ol > li > p {
			position: absolute;
			bottom: 10%;
			left: 0;
			width: 100%;
			margin: 0;
			text-align: center;
			color: white;
			font-width: 600;
			font-size: 2em;
			text-shadow: 0 1px 2px rgba(0,0,0,0.6);
		}

		.carousel > .control {
			position: absolute;
			top: 0;
			height: 100%;
			width: 20%;
			cursor: pointer;
			font-weight: bold;
		}

		.carousel > .control.left {
			left: 0;
		}

		.carousel > .control.right {
			right: 0;
		}

		.carousel > .control:hover {
			transition: background 0.3s;
		}

		.carousel > .control.left:hover {
			background: linear-gradient(to right, rgba(0,0,0,0.6), rgba(0,0,0,0.4) 25%, rgba(0,0,0,0));
		}

		.carousel > .control.right:hover {
			background: linear-gradient(to left, rgba(0,0,0,0.6), rgba(0,0,0,0.4) 25%, rgba(0,0,0,0));
		}

		.logo {
			display: flex;
			justify-content: space-between;
			align-items: center;
		}
		#amtlogo {
			width: 15%;
		}
		#snllogo {
			width: 12%;
		}
		#lbllogo {
			width: 8%
		}
		#usgslogo {
			width: 15%;
		}

		@media screen and (max-width: 60rem) {
			.container > .card {
				width: 50%;
			}
		}

		@media screen and (max-width: 40rem) {
			.container > .card {
				width: 100%;
			}
		}
	</style>
	<body>
		<div class="carousel">
			<ol><?cs set:index = 0?><?cs each:item = apps?>
				<li>
					<img src="share/images/carousel_<?cs var:index?>.png" alt="AMT Site">
					<p></p>
				</li><?cs set:index = index+1?><?cs /each?>
			</ol>
			<div class="left control" onclick="cStep(-1)"></div>
			<div class="right control" onclick="cStep(+1)"></div>
		</div>
		<div class="container logo">
			<img id="lbllogo" src="share/images/7_BL_Vert_547.svg" alt="LBNL logo">
			<img id="amtlogo" src="share/images/AMT-good-logo_v1.svg" alt="Amplify EGS logo">
			<img id="snllogo" src="share/images/sandia-national-laboratories-cropped.svg" alt="SNL logo">
			<img id="usgslogo" src="share/images/USGS_logo_green.png" alt="USGS logo">
		</div>
		<div class="flex container"><?cs each:item = apps?>
			<div class="card">
				<h1><?cs var:item.title?></h1>
				<p><?cs var:item.description?></p>
				<p>
					<a class="button" href="<?cs var:item.path?>">Launch application</a>
				</p>
			</div><?cs /each?>
		</div>
		<script>
			let cItems = document.querySelectorAll('.carousel > ol > li');
			let index = 0;
			let autoPlay = null;

			window.cStep = function(step) {
				if ( autoPlay ) {
					window.clearInterval(autoPlay);
					autoPlay = null;
				}
				window.cShow(step);
			}

			window.cShow = function(step) {
				if ( step ) index = index + step;
				if ( index < 0 ) index = cItems.length-1;
				else if ( index >= cItems.length ) index = 0;
				cItems[index].scrollIntoView({ behavior: 'smooth' });
			}

			window.addEventListener('resize', function(event) {
				cItems[index].scrollIntoView();
			});

			autoPlay = window.setInterval(function() {
				window.cShow(1);
			}, 2000);
		</script>
	</body>
</html>
