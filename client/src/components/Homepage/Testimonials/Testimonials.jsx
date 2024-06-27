import React, { useState } from "react";
import Box from "@mui/material/Box";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import IconButton from "@mui/material/IconButton";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import { Grid } from "@mui/material";
import Divider from "@mui/material/Divider";
import { colorScheme } from "../../../constants/colorScheme";
import { testimonials } from "../../../constants/Data/homepage";

function Testimonials() {
  const [expanded, setExpanded] = useState({});

  const truncateMessage = (message, length) => {
    if (message.length <= length) return message;
    return message.slice(0, length) + "...";
  };

  const handleReadMore = (author) => {
    setExpanded((prev) => ({
      ...prev,
      [author]: !prev[author],
    }));
  };

  return (
    <Box>
      <Container
        id="testimonials"
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
          Testimonials
        </Typography>
        <Box
          sx={{
            p: "2rem",
            display: "flex",
            justifyContent: "center",
          }}
        >
          <Grid container spacing={4} justifyContent="center">
            {testimonials.map((data) => {
              const isExpanded = expanded[data.author];
              const message = isExpanded
                ? data.message
                : truncateMessage(data.message, 140);
              return (
                <Grid item xs={12} sm={6} md={4} key={data.author}>
                  <Box
                    sx={{
                      background: `radial-gradient(circle, ${"#ffffff"}, ${
                        colorScheme.primaryOrangeLight
                      })`,
                      borderRadius: "0.5rem",
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                      boxShadow: "0px 0px 12px -5px " + colorScheme.lightText,
                      "&:hover": { transform: "scale(1.1)" },
                      p: "1rem",
                    }}
                  >
                    <Grid container direction="column" alignItems="center">
                      <Grid item>
                        <Typography
                          variant="caption"
                          gutterBottom
                          sx={{
                            textAlign: "center",
                            fontSize: "0.8rem",
                            color: colorScheme.secondaryGrey,
                          }}
                        >
                          "{message}"{" "}
                          <IconButton
                            onClick={() => handleReadMore(data.author)}
                            sx={{
                              fontSize: "0.7rem",
                              color: colorScheme.lightText,
                            }}
                          >
                            {isExpanded ? "Read Less" : "Read More"}
                          </IconButton>
                        </Typography>
                      </Grid>
                      <Divider
                        variant="fullWidth"
                        sx={{ width: "100%", mt: "1rem", mb: "-0.3rem" }}
                      />
                      <Grid
                        item
                        sx={{
                          display: "flex",
                          justifyContent: "space-around",
                          alignItems: "center",
                          alignContent: "center",
                          mt: "0.5rem",
                        }}
                      >
                        <AccountCircleIcon
                          sx={{ color: colorScheme.primaryOrange }}
                        />
                        <Typography
                          variant="caption"
                          sx={{
                            fontSize: "0.7rem",
                            fontWeight: "bold",
                            mt: "0rem",
                            ml: "0.5rem",
                          }}
                        >
                          {data.author}
                        </Typography>
                      </Grid>
                    </Grid>
                  </Box>
                </Grid>
              );
            })}
          </Grid>
        </Box>
      </Container>
    </Box>
  );
}

export default Testimonials;
