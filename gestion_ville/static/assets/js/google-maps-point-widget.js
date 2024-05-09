function initMap() {
    var sokode = {lat: 8.98333, lng: 1.13333}; // coordonnées de Sokodé
    var map = new google.maps.Map(document.getElementById('map'), {
        center: sokode, // centrer la carte sur Sokodé
        zoom: 8
    });

    // Ecouteur d'événement pour la sélection de la localisation
    google.maps.event.addListener(map, 'click', function(event) {
        // Récupérer les coordonnées géographiques de l'endroit sélectionné
        var lat = event.latLng.lat();
        var lng = event.latLng.lng();

        // Mettre à jour la valeur du champ "location" avec les coordonnées géographiques
        document.getElementById("id_location").value = lat + ',' + lng;
    });
}
