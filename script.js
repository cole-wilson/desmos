function go() {
	var fileToLoad = document.getElementById("objfile").files[0];
	var fileReader = new FileReader();
	fileReader.onload = function(fileLoadedEvent){
		var textFromFileLoaded = fileLoadedEvent.target.result;
		parse(textFromFileLoaded)
	}
  fileReader.readAsText(fileToLoad, "UTF-8");
}

let output = document.getElementById("output");

function parse(t) {
	let lines = t.split("\n").filter(e=>e.length>0);

	var vx=[];
	var vy=[];
	var vz=[];
	var fa=[];
	var fb=[];
	var fc=[];

	for (var i=0;i<lines.length;i++) {
		var line = lines[i].split(/(\s+)/g).filter(e=>(!e.includes(" ")&&e.length>0));
		// console.log(line)
		if (line[0] == 'v') {
			vx.push(line[1]);
			vy.push(line[2]);
			vz.push(line[3]);
		}
		else if (line[0] == 'f') {
			fa.push(line[1]);
			fb.push(line[2]);
			fc.push(line[3]);
		}
	}
	// console.log(vx, vy, vz, fa, fb, fc)
	output.innerHTML = `
$$
\\begin{align}
B_x &= [${vx}]\\\\
B_y &= [${vy}]\\\\
B_z &= [${vz}]\\\\
F_a &= [${fa}]\\\\
F_b &= [${fb}]\\\\
F_c &= [${fc}]
\\end{align}
$$
<br>
<code>raw text (copy/paste):</code><br>
<textarea id='copy' readonly>
B_x=[${vx}]
B_y=[${vy}]
B_z=[${vz}]
F_a=[${fa}]
F_b=[${fb}]
F_c=[${fc}]
</textarea>
`;
	document.getElementById("copy").select();
	MathJax.typeset();
}
