// vue.config.js

module.exports = {
  outputDir: "../be-server/static/",
  devServer: {
    proxy: {
      "/": {
        target: "http://localhost:5000",
        secure: false,
        changeOrigin: true,
      },
    },
  },
};
