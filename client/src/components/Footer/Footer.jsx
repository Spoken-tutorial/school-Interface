import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Divider from "@mui/material/Divider";
import Avatar from "@mui/material/Avatar";
import FooterMenu from "./FooterMenu";
import CopyRightAndSocialMedia from "./CopyRightAndSocialMedia";
import ContactDetails from "./ContactDetails";
import { Link } from "react-router-dom";
import { colorScheme } from "../../constants/colorScheme";

function Footer() {
  return (
    <footer>
      <Box
        sx={{
          backgroundColor: colorScheme.secondaryGrey,
          width: "100%",
          mt: "2rem",
        }}
      >
        <Grid container spacing={2}>
          {/* Title & Logo */}
          <Grid item xs={12} md={3}>
            <Link to="https://www.iitb.ac.in/" reloadDocument target="_blank">
              <Avatar
                sx={{
                  width: "4rem",
                  height: "4rem",
                  textAlign: "center",
                  margin: "auto",
                  marginTop: "0.5rem",
                }}
                alt="IIT Bombay"
                src="https://jrs.spoken-tutorial.org/static/images/iitb-logo.png"
              />
            </Link>
            <Link
              to="https://www.iitb.ac.in/"
              reloadDocument
              target="_blank"
              style={{ textDecoration: "none" }}
            >
              <Typography
                variant="overline"
                display="block"
                gutterBottom
                sx={{ color: "#ffffff", textAlign: "center" }}
              >
                Developed at IIT Bombay
              </Typography>
            </Link>
            <Typography
              variant="h6"
              gutterBottom
              sx={{
                color: "#ffffff",
                fontWeight: "bold",
                textAlign: "center",
                marginTop: "-0.3rem",
              }}
            >
              Spoken Tutorial
            </Typography>
          </Grid>

          {/* Footer Menu List */}
          <Grid item xs={4} md={2}>
            <FooterMenu
              key={"Training"}
              menuTitle={"Training"}
              menuItems={[
                { title: "Software Training", url: "#" },
                { title: "Training Dashboard", url: "#" },
                { title: "Creation Dashboard", url: "#" },
              ]}
            ></FooterMenu>
          </Grid>
          <Grid item xs={4} md={2}>
            <FooterMenu
              key={"About"}
              menuTitle={"About"}
              menuItems={[
                { title: "News", url: "#" },
                { title: "About Us", url: "#" },
                { title: "Stats", url: "#" },
              ]}
            ></FooterMenu>
          </Grid>

          <Grid item xs={12} md={4}>
            <ContactDetails />
          </Grid>
        </Grid>

        {/* Bottom end copyright & social media */}
        <Divider
          sx={{
            backgroundColor: "#ffffff",
            mb: "0.1rem",
            mt: "0.1rem",
          }}
        ></Divider>
        <CopyRightAndSocialMedia />
      </Box>
    </footer>
  );
}
export default Footer;
