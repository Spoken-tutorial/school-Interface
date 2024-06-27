import React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import RadioInput from "../../common/RadioInput";
import ListSelectInput from "../../common/ListSelectInput";
import { colorScheme } from "../../../constants/colorScheme";
import { PropTypes } from "prop-types";

function UserAdditionalDetails({ formData, setFormData }) {
  return (
    <Grid container sx={{ mb: "1rem", mt: "2rem" }}>
      {/* user profile details */}

      <Grid item xs={12} sm={12} md={4}>
        {/* left suggestion text */}
        <Typography
          variant="subtitle1"
          gutterBottom
          sx={{ fontWeight: "bold" }}
        >
          Additional Details
        </Typography>
        <Typography
          variant="caption"
          gutterBottom
          sx={{ color: colorScheme.lightText }}
        >
          This information will be related to your profile.
        </Typography>
      </Grid>

      <Grid item xs={12} sm={12} md={8}>
        {/* right form inputs  */}
        <ListSelectInput
          id={"userOrg"}
          name={"useOrg"}
          value={formData.userOrg}
          customOnChangeFun={true}
          setValue={setFormData}
          label={"Select Organization (If Applicable)"}
          options={["a", "b", "c", "d"]}
        ></ListSelectInput>
        <ListSelectInput
          id={"userSchool"}
          name={"userOrg"}
          value={formData.userSchool}
          customOnChangeFun={true}
          setValue={setFormData}
          label={"Select School (If Applicable)"}
          options={["a", "b", "c", "d"]}
        ></ListSelectInput>
        <RadioInput
          id={"userRole"}
          label={"Select Role (Optional)"}
          options={[
            "Organization Cooridnator",
            "School Coordinator",
            "Teacher",
          ]}
          name={"userRole"}
          value={formData.userRole}
          customOnChangeFun={true}
          setValue={setFormData}
        />
      </Grid>
    </Grid>
  );
}
UserAdditionalDetails.propTypes = {
  formData: PropTypes.object.isRequired,
  setFormData: PropTypes.func.isRequired,
};
export default UserAdditionalDetails;
