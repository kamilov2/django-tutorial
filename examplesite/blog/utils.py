from blog.models import Post

def check_reaction(request,post,react):
    request.session.modified = True
    try:
        reacted_posts = request.session["react_list"]
    except:
        reacted_posts = request.session["react_list"] = []
   
    if post.id in reacted_posts:
        return "Siz bu maqolaga reaksiya bildirgansiz ! "
    else:
        if react == "like":
            post.likes += 1
            post.save()
            reacted_posts.append(post.id)
            return "Like qabul qilindi !"
        if react == "dislike":
            post.dislikes += 1
            post.save()
            reacted_posts.append(post.id)
            return "Dislike qabul qilindi !"