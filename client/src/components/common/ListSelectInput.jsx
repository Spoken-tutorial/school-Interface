import React from "react";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import { colorScheme } from "../../constants/colorScheme";
import { PropTypes } from "prop-types";

function ListSelectInput({
  id,
  name,
  value,
  setValue,
  label,
  options,
  customOnChangeFun,
}) {
  const handleChange = async (event) => {
    setValue(event.target.value);
  };

  return (
    <>
      <FormControl
        variant="outlined"
        sx={{
          width: { xs: "100%", md: "17rem", lg: "20rem" },
          mt: "2rem",
          mr: "3rem",
          "& .MuiOutlinedInput-root": {
            "&.Mui-focused .MuiOutlinedInput-notchedOutline": {
              borderColor: colorScheme.primaryOrange,
            },
          },
          "& .MuiInputLabel-root": {
            "&.Mui-focused": {
              color: colorScheme.secondaryGrey,
            },
          },
        }}
        size="small"
        id={id}
      >
        <InputLabel id={id} sx={{ fontSize: "0.9rem" }}>
          {label}
        </InputLabel>
        <Select
          labelId={id}
          id={id}
          name={name}
          value={value}
          onChange={customOnChangeFun ? setValue : handleChange}
          label={label}
        >
          {options.map((obj) => (
            <MenuItem key={obj} value={obj} sx={{ fontSize: "0.7rem" }}>
              {obj}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </>
  );
}

ListSelectInput.propTypes = {
  id: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  setValue: PropTypes.func.isRequired,
  label: PropTypes.string.isRequired,
  customOnChangeFun: PropTypes.bool,
  options: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default ListSelectInput;
