from flask import Flask,request,redirect,render_template_string
from datetime import datetime

app=Flask(__name__)

books=[]

page="""

<!DOCTYPE html>
<html>

<head>

<title>Library Fine System</title>

<style>

body{
background:#f2f2f2;
font-family:Arial;
padding:20px;
}

h1{
text-align:center;
color:darkblue;
}

form{
background:white;
padding:20px;
border-radius:10px;
margin-bottom:20px;
}

input{
padding:10px;
margin:5px;
width:25%;
}

button{
padding:10px 20px;
background:green;
color:white;
border:none;
cursor:pointer;
}

table{
width:100%;
background:white;
border-collapse:collapse;
}

th,td{
border:1px solid gray;
padding:10px;
text-align:center;
}

th{
background:darkblue;
color:white;
}

tr:hover{
background:#ddd;
}

.total{
margin-top:20px;
background:white;
padding:15px;
font-size:20px;
}

</style>

</head>

<body>

<h1>📚 Library Fine Management System</h1>

<form method="POST" action="/add">

<input type="text" name="book" placeholder="Book Name" required>

<input type="text" name="student" placeholder="Student Name" required>

<input type="date" name="due" required>

<button>Add Book</button>

</form>

<table>

<tr>
<th>ID</th>
<th>Book</th>
<th>Student</th>
<th>Due Date</th>
<th>Late Days</th>
<th>Fine</th>
<th>Action</th>
</tr>

{% for b in books %}

<tr>

<td>{{b.id}}</td>
<td>{{b.book}}</td>
<td>{{b.student}}</td>
<td>{{b.due}}</td>
<td>{{b.days}}</td>
<td>₹{{b.fine}}</td>

<td>
<a href="/delete/{{b.id}}">
<button style="background:red;">Delete</button>
</a>
</td>

</tr>

{% endfor %}

</table>

<div class="total">

<b>Total Fine Collected :</b> ₹{{total}}

</div>

</body>
</html>

"""

@app.route('/')
def home():

    data=[]
    total=0

    for i in books:

        due=datetime.strptime(i['due'],"%Y-%m-%d")
        today=datetime.now()

        days=(today-due).days

        if days<0:
            days=0

        fine=days*10

        total+=fine

        data.append({
            "id":i['id'],
            "book":i['book'],
            "student":i['student'],
            "due":i['due'],
            "days":days,
            "fine":fine
        })

    return render_template_string(page,books=data,total=total)

@app.route('/add',methods=['POST'])
def add():

    books.append({

        "id":len(books)+1,
        "book":request.form['book'],
        "student":request.form['student'],
        "due":request.form['due']

    })

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):

    global books

    books=[b for b in books if b['id']!=id]

    return redirect('/')

app.run(debug=True)