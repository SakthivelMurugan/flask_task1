from flask import request,redirect,render_template,Flask

app=Flask("__name__")

@app.route("/home")
def msg():
    return "hellow friends"

subscribers_list=[]
post=[]
products=[]
@app.route("/append",methods=["post","get"])
def store():
    if request.form.get("subscribers_list")!=None:
        subscribers_list.append(request.form.get("subscribers_list"))
        post.append(request.form.get("post"))
        products.append(request.form.get("products"))
        print(subscribers_list)
        print(post)
        print(products)
    return render_template("index.html",a=subscribers_list,b=post,c=products)

if __name__=="__main__":
    app.run(debug=True)n 