"use strict";

app.controller('CandidateCtrl', function ($scope, $routeParams, DjangoFactory) {

    $scope.chosenCandidate = {};
    $scope.frequentWords = [];

    //get all presidential candidates from Django API
    DjangoFactory.getSingleCandidate($routeParams.candidateId)
        .then(function successCallback(response) {
            $scope.chosenCandidate = response;
            let words = $scope.chosenCandidate.most_used_words;
            $scope.frequentWords = words.split(", ")
        });




});