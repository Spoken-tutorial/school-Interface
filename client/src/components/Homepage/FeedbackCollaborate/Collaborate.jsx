import React from "react";
import Grid from "@mui/material/Grid";
import { Typography } from "@mui/material";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import Chip from "@mui/material/Chip";
import { colorScheme } from "../../../constants/colorScheme";
import { additionalLinks } from "../../../constants/Data/homepage";

function Collaborate() {
  return (
    <Container id="collaborate">
      <Grid
        container
        direction="column"
        justifyContent="flex-start"
        alignItems="center"
        rowSpacing={3}
        sx={{ mt: "2rem" }}
      >
        {/* title */}
        <Grid
          item
          sx={{
            width: "100%",
            display: "flex",
            justifyContent: "flex-start",
          }}
        >
          <Typography
            variant="h6"
            gutterBottom
            sx={{
              textAlign: "center",
              fontWeight: "bold",
            }}
          >
            Collaborate with Us
          </Typography>
        </Grid>
        {/* description */}
        <Grid
          item
          sx={{
            width: "100%",
            display: "flex",
            justifyContent: "flex-start",
          }}
        >
          <Typography
            variant="caption"
            display="block"
            gutterBottom
            sx={{
              fontSize: "1rem",
              mt: "-1rem",
              mb: "1rem",
              color: colorScheme.lightText,
            }}
          >
            We invite you to become a part of this amazing journey of making
            India IT-literate. Join our growing network of Resources Centres,
            Organisers, Content creators, Domain Experts, Translators, Dubbers,
            Reviewers and help us to reach every nook and corner of India.
          </Typography>
        </Grid>
        {/* form link */}
        <Grid
          item
          sx={{
            width: "100%",
            display: "flex",
            justifyContent: "flex-start",
          }}
        >
          <Typography
            variant="caption"
            display="block"
            gutterBottom
            sx={{
              fontSize: "1rem",
              mt: "-1rem",
              mb: "1rem",
              color: colorScheme.lightText,
            }}
          >
            First step to do so - fill the form given{" "}
            <Button
              variant="text"
              sx={{ height: "0.8rem", color: colorScheme.primaryOrange }}
            >
              Here
            </Button>
          </Typography>
        </Grid>
        {/* Additional Links */}
        <Grid
          item
          sx={{
            width: "100%",
            display: "flex",
            justifyContent: "flex-start",
          }}
        >
          <Stack
            direction={{ xs: "column", md: "row" }}
            spacing={{ xs: 3, md: 2 }}
          >
            {additionalLinks.map((data) => (
              <Chip
                key={data.label}
                label={data.label}
                component="a"
                href={data.url}
                target="_blank"
                variant="outlined"
                clickable
                sx={{
                  borderColor: colorScheme.primaryOrange,
                  color: colorScheme.primaryOrange,
                  backgroundColor: "#ffffff",
                }}
              />
            ))}
          </Stack>
        </Grid>
      </Grid>
    </Container>
  );
}

export default Collaborate;
