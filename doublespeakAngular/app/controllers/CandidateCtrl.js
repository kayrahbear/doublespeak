"use strict";

app.controller('CandidateCtrl', function ($scope, $routeParams, $q, filterFilter, DjangoFactory) {

    $scope.mostWords = true;
    $scope.simpleSentimant = false;
    $scope.personalityTone = false;
    $scope.emotionalTone = false;


    let promises = {
        sentiment: DjangoFactory.getCandidateSentiment($routeParams.candidateId),
        emotion: DjangoFactory.getCandidateEmotion($routeParams.candidateId),
        personality: DjangoFactory.getCandidatePersonality($routeParams.candidateId)
    };

    //get single presidential candidates from Django API
    DjangoFactory.getSingleCandidate($routeParams.candidateId)
        .then(function successCallback(response) {
            $scope.chosenCandidate = response;
            let words = $scope.chosenCandidate.most_used_words;
            $scope.frequentWords = words.split(", ");
            makeCloud($scope.frequentWords);
        });

    $q.all(promises).then((values) => {
        $scope.candidateSimpleSetiment = values.sentiment[0];

        $scope.candidateEmotion = values.emotion[0];

        $scope.candidatePersonality = values.personality[0];


    });

    $scope.wordsView = function () {
        $scope.mostWords = true;
        $scope.emotionalTone = false;
        $scope.personalityTone = false;
        $scope.simpleSentimant = false;
    };

    $scope.setDoughtnutData = function (candidateSimpleSetiment) {
        $scope.labels = ["Positive", "Negative"];
        $scope.data = [candidateSimpleSetiment.positive_sentiment, candidateSimpleSetiment.negative_sentiment];
        $scope.mostWords = false;
        $scope.emotionalTone = false;
        $scope.personalityTone = false;
        $scope.simpleSentimant = true;

    };

    $scope.setEmotionalBar = function (candidateEmotion) {
        $scope.labels = ["Anger", "Disgust", "Fear", "Joy", "Sadness"];

        $scope.data = [];
        let results = [candidateEmotion.anger_tone, candidateEmotion.disgust_tone, candidateEmotion
            .fear_tone, candidateEmotion.joy_tone, candidateEmotion.sadness_tone];

        results.forEach(function (result) {
            parseInt(result);
            $scope.data.push(result);
            console.log($scope.data);
        });
        $scope.mostWords = false;
        $scope.emotionalTone = true;
        $scope.personalityTone = false;
        $scope.simpleSentimant = false;

    };

    $scope.setPersonalityBar = function (candidatePersonality) {
        $scope.labels = ["Open", "Conscientious", "Extroverted", "Agreeable", "Emotional Range"];

        $scope.data = [];
        let results = [candidatePersonality.openness_tone, candidatePersonality.conscientiousness_tone, candidatePersonality
            .extraversion_tone, candidatePersonality.agreeableness_tone, candidatePersonality.emotional_range_tone];

        results.forEach(function (result) {
            parseInt(result);
            $scope.data.push(result);
            console.log($scope.data);
        });
        $scope.mostWords = false;
        $scope.emotionalTone = false;
        $scope.personalityTone = true;
        $scope.simpleSentimant = false;

    };

    function makeCloud(frequentWords) {

        $scope.words = [
            {text: $scope.frequentWords[0], weight: 13},
            {text: $scope.frequentWords[1], weight: 10.5},
            {text: $scope.frequentWords[2], weight: 9.4},
            {text: $scope.frequentWords[3], weight: 8},
            {text: $scope.frequentWords[4], weight: 6.2},
            {text: $scope.frequentWords[5], weight: 5},
            {text: $scope.frequentWords[6], weight: 5},
            {text: $scope.frequentWords[7], weight: 5},
            {text: $scope.frequentWords[8], weight: 5},
            {text: $scope.frequentWords[9], weight: 4},
            {text: $scope.frequentWords[10], weight: 4},
            {text: $scope.frequentWords[11], weight: 3},
            {text: $scope.frequentWords[12], weight: 3},
            {text: $scope.frequentWords[13], weight: 3},
            {text: $scope.frequentWords[14], weight: 3},
            {text: $scope.frequentWords[15], weight: 3},
            {text: $scope.frequentWords[16], weight: 3},
            {text: $scope.frequentWords[17], weight: 3},
            {text: $scope.frequentWords[18], weight: 2},
            {text: $scope.frequentWords[19], weight: 2}
        ];

        $scope.colors = ["#4db6ac", "#26a69a", "#009688", "#00897b", "#00796b", "#00695c", "#004d40"];
        $scope.update = function () {
            $scope.words.splice(-5);
        };

    }


});



