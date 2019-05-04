var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlEncodedParser = bodyParser.urlencoded({extended: false});

app.use(express.static('public'));

app.get('/', function(req, res){
	res.redirect('/home.html');
})

app.get('/home.html', function(req, res){
	res.sendFile(__dirname + "/" + "home.html");
})

app.get('/get_names', function(req, res){
	response = {
		first_name:req.query.first_name,
		last_name:req.query.last_name
	};
	console.log(response);
	res.end(JSON.stringify(response));
})

app.post('/post_names', urlEncodedParser, function(req, res){
	response = {
		first_name:req.body.first_name,
		last_name:req.body.last_name
	};
	console.log(response);
	res.end(JSON.stringify(response));
})

var server = app.listen(8081, function(){
	var host = server.address().address;
	var port = server.address().port;

	console.log("Example app listening at port %s", port);
})
