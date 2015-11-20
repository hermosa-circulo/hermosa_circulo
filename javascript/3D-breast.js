
	var node = document.getElementById("canvas");
	var renderer = new THREE.WebGLRenderer();
	renderer.setSize(500, 500);
	node.appendChild( renderer.domElement );
	
      	var scene = new THREE.Scene();

      	var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
      	camera.position = new THREE.Vector3(0, 0, 8);
      	camera.lookAt(new THREE.Vector3(0, 0, 0));
      	camera.position.z = 50;	
	camera.rotation.x += 0.2;
	trackball = new THREE.TrackballControls(camera, node);
	//trackball.noRotate = false;
	//trackball.rotateSpeed = 1.0;
	//trackball.noZoom = false;
	//trackball.zoomSpeed = 1.0;
	//trackball.noPan = false;
	//trackball.panSpeed = 1.0;
	//trackball.staticMoving = true;
	//trackball.dynamicDampingFactor = 0.3;
    light = new THREE.DirectionalLight( 0xffffff );
	light.position.set( 25, 50, 25 );
	scene.add( light );

	light2 = new THREE.DirectionalLight( 0x002288 );
	light2.position.set( 100, 25, 21 );
	scene.add( light2 );
	
	light3 = new THREE.DirectionalLight( 0x002288 );
	light3.position.set( 25, 10, 100 );
	scene.add( light3 );
	light4 = new THREE.DirectionalLight( 0x002288 );
	light4.position.set( -100, -25, 21 );
	scene.add( light4 );
	
	light5 = new THREE.DirectionalLight( 0x002288 );
	light5.position.set( 25, -10, -100 );
	scene.add( light5 );

	light = new THREE.AmbientLight( 0x222222 );
	scene.add( light );
	
	var object = new THREE.Mesh();
	var loader = new THREE.OBJLoader();
	loader.load( 'model2.obj', function ( object ) {
		scene.add(object);
		if (mesh.geometry.animation.name) {
        	THREE.AnimationHandler.add(mesh.animation);
        	animation = new THREE.Animation(mesh, mesh.animation.name, THREE.AnimationHandler.CATMULLROM);
        	animation.play();
        }
      	animate();
	});


	var object = new THREE.Mesh();
	var loader = new THREE.OBJLoader();
	loader.load( 'model2.obj', function ( object ) {
		scene.add(object);
		object.position.set(50,0,0)
		if (mesh.geometry.animation.name) {
        	THREE.AnimationHandler.add(mesh.animation);
        	animation = new THREE.Animation(mesh, mesh.animation.name, THREE.AnimationHandler.CATMULLROM);
        	animation.play();
        }
      	animate();
	});


	var baseTime = +new Date;
   	function render() {
        requestAnimationFrame(render);
	trackball.update();
        renderer.render(scene, camera);
      	};
      render();
