const webpack = require("webpack")
const resolve = require("path").resolve

const config = {
	// devtool: "eval-source-map",
	entry: __dirname + "/js/index.jsx",
	output: {
		path: resolve("../public"),
		filename: "bundle.js",
		publicPath: resolve("../public")
	},
	resolve: {
		extensions: ['.js', '.jsx'/* , '.css' */]
	},
	module: {
		rules: [
			{
				test: /\.jsx?/,
				// Se supone que recomiendan usar include en lugar de exclude
				exclude: /node_modules/,
				loader: "babel-loader"
			}/* ,
			{
				test: /\.css$/,
				use: [
					{
						loader: "style-loader"
					},
					{
						loader: "css-loader",
						options: {
							modules: true
						}
					}
				]
			} */
		]
	}
}

module.exports = config