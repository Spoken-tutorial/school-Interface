/* eslint-disable react/prop-types */
import React from "react";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import InputAdornment from "@mui/material/InputAdornment";
import { colorScheme } from "../../constants/colorScheme";
import { PropTypes } from "prop-types";

function TextInput({
  id,
  type,
  value,
  setValue,
  label,
  alternateLabelRequired,
  alternateLabel,
  requiredToFill,
  iconRequired,
  icon,
  multiline,
  rows,
  style,
  customOnChangeFun,
}) {
  const handleChange = (event) => {
    setValue(event.target.value);
  };
  return (
    <>
      {/* alternate label if required for other types of input */}
      {alternateLabelRequired && (
        <Typography sx={{ mt: "1.7rem", mb: "-1.7rem", opacity: "60%" }}>
          {alternateLabel}
        </Typography>
      )}
      {/* for custom onChange function make sure name==id of textinput matches formdata key */}
      <TextField
        id={id}
        name={id}
        label={alternateLabelRequired ? "" : label}
        multiline={multiline}
        rows={multiline ? rows : undefined}
        variant="outlined"
        size="small"
        value={value}
        required={requiredToFill}
        type={type ? type : "text"}
        onChange={customOnChangeFun ? setValue : handleChange}
        InputProps={{
          startAdornment: iconRequired ? (
            <InputAdornment position="start">{icon}</InputAdornment>
          ) : null,
        }}
        sx={{
          "& .MuiOutlinedInput-root": {
            "&.Mui-focused fieldset": {
              borderColor: colorScheme.primaryOrange,
            },
          },
          "& label.Mui-focused": {
            color: "#000000",
          },
          width: { xs: "100%", md: "17rem", lg: "20rem" },
          mr: { xs: 0, md: "3rem" },
          mb: { xs: "1.5rem", md: 0 },
          mt: "2rem",
          ...style,
        }}
      />
    </>
  );
}

TextInput.propTypes = {
  id: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  setValue: PropTypes.func.isRequired,
  label: PropTypes.string,
  alternateLabelRequired: PropTypes.bool,
  alternateLabel: PropTypes.string,
  requiredToFill: PropTypes.bool,
  iconRequired: PropTypes.bool,
  icon: PropTypes.element,
  multiline: PropTypes.bool,
  rows: PropTypes.number,
  style: PropTypes.object,
  customOnChangeFun: PropTypes.bool,
};

export default TextInput;
