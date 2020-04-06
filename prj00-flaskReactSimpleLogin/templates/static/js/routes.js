// el output de webpack está en public/bundle.js, seguramente esto se incluye en el paquete de webpack
import React from "react"
import { HashRouter, Route } from "react-router-dom"
import { createBrowserHistory } from "history"

// import Home from "./components/Home"

// Esta variable se crea con la librería history, al parecer es un remplazo de hashHistory
const historial = createBrowserHistory()

// Es llamado desde index.jsx, este código es renderizado desde allí
export default (
	// el tutorial tenía <HashRouter history={hashHistory}>, pero hashHistory no parecía estar en la librería
	/* {<HashRouter history={historial}>
		<div>
			<Route path='/' component={Home} />
		</div>
	</HashRouter>} */
	<h1>routes - funcionando</h1>
)