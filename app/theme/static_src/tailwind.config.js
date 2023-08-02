module.exports = {
  content: [
    "../../templates/**/*.html",
    "../../templates/**/**/*.html",
    "!../../**/node_modules",
    "../../components/**/*.html",
    "../../components/**/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/typography"),
  ],
};
