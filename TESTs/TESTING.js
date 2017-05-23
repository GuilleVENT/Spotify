related();

function genURL(){
    var url1 = "https://api.spotify.com/v1/artists/52la6ts4higk3sqyFC3aTg/related-artists";
    return url1;
}
function related(){
    var data = null;

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
     if (this.readyState === 4) {
        console.log(this.responseText);
      }
    });
    var url1 = genURL();

    xhr.open("GET", url1);
    xhr.setRequestHeader("accept", "application/json");
    xhr.setRequestHeader("authorization", "Bearer BQAOxgMmKuOr30gb-vKb8aP5c1EJ-SyLSM6ZSeWTbmPfn7-28z9nR9IogP9lCrUCZuSaEiL5P3OzMZo3xDrvXQOruMWgCkVSFAwo9TMATOe85nuP14_fKYe9HijicYNDLNg71fTQOFCwh4sVH0rI6gFT7hnUS2tLaMY5hokP91mLy9CkelAZtGiVl2Pk_9sPnqBN_7n7BVvr9ugiOgh9YpNycG6AK_0NKAfklUaAIUWNtXT1p0qVxqDwRgkNUPU5JAGDwvvzNyWOoU_7CHqHVMY3MlVdr2QC21iMqMw63GBQvLUvfz25UCv8wgCRUg");
    xhr.setRequestHeader("cache-control", "no-cache");
    xhr.setRequestHeader("postman-token", "9bd22066-2e90-88f3-dee3-8518e256f1d0");

    xhr.send(data);
    return data;
}

