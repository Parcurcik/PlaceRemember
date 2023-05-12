 ymaps.ready(init);

    function init() {
        var myMap = new ymaps.Map("map", {
            center: [56.838011, 60.597474],
            zoom: 10
        });

        myMap.events.add('click', function (e) {
            var coords = e.get('coords');
            console.log(coords)
            if (myMap.geoObjects.getLength() > 0) {
                myMap.geoObjects.removeAll();
            }

            document.getElementById('id_latitude').value = coords[0];
            document.getElementById('id_longitude').value = coords[1];

            var placemark = new ymaps.Placemark(coords, {}, {
                preset: 'islands#dotIcon',
                iconColor: '#ff0000'
            });

            myMap.geoObjects.add(placemark);
        });
    }