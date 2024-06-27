import React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import RadioInput from "../../common/RadioInput";
import { colorScheme } from "../../../constants/colorScheme";
import { PropTypes } from "prop-types";

function TrainingTeamAdditionalDetails({ formData, setFormData }) {
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
        <RadioInput
          id={"trainingTeamType"}
          label={"Select Type"}
          options={[
            "National Cooridnator",
            "State Coordinator",
            "District Coordinator",
          ]}
          name={"trainingTeamType"}
          value={formData.trainingTeamType}
          customOnChangeFun={true}
          setValue={setFormData}
        />
      </Grid>
    </Grid>
  );
}

TrainingTeamAdditionalDetails.propTypes = {
  formData: PropTypes.object.isRequired,
  setFormData: PropTypes.func.isRequired,
};
export default TrainingTeamAdditionalDetails;
