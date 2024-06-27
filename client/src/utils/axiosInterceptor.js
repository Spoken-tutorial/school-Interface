import axios from "axios";

const axiosPrivate = axios.create({
  baseURL: "",
});

export { axiosPrivate };

// request interceptor
axiosPrivate.interceptors.request.use(
  function (config) {
    // This function is called before the request is sent
    // You can modify the request configuration here
    console.log("From interceptor before req is being sent");
    return config;
  },
  function (error) {
    // This function is called if there is an error during the request setup
    return Promise.reject(error);
  }
);

// response interceptor
axiosPrivate.interceptors.response.use(
  function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    console.log("From interceptor just after response is received");
    return response;
  },
  function (error) {
    if (error.response) {
      // Server responded with a status code outside the range of 2xx
      console.error("Response error:", error.response);
    } else if (error.request) {
      // Request was made but no response was received
      console.error("No response received:", error.request);
    } else {
      // Something happened in setting up the request that triggered an error
      console.error("Request setup error:", error.message);
    }
  }
);
