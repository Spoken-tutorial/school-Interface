import React from "react";
import Typography from "@mui/material/Typography";
import { Link } from "react-router-dom";
import { colorScheme } from "../../constants/colorScheme";
import { PropTypes } from "prop-types";

function FooterMenu({ menuTitle, menuItems }) {
  return (
    <>
      <Typography
        variant="subtitle2"
        gutterBottom
        sx={{
          color: "#ffffff",
          fontWeight: "bold",
          mt: "0.5rem",
          ml: "0.4rem",
          textAlign: {
            xs: "center",
            sm: "center",
            md: "left",
            lg: "left",
            xl: "left",
          },
        }}
      >
        {menuTitle}
      </Typography>
      {menuItems.map((obj) => (
        <Link to={obj.url} style={{ textDecoration: "none" }} key={obj.title}>
          <Typography
            variant="caption"
            display="block"
            key={obj.title}
            gutterBottom
            sx={{
              color: "#ffffff",
              ml: "0.4rem",
              fontSize: "0.875rem",
              mb: "0.5rem",
              "&:hover": { color: colorScheme.primaryOrange },
              textAlign: {
                xs: "center",
                sm: "center",
                md: "left",
                lg: "left",
                xl: "left",
              },
            }}
          >
            {obj.title}
          </Typography>
        </Link>
      ))}
    </>
  );
}

FooterMenu.propTypes = {
  menuTitle: PropTypes.string.isRequired,
  menuItems: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      url: PropTypes.string.isRequired,
    })
  ),
};

export default FooterMenu;
