import React, { useState } from "react";
import Grid from "@mui/material/Grid";
import { Box, Typography } from "@mui/material";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import TextInput from "../../common/TextInput";
import { colorScheme } from "../../../constants/colorScheme";

function ContactUsForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  return (
    <>
      <Container id="feedback">
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
              Feedback
            </Typography>
          </Grid>
          {/* name */}
          <Grid
            item
            sx={{
              width: "100%",
              display: "flex",
              justifyContent: "flex-start",
            }}
          >
            <TextInput
              value={name}
              setValue={setName}
              requiredToFill={true}
              label={"Your Name"}
              id={"yourName"}
              style={{ width: "100%", mt: "-0.5rem", mb: "-1rem" }}
            />
          </Grid>

          {/* email */}
          <Grid
            item
            sx={{
              width: "100%",
              display: "flex",
              justifyContent: "flex-start",
            }}
          >
            <TextInput
              value={email}
              setValue={setEmail}
              requiredToFill={true}
              label={"Your Email"}
              id={"yourEmail"}
              style={{ width: "100%", mb: "-1rem" }}
            />
          </Grid>

          {/* message */}
          <Grid
            item
            sx={{
              width: "100%",
              display: "flex",
              justifyContent: "flex-start",
            }}
          >
            <TextInput
              value={message}
              setValue={setMessage}
              requiredToFill={true}
              label={"Your Message"}
              id={"yourMessage"}
              style={{ width: "100%", mb: "-1rem" }}
              multiline={true}
              rows={8}
            />
          </Grid>

          {/* send button */}
          <Grid
            item
            sx={{
              width: "100%",
              display: "flex",
              justifyContent: "flex-start",
            }}
          >
            <Box
              sx={{
                width: "80%",
              }}
            >
              <Button
                size="small"
                variant="outlined"
                sx={{
                  borderColor: colorScheme.primaryOrange,
                  color: colorScheme.primaryOrange,
                  mt: "0.5rem",
                  fontSize: {
                    xs: "0.7rem",
                    sm: "0.9rem",
                    md: "0.8rem",
                  },
                  "&:hover": {
                    color: "#ffffff",
                    backgroundColor: colorScheme.primaryOrange,
                    borderColor: colorScheme.primaryOrange,
                  },
                }}
              >
                Send
              </Button>
            </Box>
          </Grid>
        </Grid>
      </Container>
    </>
  );
}

export default ContactUsForm;
