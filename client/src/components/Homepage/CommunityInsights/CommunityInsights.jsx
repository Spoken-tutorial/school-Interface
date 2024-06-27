import React from "react";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Container from "@mui/material/Container";
import ForumIcon from "@mui/icons-material/Forum";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";
import { colorScheme } from "../../../constants/colorScheme";
import { coumminityInsights } from "../../../constants/Data/homepage";

function CommunityInsights() {
  return (
    <>
      <Box id="community">
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
            Community Insights & Learning Resources
          </Typography>
          <Box
            sx={{
              p: "2rem",
              display: "flex",
              justifyContent: "center",
            }}
          >
            <Grid
              container
              direction="row"
              justifyContent={"center"}
              alignItems={"center"}
              spacing={4}
            >
              {coumminityInsights.map((data) => (
                <Grid item xs={12} md={4} key={data.title}>
                  <Grid container direction="column">
                    <>
                      <Grid item sx={{ mt: "1.5rem" }}>
                        <Box
                          sx={{
                            height: "3rem",
                            width: "3rem",
                            backgroundColor: colorScheme.primaryOrangeLight,
                            borderRadius: "0.5rem",
                            display: "flex",
                            justifyContent: "center",
                            alignItems: "center",
                          }}
                        >
                          <ForumIcon
                            sx={{ color: colorScheme.primaryOrange }}
                          />
                        </Box>
                      </Grid>
                      <Grid item sx={{ mt: "1rem" }}>
                        <Typography
                          variant="h6"
                          gutterBottom
                          sx={{ fontWeight: "bold" }}
                        >
                          {data.title}
                        </Typography>
                      </Grid>
                      <Grid item>
                        <Typography
                          gutterBottom
                          variant="caption"
                          sx={{
                            color: colorScheme.lightText,
                            fontSize: "1rem",
                          }}
                        >
                          {data.description}
                        </Typography>
                      </Grid>
                      <Grid item sx={{ mt: "1rem", mb: "2rem" }}>
                        <Button
                          variant="text"
                          size="small"
                          sx={{ color: colorScheme.primaryOrange }}
                          endIcon={
                            <ArrowForwardIcon
                              sx={{ color: colorScheme.primaryOrange }}
                            />
                          }
                        >
                          Learn More
                        </Button>
                      </Grid>
                    </>
                  </Grid>
                </Grid>
              ))}
            </Grid>
          </Box>
        </Container>
      </Box>
    </>
  );
}

export default CommunityInsights;
