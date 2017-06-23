'use strict';

var app = angular.module("Doublespeak", ["ngRoute", "ngMaterial", 'angular-d3-word-cloud']);

//set up route paramaters
app.config(function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'partials/home_view.html',
        controller: 'HomeCtrl'
    }).when('/candidate:candidateId', {
        templateUrl: 'partials/candidate_view.html',
        controller: 'CandidateCtrl'
    }).otherwise('/', {});
});

