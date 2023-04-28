module.exports = {
  apps: [
    {
      name: "fastapi",
      script: "uvicorn main:app --host 0.0.0.0 --port 8000",
      env: {
        PORT: 8000,
        ENVIRONMENT: "production",
      },
    },
  ],
};
