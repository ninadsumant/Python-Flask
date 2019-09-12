from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message1 = "Hello Buddy!"
    message2 = "Let's have a cup of coffee."
    message3 = "it's raining outside"
    return render_template('greet.html', message1 = message1,message2 = message2,message3= message3)
if __name__ == '__main__':
    app.run(debug=True)
    
   
 #HTML File 'greet.html'

'''
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Greet</title>
</head> 
<body>  
    <h1>{{message1}}</h1>
    <h2> {{message2}} </h2>
    <h3> {{message3}} </h3>
</body>
</html>
 '''
