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


    return {getCandidates, getSingleCandidate};

});