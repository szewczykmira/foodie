var path = require('path');

module.exports = {
    entry: './static/source/js/main.js',
    output: {
        filename: 'scripts/main.js',
        path: path.resolve(__dirname, 'static')
    }
};
