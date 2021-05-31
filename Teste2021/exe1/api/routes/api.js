var express = require('express');
var router = express.Router();

var graphDB = require('../utils/graphdb')


router.get('/emd', function(req, res, next) {
    if(req.query.res == "OK"){
        q = `select ?s where { ?s rdf:type :EMD ; :Resultado "true"^^xsd:boolean .}`
        graphDB.fetch(q)
        .then(resp => {
            res.jsonp(resp.data)
        })
        .catch(error => {
            console.log('Erro /emd?res=OK \n'+ error)
        })
    } else {
        q = `
        select ?s ?r ?data ?pNome ?uNome where { 
            ?s rdf:type :EMD ; 
               :feitoPor ?a ; 
               :Resultado ?r ; 
               :Data ?data . 
            ?a rdf:type :Atleta ;
               :Primeiro ?pNome ;
               :Ultimo ?uNome .}`
        graphDB.fetch(q)
        .then(resp => {
            res.jsonp(resp.data)
        })
        .catch(error => {
            console.log('Erro /emd/ \n'+ error)
        })
    }
});

router.get('/emd/:id', function(req, res, next) {
    q = `
    select ?r ?data ?index ?pNome ?uNome where { 
        :${req.params.id} rdf:type :EMD ; 
           :feitoPor ?a ; 
           :Resultado ?r ; 
           :Data ?data ;
           :Index ?index. 
        ?a rdf:type :Atleta ;
           :Primeiro ?pNome ;
           :Ultimo ?uNome .}`
    graphDB.fetch(q)
    .then(resp => {
        res.jsonp(resp.data)
    })
    .catch(error => {
        console.log(`Erro /emd/${req.params.id} \n`+ error)
    })
}
);

router.get('/modalidades ', function(req, res, next) {
    q = `select distinct ?s where { ?s rdf:type :Modalidade .}`
    graphDB.fetch(q)
    .then(resp => {
        res.jsonp(resp.data)
    })
    .catch(error => {
        console.log('Erro /modalidades \n'+ error)
    })
}
);
router.get('/modalidades/:id', function(req, res, next) {
    q = `
    select ?s  where {
        ?s rdf:type :EMD ; 
           :feitoPor ?a .
        ?a rdf:type :Atleta ;
           :temModalidade :${req.params.id} .
    }`
    graphDB.fetch(q)
    .then(resp => {
        res.jsonp(resp.data)
    })
    .catch(error => {
        console.log(`Erro /modalidades/${req.params.id} \n`+ error)
    })
}
);
router.get('/atletas', function(req, res, next) {

    if(req.query.gen){
        q = `
        select ?s ?pNome ?uNome where {
            ?s rdf:type :Atleta ; 
            :Genero "${req.query.gen}" ; 
            :Primeiro ?pNome ;
            :Ultimo ?uNome .
        } order by (?pNome && ?uNome)`
        graphDB.fetch(q)
        .then(resp => {
            res.jsonp(resp.data)
        })
        .catch(error => {
            console.log(`Erro /atletas?gen=${req.query.gen} \n`+ error)
        })
    } else if(req.query.clube){
        q = `
        select ?a ?pNome ?uNome where { 
            ?a rdf:type :Atleta ;
               :temClube :ABCbraga ;
               :Primeiro ?pNome ;
               :Ultimo ?uNome .
        } order by (?pNome && ?uNome)`
        graphDB.fetch(q)
        .then(resp => {
            res.jsonp(resp.data)
        })
        .catch(error => {
            console.log(`Erro /atletas?gen=${req.query.clube} \n`+ error)
        })
    }
}
);



module.exports = router;
