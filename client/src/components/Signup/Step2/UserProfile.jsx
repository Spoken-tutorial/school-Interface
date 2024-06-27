import React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import TextInput from "../../common/TextInput";
import { colorScheme } from "../../../constants/colorScheme";
import { PropTypes } from "prop-types";

function UserProfile({ formData, setFormData }) {
  return (
    <>
      <Grid container sx={{ mb: "1rem" }}>
        {/* user profile details */}

        <Grid item xs={12} sm={12} md={4}>
          {/* left suggestion text */}
          <Typography
            variant="subtitle1"
            gutterBottom
            sx={{ fontWeight: "bold" }}
          >
            Profile
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
          <TextInput
            id={"firstName"}
            label={"First Name"}
            value={formData.firstName}
            customOnChangeFun={true}
            setValue={setFormData}
            requiredToFill={true}
          ></TextInput>
          <TextInput
            id={"lastName"}
            label={"Last Name"}
            customOnChangeFun={true}
            value={formData.lastName}
            requiredToFill={true}
            setValue={setFormData}
          ></TextInput>
          <TextInput
            id={"email"}
            label={"Email"}
            customOnChangeFun={true}
            value={formData.email}
            requiredToFill={true}
            setValue={setFormData}
            type={"email"}
          ></TextInput>
          <TextInput
            id={"username"}
            label={"Username"}
            customOnChangeFun={true}
            value={formData.username}
            setValue={setFormData}
          ></TextInput>
          <TextInput
            id={"password"}
            label={"Password"}
            customOnChangeFun={true}
            value={formData.password}
            setValue={setFormData}
            type={"password"}
          ></TextInput>
          <TextInput
            id={"confirmPassword"}
            label={"Confirm Password"}
            customOnChangeFun={true}
            value={formData.confirmPassword}
            setValue={setFormData}
            type={"password"}
          ></TextInput>
          <TextInput
            id={"phone"}
            label={"Phone"}
            customOnChangeFun={true}
            value={formData.phone}
            requiredToFill={true}
            type={"number"}
            setValue={setFormData}
          ></TextInput>
          {formData.signupRole !== "Training Team" ? (
            <TextInput
              id={"dob"}
              value={formData.dob}
              customOnChangeFun={true}
              type={"date"}
              alternateLabelRequired={true}
              alternateLabel={"DOB"}
              setValue={setFormData}
            ></TextInput>
          ) : null}
        </Grid>
      </Grid>
    </>
  );
}

UserProfile.propTypes = {
  formData: PropTypes.object.isRequired,
  setFormData: PropTypes.func.isRequired,
};

export default UserProfile;
