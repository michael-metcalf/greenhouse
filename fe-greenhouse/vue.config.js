// vue.config.js

module.exports = {
  pwa: {
    name: "MoneySprouts",
    workboxPluginMode: "GenerateSW",
    themeColor: "#6FB02A"
  },
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
