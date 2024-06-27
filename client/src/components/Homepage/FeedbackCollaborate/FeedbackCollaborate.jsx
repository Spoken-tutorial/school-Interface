import React from "react";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import ContactUsForm from "./ContactUsForm";
import Collaborate from "./Collaborate";

function FeedbackCollaborate() {
  return (
    <Box>
      <Container
        sx={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Typography
          variant="h4"
          gutterBottom
          sx={{
            textAlign: "center",
            mt: "6rem",
            mb: "2rem",
            fontWeight: "bold",
          }}
        >
          Thanks for Visiting Us
        </Typography>
        <Grid container direction="row">
          <Grid item xs={12} md={6}>
            <ContactUsForm />
          </Grid>
          <Grid item xs={12} md={6}>
            <Collaborate />
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
}

export default FeedbackCollaborate;
