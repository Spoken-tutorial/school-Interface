import { createBrowserRouter } from "react-router-dom";

import Template from "../pages/Template";
import Home from "../components/Homepage/Home";
import Signup from "../components/Signup/Signup";
import Login from "../components/Login/Login";
const router = createBrowserRouter([
  {
    path: "/",
    element: <Template />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/signup",
        element: <Signup urlRole={null} />,
      },
      {
        path: "/signup/organization",
        element: <Signup urlRole={"Organization"} />,
      },
      {
        path: "/signup/school",
        element: <Signup urlRole={"School"} />,
      },
      {
        path: "/signup/user",
        element: <Signup urlRole={"User"} />,
      },
      {
        path: "/signup/training-team",
        element: <Signup urlRole={"Training Team"} />,
      },
      {
        path: "/login",
        element: <Login />,
      },
    ],
  },
]);

export default router;
