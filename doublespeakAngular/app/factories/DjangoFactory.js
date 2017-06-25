"use strict";

app.factory("DjangoFactory", function ($q, $http) {


    let getCandidates = () => {
        return $q(function (resolve, reject) {
            $http.get(`http://localhost:8000/candidate`)
                .then(function (candidateData) {
                    resolve(candidateData);
                })
                .catch(function (error) {
                    reject(error);
                });
        });
    };

    let getSingleCandidate = (candidateId) => {
        return $q(function (resolve, reject) {
            $http.get(`http://localhost:8000/candidate/${candidateId}`)
                .then(function (candidate) {
                    resolve(candidate.data);
                })
                .catch(function (error) {
                    reject(error);
                });
        });
    };

    let getCandidateSentiment = (candidateId) => {
        return $q(function (resolve, reject) {
            $http.get(`http://localhost:8000/getsentimentbyid/${candidateId}`)
                .then(function (sentiment) {
                    resolve(sentiment.data);
                })
                .catch(function (error) {
                    reject(error);
                });
        });
    };

    let getCandidateEmotion = (candidateId) => {
        return $q(function (resolve, reject) {
            $http.get(`http://localhost:8000/getemotionbyid/${candidateId}`)
                .then(function (emotion) {
                    resolve(emotion.data);
                })
                .catch(function (error) {
                    reject(error);
                });
        });
    };

    let getCandidatePersonality = (candidateId) => {
        return $q(function (resolve, reject) {
            $http.get(`http://localhost:8000/getpersonalitybyid/${candidateId}`)
                .then(function (personality) {
                    resolve(personality.data);
                })
                .catch(function (error) {
                    reject(error);
                });
        });
    };


    return {getCandidates, getSingleCandidate, getCandidateSentiment, getCandidatePersonality, getCandidateEmotion};

});