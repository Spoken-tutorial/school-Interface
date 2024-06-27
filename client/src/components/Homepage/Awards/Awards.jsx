import React from "react";
import Box from "@mui/material/Box";
import Marquee from "react-fast-marquee";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import IconButton from "@mui/material/IconButton";
import useMediaQuery from "@mui/material/useMediaQuery";
import OpenInNewIcon from "@mui/icons-material/OpenInNew";
import { Grid } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import { awards } from "../../../constants/Data/homepage";
import { colorScheme } from "../../../constants/colorScheme";

function Awards() {
  const theme = useTheme();
  const isSmallScreen = useMediaQuery(theme.breakpoints.down("sm"));
  return (
    <>
      <Box id="awards">
        <Typography
          variant="h4"
          gutterBottom
          sx={{
            textAlign: "center",
            mt: "6rem",
            mb: "3rem",
            fontWeight: "bold",
          }}
        >
          Awards & Honors
        </Typography>
        <Box sx={{ mt: "3rem" }}>
          <Marquee
            speed={100}
            gradient={true}
            gradientWidth={isSmallScreen ? 60 : 200}
            pauseOnHover={true}
          >
            <Stack
              direction="row"
              justifyContent="center"
              alignItems="center"
              spacing={10}
              sx={{
                p: "2rem",
              }}
            >
              {awards.map((award) => (
                <Box
                  key={award}
                  sx={{
                    width: "15rem",
                    height: "8rem",
                    background: `radial-gradient(circle, ${"#ffffff"}, ${
                      colorScheme.primaryOrangeLight
                    })`,
                    borderRadius: "0.5rem",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    boxShadow: "0px 0px 12px -5px " + colorScheme.lightText,
                    "&:hover": { transform: "scale(1.1)" },
                  }}
                >
                  <Grid container sx={{ width: "100%" }}>
                    <Grid
                      item
                      sx={{
                        width: "100%",
                        display: "flex",
                        justifyContent: "end",
                      }}
                    >
                      <IconButton aria-label="delete">
                        <OpenInNewIcon
                          sx={{
                            color: colorScheme.primaryOrange,
                            fontSize: "1rem",
                          }}
                        />
                      </IconButton>
                    </Grid>
                    <Grid item sx={{ width: "100%" }}>
                      <Typography
                        variant="h6"
                        gutterBottom
                        sx={{
                          textAlign: "center",
                          p: "1rem",
                          fontWeight: "bold",
                          fontSize: "1.2rem",
                          color: colorScheme.secondaryGrey,
                        }}
                      >
                        {award}
                      </Typography>
                    </Grid>
                  </Grid>
                </Box>
              ))}
            </Stack>
          </Marquee>
        </Box>
      </Box>
    </>
  );
}

export default Awards;
