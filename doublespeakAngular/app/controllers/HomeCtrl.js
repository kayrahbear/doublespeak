"use strict";

app.controller('HomeCtrl', function ($scope, $routeParams, filterFilter, DjangoFactory) {

    $scope.candidates = [];

    //get all presidential candidates from Django API
    DjangoFactory.getCandidates()
        .then((candidateResponse) => {
            $scope.candidates = candidateResponse.data;
        });
});