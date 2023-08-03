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
    require("daisyui"),
  ],
  daisyui: {
    darkTheme: "dark",
    base: true,
    styled: true,
    utils: true,
    rtl: false,
    prefix: "",
    logs: true,
    themes: [
      {
        mytheme: {
          primary: "#2563eb",
          secondary: "#828df8",
          accent: "#f471b5",
          neutral: "#1d283a",
          "base-100": "#ffffff",
          info: "#3abff8",
          success: "#2bd4bd",
          warning: "#f4c152",
          error: "#fb6f84",
        },
      },
    ],
  },
};
