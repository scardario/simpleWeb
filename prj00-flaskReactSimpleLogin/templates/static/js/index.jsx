import React from 'react'
import ReactDOM from 'react-dom'

// import routes from "./routes"

// Renderiza el contenido de routes.js
// ReactDOM.render(routes, document.getElementById("content"))

console.log("iniciando....")

export default class reactTest extends Component {
	render() {
		return (<h1>reactTest - funcionando</h1>)
	}
}

console.log("Hi, I'm in index.jsx")

ReactDOM.render(reactTest, document.getElementById("content"))