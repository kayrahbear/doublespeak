'use strict';

var app = angular.module("Doublespeak", ["ngRoute", "ngMaterial"]);

//set up route paramaters
app.config(function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'partials/home.html'
    }).otherwise('/', {});
});

