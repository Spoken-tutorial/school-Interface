import React from "react";
import PropTypes from "prop-types";
import { Typography } from "@mui/material";
import { colorScheme } from "../../constants/colorScheme";

function TableDescription({ signupRole }) {
  return (
    <>
      <Typography
        variant="h6"
        sx={{
          fontWeight: "bold",
          letterSpacing: "0.03rem",
          mt: "1rem",
        }}
      >
        Pending Signups
      </Typography>
      <Typography
        variant="body1"
        sx={{
          mb: "3rem",
          letterSpacing: "0.05rem",
          color: colorScheme.lightText,
        }}
      >
        {`  Overview of all ${signupRole} signups awaiting your approval.`}
      </Typography>
    </>
  );
}

TableDescription.propTypes = {
  signupRole: PropTypes.string.isRequired,
};
export default TableDescription;
