import React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";
import { NavLink } from "react-router-dom";
import { navItems } from "../../constants/Data/navbar";
import { colorScheme } from "../../constants/colorScheme";
import { PropTypes } from "prop-types";

function ResponsiveAppBar({ showNavList, setShowNavList, handleNavItemClick }) {
  return (
    <AppBar
      position="fixed"
      sx={{
        mb: "2rem",
        backgroundColor: colorScheme.secondaryGrey,
      }}
    >
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          {/* company logo */}
          <Avatar
            sx={{
              backgroundColor: "#ffffff",
              ml: "0.5rem",
              mr: "0.5rem",
              display: { xs: "none", sm: "none", md: "inline" },
            }}
            alt="IIT Bombay"
            src="https://jrs.spoken-tutorial.org/static/images/st-logo.png"
          />
          {/* company title */}
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: "none", md: "flex" },
              fontFamily: "monospace",
              fontWeight: 700,
              color: "inherit",
              textDecoration: "none",
            }}
          >
            Spoken Tutorial
          </Typography>

          {/* responsive small screen menu item list */}
          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
            {/*Small screen nav items list button*/}
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={() => {
                setShowNavList(!showNavList);
              }}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
          </Box>
          {/* small screen app bar */}

          <Avatar
            sx={{
              backgroundColor: "#ffffff",
              mr: "0.5rem",
              width: { xs: "1.5rem", sm: "1.8rem" },
              height: { xs: "1.5rem", sm: "1.8rem" },
              display: { xs: "flex", md: "none" },
            }}
            alt="IIT Bombay"
            src="https://jrs.spoken-tutorial.org/static/images/st-logo.png"
          />
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: "flex", md: "none" },
              flexGrow: 1,
              fontFamily: "monospace",
              fontWeight: 700,
              color: "inherit",
              fontSize: "1rem",
              textDecoration: "none",
            }}
          >
            Spoken Tutorial
          </Typography>

          {/* lg screen nav items */}
          <Box
            sx={{
              ml: "3rem",
              flexGrow: 1,
              display: { xs: "none", md: "flex" },
            }}
          >
            {navItems.map((navItem) => (
              <Typography
                key={navItem.title + "lg"}
                sx={{
                  color: "white",
                  display: "block",
                  mr: "3rem",
                  cursor: "pointer",
                  "&:hover": { color: colorScheme.primaryOrange },
                }}
                onClick={() => handleNavItemClick(navItem.title, "", "scroll")}
              >
                {navItem.title}
              </Typography>
            ))}
          </Box>
          {/* right side action buttons */}
          <Box
            sx={{
              flexGrow: 0,
              display: { xs: "none", sm: "none", md: "inline" },
            }}
          >
            <NavLink to="/login">
              {({ isActive }) => (
                <Typography
                  variant="h6"
                  gutterBottom
                  sx={{
                    textDecoration: "none",
                    color: isActive ? colorScheme.primaryOrange : "#ffffff",
                    fontSize: "1rem",
                    mr: "1rem",
                    "&:hover": { color: colorScheme.primaryOrange },
                    cursor: "pointer",
                  }}
                >
                  Login
                </Typography>
              )}
            </NavLink>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}

ResponsiveAppBar.propTypes = {
  showNavList: PropTypes.bool.isRequired,
  setShowNavList: PropTypes.func.isRequired,
  handleNavItemClick: PropTypes.func.isRequired,
};
export default ResponsiveAppBar;
