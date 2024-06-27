import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import IconButton from "@mui/material/IconButton";
import FacebookRoundedIcon from "@mui/icons-material/FacebookRounded";
import YouTubeIcon from "@mui/icons-material/YouTube";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import { Link } from "react-router-dom";
import { colorScheme } from "../../constants/colorScheme";
import { footerSocialIcons } from "../../constants/Data/footer";

function CopyRightAndSocialMedia() {
  const iconMap = {
    Facebook: <FacebookRoundedIcon />,
    Youtube: <YouTubeIcon />,
    LinkedIn: <LinkedInIcon />,
  };
  return (
    <Box sx={{ width: "100%", display: "flex" }}>
      <Grid
        container
        direction="row"
        justifyContent="space-between"
        alignItems="center"
      >
        <Grid item xs={12} sm={12} md={7} lg={7}>
          <Typography
            variant="caption"
            display="block"
            gutterBottom
            sx={{
              p: "0.2rem",
              color: colorScheme.lightText,
              ml: "1rem",
              mt: "0.3rem",
              textAlign: "center",
            }}
          >
            Spoken Tutorial by{" "}
            <Link
              to={"https://www.iitb.ac.in/"}
              target="_blank"
              style={{
                textDecoration: "none",
                color: colorScheme.lightText,
              }}
            >
              IIT Bombay
            </Link>{" "}
            is licensed under a Creative{" "}
            <Link
              to={"https://www.iitb.ac.in/"}
              target="_blank"
              style={{
                textDecoration: "none",
                color: colorScheme.lightText,
              }}
            >
              Commons Attribution-ShareAlike 4.0 International License{" "}
            </Link>
            , except where stated otherwise Based on a work at
            <Link
              to={"https://www.iitb.ac.in/"}
              target="_blank"
              style={{
                textDecoration: "none",
                color: colorScheme.lightText,
              }}
            >
              {" "}
              https://spoken-tutorial.org
            </Link>
            . Permissions beyond the scope of this license may be available at
            <Link
              to={"https://www.iitb.ac.in/"}
              target="_blank"
              style={{
                textDecoration: "none",
                color: colorScheme.lightText,
              }}
            >
              https://spoken-tutorial.org
            </Link>
            .
          </Typography>
        </Grid>
        <Grid
          item
          xs={12}
          sm={12}
          md={5}
          lg={5}
          sx={{ display: "flex", justifyContent: "center" }}
        >
          {footerSocialIcons.map((data) => (
            <Link to={data.url} reloadDocument target="_blank" key={data.title}>
              <IconButton aria-label="delete">
                <Box
                  sx={{
                    color: "#9396A3",
                    width: "1.3rem",
                    "&:hover": {
                      color: colorScheme.primaryOrange,
                    },
                  }}
                >
                  {iconMap[data.title] || "#"}
                </Box>
              </IconButton>
            </Link>
          ))}
        </Grid>
      </Grid>
    </Box>
  );
}
export default CopyRightAndSocialMedia;
