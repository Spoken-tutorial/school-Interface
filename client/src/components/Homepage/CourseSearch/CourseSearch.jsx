import React, { useState } from "react";
import ListSelectInput from "../../common/ListSelectInput";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import { colorScheme } from "../../../constants/colorScheme";
import { Grid } from "@mui/material";

function CourseSearch() {
  const [course, setCourse] = useState("");
  const [language, setLanguage] = useState("");
  return (
    <>
      <Grid
        container
        direction="row"
        justifyContent="space-evenly"
        alignItems="center"
        columnSpacing={6}
        sx={{ mt: "1rem" }}
      >
        <Grid item xs={12} md={2}>
          <ListSelectInput
            id={"courseList"}
            name={"courseSearch"}
            value={course}
            setValue={setCourse}
            label={"Courses"}
            options={["a", "b", "c", "d"]}
          />
        </Grid>
        <Grid item xs={12} md={2}>
          <ListSelectInput
            id={"languageList"}
            name={"languageSearch"}
            value={language}
            setValue={setLanguage}
            label={"Languages"}
            options={["a", "b", "c", "d"]}
          />
        </Grid>
        <Grid item xs={12} md={1}>
          <IconButton
            aria-label="search"
            sx={{
              mt: "1.7rem",
              ml: {
                md: "-1rem",
                color: colorScheme.primaryOrange,
                backgroundColor: colorScheme.primaryOrangeLight,
                "&:hover": { backgroundColor: colorScheme.primaryOrangeLight },
              },
            }}
          >
            <SearchIcon />
          </IconButton>
        </Grid>
      </Grid>
    </>
  );
}

export default CourseSearch;
