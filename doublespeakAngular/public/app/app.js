'use strict';

let app = angular.module("Doublespeak", ["ngRoute", "ngMaterial", "angular-jqcloud", "chart.js"]);

//set up route parameters
app.config(function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'partials/home_view.html',
        controller: 'HomeCtrl'
    }).when('/candidate:candidateId', {
        templateUrl: 'partials/candidate_view.html',
        controller: 'CandidateCtrl'
    }).otherwise('/', {});
});

