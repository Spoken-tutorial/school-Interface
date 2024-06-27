import React from "react";
import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import UserProfile from "./UserProfile";
import SchoolOrgProfile from "./SchoolOrgProfile";
import TrainingTeamAdditionalDetails from "./TrainingTeamAdditionalDetails";
import UserAdditionalDetails from "./UserAdditionalDetails";
import { PropTypes } from "prop-types";

function SignupForm({ formData, setFormData }) {
  //dict
  const roleComponents = {
    Organization: SchoolOrgProfile,
    School: SchoolOrgProfile,
    User: UserAdditionalDetails,
    "Training Team": TrainingTeamAdditionalDetails,
  };
  const SpecificRoleComponent = roleComponents[formData.signupRole];

  return (
    <Box sx={{ mt: "2rem" }}>
      {/* user profile details common */}
      <UserProfile formData={formData} setFormData={setFormData}></UserProfile>
      <Divider sx={{ mt: "2rem", mb: "1rem" }} />

      {/* additional details */}
      {SpecificRoleComponent && (
        <SpecificRoleComponent formData={formData} setFormData={setFormData} />
      )}
    </Box>
  );
}

SignupForm.propTypes = {
  formData: PropTypes.object.isRequired,
  setFormData: PropTypes.func.isRequired,
};

export default SignupForm;
