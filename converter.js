// Import sharp
const sharp = require("sharp");

// Define the files
const files = [
    "4358ad1fb423b346324516453750f569",
    "33fedf082addb91d88abc272b4b18daa",
    "6c73f47daf179ffade99f501bfc5101b",
    "64ae1208b6aefc0a0c3681e6be36f0ff",
    "48cf0556d93901c8cb16317be2436523",
    "9fdc63ef8a3cc1617c7586286c34e4f1",
    "26a2dc8c9d70955a988cb377eec84c22",
    "88d4f11bee9ea34fee59973b33353da0",
    "3245b2cd85b787b195ea8f6e10ef5790",
    "23e59d799436a73c024819f84ea0b627",
    "386884eecd36164487505ddfbac35a9d",
    "f61b8981e92feead854f52e5a1ba14f0",
    "9286332d6e947c91fa91569efce431b0",
    "fbb6f1e160280f0e9aeb5d7c452eefe1",
    "b4b741bef6c3de9b29e2e0653e294620",
    "93f5a393e22796a850931483166d7cb9",
    "4c380650960c2b1e1584115d5e9ad63b",
    "438dd7ecbffcf21b6cbf2773ade51a04",
    "7a5f78de816fcecbbd1d5d6e635cc7dd",
    "5a24b20b84fb3eafc138916729386e76",
    "f31d590e1f3629cd0b614330f4a8ee2a",
    "9ba64f1fa91ccde0eba506c1c33f3d1a",
    "45cd06af582dcd3c6b79370b4e3630de"
]

// Loop through each file
files.forEach(filename => {
    // Go into svgs folder, get the current file and convert it to png
    sharp("svgs/" + filename + ".svg")
    .png()
    // Save the png in the pngs folder
    .toFile("pngs/" + filename + ".png")
    .then(function(info) {
        console.log(info);
    })
    .catch(function(err) {
        console.log(err);
    });
});