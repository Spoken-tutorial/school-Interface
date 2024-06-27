import React from "react";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import SchoolIcon from "@mui/icons-material/School";
import PersonIcon from "@mui/icons-material/Person";
import GroupsIcon from "@mui/icons-material/Groups";
import CorporateFareIcon from "@mui/icons-material/CorporateFare";
import { colorScheme } from "../../../constants/colorScheme";
import { PropTypes } from "prop-types";

function RoleCard({ title, description }) {
  const iconMap = {
    Organization: (
      <CorporateFareIcon sx={{ color: colorScheme.primaryOrange }} />
    ),
    School: <SchoolIcon sx={{ color: colorScheme.primaryOrange }} />,
    User: <PersonIcon sx={{ color: colorScheme.primaryOrange }} />,
    "Training Team": <GroupsIcon sx={{ color: colorScheme.primaryOrange }} />,
  };
  return (
    <>
      <Box sx={{ width: "100%", height: "100%" }}>
        <Grid
          container
          direction="column"
          justifyContent="flex-start"
          rowSpacing={3}
          alignItems="flex-start"
        >
          {/* role icon */}{" "}
          <Grid item>
            <Box
              sx={{
                height: "3rem",
                width: "3rem",
                backgroundColor: colorScheme.primaryOrangeLight,
                borderRadius: "0.15rem",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              {iconMap[title]}
            </Box>
          </Grid>
          {/* role title */}
          <Grid item>
            <Typography variant="h6" gutterBottom sx={{ fontWeight: "bold" }}>
              {title}
            </Typography>
          </Grid>
          {/* role description */}
          <Grid item>
            <Typography
              variant="subtitle1"
              display="block"
              gutterBottom
              sx={{
                mt: "-1rem",
                color: colorScheme.lightText,
                textAlign: "left",
              }}
            >
              {description}
            </Typography>
          </Grid>
        </Grid>
      </Box>
    </>
  );
}

RoleCard.propTypes = {
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
};

export default RoleCard;
