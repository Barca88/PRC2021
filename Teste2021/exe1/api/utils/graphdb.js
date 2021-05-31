const axios = require('axios')

module.exports.fetch = function fetchOntobud(q){

    let prefixes = `PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
`
    let query = encodeURI(prefixes + q)

        
        url = 'http://localhost:7200/repositories/EMD?query=' + query
        console.log(url)
      return axios.get(url,{Headers: {
          'Content-type': 'application/sparql-results+json;charset=UTF-8'
      }})
}