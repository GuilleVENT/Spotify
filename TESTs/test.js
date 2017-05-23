
function(){
    var data = null;

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
      if (this.readyState === 4) {
        console.log(this.responseText);
      }
    });

    xhr.open("GET", "https://api.spotify.com/v1/browse/categories/dinner/playlists?Accept=application%2Fjson&Authorization=Bearer%20BQBM3uSSHvZYYhzjJbeHwV85GDZTQXRhrIwt562jOawMYnOOECbxbWE3JFu4oEUvD-ifDgupJL4C9kRXdZUfQTxEX602j1SVov_uVAVdlO6pxphDytaK2d-Ln7JevM_SfyyiKdpiIUKMPxQAKdY-STKO8BKGpIRjRCQzUrDtW3mvnzNKjYJ2xSHqO1NVljK0aObq_g_X7HqQc-aTAIlqEGf_eyrWeVEXgVvJ_QdqoFRjZXngXpQN0aSsGf6_YASeaWIJKQ_P9FASl4v-3S-SjqsP_ulCtGn8jLEKbH4e-DzR_7vK_vYka__-0iR2ug");
    xhr.setRequestHeader("cache-control", "no-cache");
    xhr.setRequestHeader("postman-token", "e3a50461-7f2b-5253-b40c-115d9b8f0963");

    xhr.send(data);
    console.log(data);
}