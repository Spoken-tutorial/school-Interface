import React from "react";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import { colorScheme } from "../../../constants/colorScheme";
import SourceIcon from "@mui/icons-material/Source";
import { LinearGradient } from "react-text-gradients";
import VideoLibraryIcon from "@mui/icons-material/VideoLibrary";
import CourseSearch from "../CourseSearch/CourseSearch";
function HeroSection() {
  return (
    <>
      <Box
        id="home"
        sx={{
          width: "100%",
          mb: "3rem",
          mt: "-1rem",
        }}
      >
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
            variant="h2"
            gutterBottom
            sx={{
              textAlign: "center",
              fontWeight: "bold",
              letterSpacing: "0.2rem",
              mt: "3rem",
              fontSize: { xs: "3.5rem", md: "4rem" },
            }}
          >
            Spoken{" "}
            <LinearGradient
              gradient={["to left", "#FFB456 ,#F89021"]}
              fallbackColor={colorScheme.primaryOrange}
            >
              Tutorial
            </LinearGradient>
          </Typography>
          <Typography
            variant="h5"
            display="block"
            gutterBottom
            sx={{
              textAlign: "center ",
              mt: "2rem",
              color: colorScheme.secondaryGrey,

              fontSize: { xs: "1rem", md: "1.5rem" },
              letterSpacing: "0.1rem",
            }}
          >
            An Initiative of National Mission on Education throguh ICT, MHRD,
            Govt. of India to promote IT Literacy Through,
          </Typography>
          <Box sx={{ mt: "3rem" }}>
            <Box sx={{ display: "flex", flexDirection: "row", mb: "1rem" }}>
              <Box
                sx={{
                  height: "2.8rem",
                  width: "2.8rem",
                  backgroundColor: colorScheme.primaryOrangeLight,
                  borderRadius: "0.5rem",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                <SourceIcon sx={{ color: colorScheme.primaryOrange }} />
              </Box>
              <Typography
                variant="h6"
                gutterBottom
                sx={{
                  textAlign: "center",
                  fontWeight: "bold",
                  fontSize: "1.2rem",
                  ml: "1rem",
                }}
              >
                Open Source Software
              </Typography>
            </Box>
            <Box sx={{ display: "flex", flexDirection: "row", mb: "1rem" }}>
              <Box
                sx={{
                  height: "2.8rem",
                  width: "2.8rem",
                  backgroundColor: colorScheme.primaryOrangeLight,
                  borderRadius: "0.5rem",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                <VideoLibraryIcon sx={{ color: colorScheme.primaryOrange }} />
              </Box>
              <Typography
                variant="h6"
                gutterBottom
                sx={{
                  textAlign: "center",
                  fontWeight: "bold",
                  fontSize: "1.2rem",
                  ml: "1rem",
                }}
              >
                Audio Video Tutorials
              </Typography>
            </Box>
          </Box>
          <CourseSearch />
        </Container>
      </Box>
    </>
  );
}

export default HeroSection;
