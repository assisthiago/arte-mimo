from django.shortcuts import render


def index(request):
    products = [
        {
            "img": "https://images.unsplash.com/photo-1552899167-d0b2887ca549?q=80&w=2815&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "boneco",
            "preheading": "Boneco",
            "name": "Curology Campaign",
        },
        {
            "img": "https://images.unsplash.com/photo-1552899167-d0b2887ca549?q=80&w=2815&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "boneco",
            "preheading": "Boneco",
            "name": "Curology Campaign",
        },
        {
            "img": "https://images.unsplash.com/photo-1613339038444-ca6b1e8eb7b4?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "pano",
            "preheading": "Pano",
            "name": "Honest Packaging",
        },
        {
            "img": "https://images.unsplash.com/photo-1552899167-d0b2887ca549?q=80&w=2815&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "boneco",
            "preheading": "Boneco",
            "name": "Larq Bright Campaign",
        },
        {
            "img": "https://images.unsplash.com/photo-1574627958512-8c12d94ec295?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "decoracao",
            "preheading": "Decoração",
            "name": "Doodle Pads",
        },
        {
            "img": "https://images.unsplash.com/photo-1552899167-d0b2887ca549?q=80&w=2815&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "boneco",
            "preheading": "Boneco",
            "name": "Larq Earthtones Collection",
        },
        {
            "img": "https://images.unsplash.com/photo-1623936180584-7a422cd8f7fb?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "outros",
            "preheading": "Outros",
            "name": "Goby Brush Prototype",
        },
        {
            "img": "https://images.unsplash.com/photo-1623936180584-7a422cd8f7fb?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "outros",
            "preheading": "Outros",
            "name": "Larq Bottle Redesign",
        },
        {
            "img": "https://images.unsplash.com/photo-1623936180584-7a422cd8f7fb?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "outros",
            "preheading": "Outros",
            "name": "Goby Packaging ",
        },
    ]

    background = "https://plus.unsplash.com/premium_photo-1681210072901-edf04c718727?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

    filters = [
        {"name": "Boneco", "slug": "boneco"},
        {"name": "Pano", "slug": "pano"},
        {"name": "Decoração", "slug": "decoracao"},
        {"name": "Outros", "slug": "outros"},
    ]
    return render(
        request,
        "index.html",
        context={"products": products, "filters": filters, "background": background},
    )
