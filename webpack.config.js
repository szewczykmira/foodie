var path = require('path');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    entry: ['./static/source/js/main.js', './static/source/less/main.less'],
    output: {
        filename: './static/dist/scripts/main.js',
    },
    module: {
      rules: [

        {
        test: /\.less$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            {
              loader: 'css-loader',
              options: {
                sourceMap: true
              }
            },
            {
              loader: 'less-loader'
            }
          ]
        })
      },
      ]
    },
    plugins: [
      new ExtractTextPlugin({ // define where to save the file
        filename: 'static/dist/css/[name].bundle.css',
        allChunks: true,
      }),
    ]
  };
