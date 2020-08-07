import requests

# Base discord assets url
baseurl = "https://discordapp.com/assets/"

# Image URLs
img_urls = [
    "4358ad1fb423b346324516453750f569.svg",
    "33fedf082addb91d88abc272b4b18daa.svg",
    "6c73f47daf179ffade99f501bfc5101b.svg",
    "64ae1208b6aefc0a0c3681e6be36f0ff.svg",
    "48cf0556d93901c8cb16317be2436523.svg",
    "9fdc63ef8a3cc1617c7586286c34e4f1.svg",
    "26a2dc8c9d70955a988cb377eec84c22.svg",
    "88d4f11bee9ea34fee59973b33353da0.svg",
    "3245b2cd85b787b195ea8f6e10ef5790.svg",
    "23e59d799436a73c024819f84ea0b627.svg",
    "386884eecd36164487505ddfbac35a9d.svg",
    "f61b8981e92feead854f52e5a1ba14f0.svg",
    "9286332d6e947c91fa91569efce431b0.svg",
    "fbb6f1e160280f0e9aeb5d7c452eefe1.svg",
    "b4b741bef6c3de9b29e2e0653e294620.svg",
    "93f5a393e22796a850931483166d7cb9.svg",
    "4c380650960c2b1e1584115d5e9ad63b.svg",
    "438dd7ecbffcf21b6cbf2773ade51a04.svg",
    "7a5f78de816fcecbbd1d5d6e635cc7dd.svg",
    "5a24b20b84fb3eafc138916729386e76.svg",
    "f31d590e1f3629cd0b614330f4a8ee2a.svg",
    "9ba64f1fa91ccde0eba506c1c33f3d1a.svg",
    "45cd06af582dcd3c6b79370b4e3630de.svg"
]

# Download all the SVG files using requests
for i in img_urls:
    r = requests.get(baseurl + i)
    # Put them in the svgs folder and save them
    with open("svgs/" + i.replace("https://discordapp.com/assets/", ""), 'wb') as f:
        f.write(r.content)
