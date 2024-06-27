import React, { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import Box from "@mui/material/Box";
import Appbar from "../components/Navbar/Appbar";
import ResponsiveList from "../components/Navbar/ResponsiveList";
import { useNavigate, useLocation } from "react-router-dom";
import Footer from "../components/Footer/Footer";

function Template() {
  const [showNavList, setShowNavList] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const [targetId, setTargetId] = React.useState(null);

  const handleNavItemClick = (navItem, type, action) => {
    const id = navItem.toLowerCase();
    setTargetId(id);
    if (action === "scroll") {
      navigate(`/#${id}`);
    } else {
      navigate("/" + navItem);
    }
    if (type === "ResponsiveList") {
      setShowNavList(false);
    }
  };

  useEffect(() => {
    if (targetId) {
      const element = document.getElementById(targetId);
      if (element) {
        const headerOffset = 70;
        const elementPosition = element.getBoundingClientRect().top;
        const offsetPosition =
          elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: "smooth",
        });
        setTargetId(null);
      }
    }
  }, [location, targetId]);

  return (
    <>
      <Box
        sx={{
          backgroundColor: "",
          height: "100vh",
        }}
      >
        <Appbar
          showNavList={showNavList}
          setShowNavList={setShowNavList}
          handleNavItemClick={handleNavItemClick}
        />
        <Box sx={{ mt: "6rem", mb: "6rem" }}>
          {showNavList ? (
            <ResponsiveList handleNavItemClick={handleNavItemClick} />
          ) : (
            <Outlet></Outlet>
          )}
        </Box>
        <Footer />
      </Box>
    </>
  );
}

export default Template;
