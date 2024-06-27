import React from "react";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import Typography from "@mui/material/Typography";
import { colorScheme } from "../../constants/colorScheme";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormControl from "@mui/material/FormControl";
import { PropTypes } from "prop-types";

function RadioInput({
  id,
  label,
  options,
  name,
  value,
  setValue,
  customOnChangeFun,
}) {
  const handleChange = async (event) => {
    setValue(event.target.value);
  };
  return (
    <FormControl id={id}>
      <Typography sx={{ opacity: "60%", mb: ".5rem", mt: "2rem" }}>
        {label}
      </Typography>
      <RadioGroup
        row
        aria-labelledby={label + "radio-group-label"}
        name={name}
        value={value}
        onChange={customOnChangeFun ? setValue : handleChange}
      >
        {options.map((label) => (
          <FormControlLabel
            key={label}
            value={label}
            control={
              <Radio
                sx={{
                  "&.Mui-checked": {
                    color: colorScheme.primaryOrange,
                  },
                }}
              />
            }
            label={label}
          />
        ))}
      </RadioGroup>
    </FormControl>
  );
}

RadioInput.propTypes = {
  id: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  options: PropTypes.arrayOf(PropTypes.string).isRequired,
  name: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  setValue: PropTypes.func.isRequired,
  customOnChangeFun: PropTypes.bool,
};

export default RadioInput;
