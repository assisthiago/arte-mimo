from django.shortcuts import render


def index(request):
    products = [
        {
            "img": "https://images.unsplash.com/photo-1617519478819-9f578a5df62f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fHw%3D",
            "type": "boneco",
            "preheading": "Boneco",
            "name": "Curology Campaign",
        },
        {
            "img": "https://images.unsplash.com/photo-1617519478819-9f578a5df62f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fHw%3D",
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
            "img": "https://images.unsplash.com/photo-1617519478819-9f578a5df62f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fHw%3D",
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
            "img": "https://images.unsplash.com/photo-1617519478819-9f578a5df62f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fHw%3D",
            "type": "boneco",
            "preheading": "Boneco",
            "name": "Larq Earthtones Collection",
        },
        {
            "img": "https://images.unsplash.com/photo-1609580006779-13720a773a30?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "outros",
            "preheading": "Outros",
            "name": "Goby Brush Prototype",
        },
        {
            "img": "https://images.unsplash.com/photo-1609580006779-13720a773a30?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "outros",
            "preheading": "Outros",
            "name": "Larq Bottle Redesign",
        },
        {
            "img": "https://images.unsplash.com/photo-1609580006779-13720a773a30?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "type": "outros",
            "preheading": "Outros",
            "name": "Goby Packaging ",
        },
    ]

    filters = [
        {"name": "Boneco", "slug": "boneco"},
        {"name": "Pano", "slug": "pano"},
        {"name": "Decoração", "slug": "decoracao"},
        {"name": "Outros"},
    ]
    return render(
        request, "index.html", context={"products": products, "filters": filters}
    )
