import React, { useState } from "react";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import RoleCard from "./RoleCard";
import { ButtonBase } from "@mui/material";
import { colorScheme } from "../../../constants/colorScheme";
import { useNavigate } from "react-router-dom";
import { PropTypes } from "prop-types";
import { roleData } from "../../../constants/Data/signup";

function SelectRole({ role, setRole }) {
  const navigate = useNavigate();

  const [borderSelected, setBorderSelected] = useState(
    roleData.findIndex((r) => r.roleTitle === role)
  );

  function handleRoleSelect(index) {
    const role = roleData[index].roleTitle;
    setRole(role);
    const urlRole = role.toLowerCase().replace(/\s+/g, "-");
    setBorderSelected(index);
    navigate("/signup/" + urlRole);
  }

  return (
    <>
      <Box sx={{ mt: "2rem" }}>
        <Grid
          container
          justifyContent={{ xs: "center", sm: "center", md: "flex-start" }}
          alignItems={{ xs: "center", sm: "center", md: "flex-start" }}
        >
          {roleData.map((data, index) => (
            <Grid
              item
              key={data.roleTitle}
              xs={12}
              sm={12}
              md={6}
              sx={{
                borderStyle: "solid",
                borderColor: "#E3E3E3",
                borderWidth: "0.02rem",
                boxShadow: "0px 0px 1px rgba(0, 0, 0, 0.5)",
                borderRightWidth: {
                  md: index % 2 === 0 ? "0" : "0.02rem",
                  lg: index % 2 === 0 ? "0" : "0.02rem",
                },
                borderTopLeftRadius: index === 0 ? "0.4rem" : 0,
                borderBottomWidth: {
                  xs: index === roleData.length - 1 ? "0.02rem" : 0,
                  sm: index === roleData.length - 1 ? "0.02rem" : 0,
                  md:
                    index === roleData.length - 1 ||
                    index === roleData.length - 2
                      ? "0.02rem"
                      : 0,
                },
                borderTopRightRadius: {
                  xs: index === 0 ? "0.4rem" : 0,
                  sm: index === 0 ? "0.4rem" : 0,
                  md: index === 1 ? "0.4rem" : 0,
                },
                borderBottomRightRadius:
                  index === roleData.length - 1 ? "0.4rem" : 0,
                borderBottomLeftRadius: {
                  xs: index === roleData.length - 1 ? "0.4rem" : 0,
                  sm: index === roleData.length - 1 ? "0.4rem" : 0,
                  md: index === roleData.length - 2 ? "0.4rem" : 0,
                },
                transition: "box-shadow 0.3s ease, transform 0.3s ease",
                "&:hover": {
                  transform: index === borderSelected ? null : "scale(1.007)",
                  borderColor:
                    index === borderSelected ? null : colorScheme.primaryOrange,
                  borderWidth: index === borderSelected ? null : "0.1rem",
                },
              }}
            >
              <ButtonBase
                onClick={() => handleRoleSelect(index)}
                disabled={index === borderSelected ? true : false}
                sx={{
                  borderStyle: index === borderSelected ? "solid" : "none",
                  borderColor: colorScheme.primaryOrange,
                  borderWidth: "0.1rem",
                  borderTopLeftRadius: index === 0 ? "0.4rem" : 0,
                  borderTopRightRadius: index === 1 ? "0.4rem" : 0,
                  borderBottomRightRadius:
                    index === roleData.length - 1 ? "0.4rem" : 0,
                  borderBottomLeftRadius:
                    index === roleData.length - 2 ? "0.4rem" : 0,
                }}
              >
                <Box sx={{ p: "1.5rem" }}>
                  <RoleCard
                    title={data.roleTitle}
                    description={data.roleDescription}
                  />
                </Box>
              </ButtonBase>
            </Grid>
          ))}
        </Grid>
      </Box>
    </>
  );
}

SelectRole.propTypes = {
  role: PropTypes.string.isRequired,
  setRole: PropTypes.func.isRequired,
};

export default SelectRole;
