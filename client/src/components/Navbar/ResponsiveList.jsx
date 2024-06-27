import React, { useEffect } from "react";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import Typography from "@mui/material/Typography";
import PersonIcon from "@mui/icons-material/Person";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";
import RateReviewIcon from "@mui/icons-material/RateReview";
import ForumIcon from "@mui/icons-material/Forum";
import Groups3Icon from "@mui/icons-material/Groups3";
import HandshakeIcon from "@mui/icons-material/Handshake";
import EmojiEventsIcon from "@mui/icons-material/EmojiEvents";
import ReviewsIcon from "@mui/icons-material/Reviews";
import HomeIcon from "@mui/icons-material/Home";
import { colorScheme } from "../../constants/colorScheme";
import { navItems } from "../../constants/Data/navbar";
import { PropTypes } from "prop-types";

function ResponsiveList({ handleNavItemClick }) {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const iconMap = {
    Home: <HomeIcon sx={{ color: colorScheme.secondaryGrey }} />,
    Forum: <ForumIcon sx={{ color: colorScheme.secondaryGrey }} />,
    Testimonials: <ReviewsIcon sx={{ color: colorScheme.secondaryGrey }} />,
    Collaborate: <HandshakeIcon sx={{ color: colorScheme.secondaryGrey }} />,
    Feedback: <RateReviewIcon sx={{ color: colorScheme.secondaryGrey }} />,
    Awards: <EmojiEventsIcon sx={{ color: colorScheme.secondaryGrey }} />,
    Community: <Groups3Icon sx={{ color: colorScheme.secondaryGrey }} />,
  };

  return (
    <Box
      sx={{
        width: "100%",
        height: "100%",
        mt: "2rem",
        mb: "-2.2rem",
      }}
    >
      {/* Login button */}

      <ListItem
        key={"LoginList"}
        onClick={() => handleNavItemClick("login", "ResponsiveList")}
        sx={{
          mb: "0.8rem",
          mt: "0.5rem",
          cursor: "pointer",
          textDecoration: "none",
          "&:hover": { color: colorScheme.primaryOrange },
        }}
      >
        <ListItemIcon key={"loginListIcon"}>
          <PersonIcon
            key={"loginIcon"}
            sx={{ color: colorScheme.secondaryGrey }}
          />
        </ListItemIcon>

        <Typography
          key={"loginListText"}
          variant="h6"
          gutterBottom
          sx={{
            textDecoration: "none!important",
            color: "#000000",
            fontSize: "1rem",
            mr: "1rem",
            "&:hover": { color: colorScheme.primaryOrange },
            cursor: "pointer",
          }}
        >
          Login
        </Typography>
      </ListItem>

      <Divider sx={{ height: "0.1rem" }} />
      <List>
        {navItems.map((navItem, index) => (
          <React.Fragment key={navItem.title + "listItem"}>
            <ListItem
              sx={{
                mb: "0.8rem",
                mt: "0.5rem",
                cursor: "pointer",
                "&:hover": { color: colorScheme.primaryOrange },
              }}
              onClick={() =>
                handleNavItemClick(navItem.title, "ResponsiveList", "scroll")
              }
            >
              <ListItemIcon key={navItem.title + "listItemIcon"}>
                {iconMap[navItem.title] || "#"}
              </ListItemIcon>
              <ListItemText
                key={navItem.title + "listItemText"}
                primary={navItem.title}
                sx={{ "&-hover": { color: colorScheme.primaryOrange } }}
              />
            </ListItem>
            <Divider
              key={navItem.title + "divider"}
              sx={{ height: "0.1rem" }}
            />
          </React.Fragment>
        ))}
      </List>
    </Box>
  );
}

ResponsiveList.propTypes = {
  handleNavItemClick: PropTypes.func.isRequired,
};

export default ResponsiveList;
