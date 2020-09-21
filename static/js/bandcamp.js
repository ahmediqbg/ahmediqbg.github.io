var url = 'https://bandcamp.com/api/fancollection/1/collection_items';
// alert(url);


$.post(url,
    {"fan_id": 149531,
        "older_than_token": "1590788900:576974541:a::",
        "count": 20
    },
    function (data) {
        console.log(data);
    })

// JK, CORS prevents this from working. ;_;