import React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import TextInput from "../../common/TextInput";
import { colorScheme } from "../../../constants/colorScheme";
import ListSelectInput from "../../common/ListSelectInput";
import { PropTypes } from "prop-types";

function SchoolOrgProfile({ formData, setFormData }) {
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
        <TextInput
          id={"orgName"}
          label={formData.signupRole + " Name"}
          value={formData.orgName}
          customOnChangeFun={true}
          setValue={setFormData}
          requiredToFill={true}
        />
        <TextInput
          id={"dateEstablish"}
          type={"date"}
          alternateLabelRequired={true}
          alternateLabel={"Date of Establishment"}
          customOnChangeFun={true}
          value={formData.dateEstablish}
          setValue={setFormData}
          requiredToFill={true}
        />
        <ListSelectInput
          id={"orgType"}
          name={"orgType"}
          customOnChangeFun={true}
          value={formData.orgType}
          setValue={setFormData}
          label={"Type"}
          options={["a", "b", "c", "d"]}
        />
        <ListSelectInput
          id={"parentOrg"}
          name={"parentOrg"}
          customOnChangeFun={true}
          value={formData.parentOrg}
          setValue={setFormData}
          label={"Parent Organization"}
          options={["a", "b", "c", "d"]}
        />
        <ListSelectInput
          id={"state"}
          name={"state"}
          customOnChangeFun={true}
          value={formData.state}
          setValue={setFormData}
          label={"State"}
          options={["a", "b", "c", "d"]}
        />
        <ListSelectInput
          id={"city"}
          name={"city"}
          customOnChangeFun={true}
          value={formData.city}
          setValue={setFormData}
          label={"City"}
          options={["a", "b", "c", "d"]}
        />
        <ListSelectInput
          id={"district"}
          name={"district"}
          value={formData.district}
          customOnChangeFun={true}
          setValue={setFormData}
          label={"District"}
          options={["a", "b", "c", "d"]}
        />
        <TextInput
          id={"pinCode"}
          label={"Pincode"}
          value={formData.pinCode}
          type={"number"}
          customOnChangeFun={true}
          setValue={setFormData}
        />
        <TextInput
          id={"address"}
          label={"Address"}
          value={formData.address}
          customOnChangeFun={true}
          setValue={setFormData}
        />
      </Grid>
    </Grid>
  );
}
SchoolOrgProfile.propTypes = {
  formData: PropTypes.object.isRequired,
  setFormData: PropTypes.func.isRequired,
};
export default SchoolOrgProfile;
