import Toolbar from "@mui/material/Toolbar";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import PropTypes from "prop-types";
import ClearIcon from "@mui/icons-material/Clear";
import Button from "@mui/material/Button";
import DoneIcon from "@mui/icons-material/Done";
import { colorScheme } from "../../constants/colorScheme";

function TableToolbar(props) {
  const { numSelected, signupRole } = props;

  return (
    <Toolbar
      sx={{
        pl: { sm: 2 },
        pr: { xs: 1, sm: 1 },
        backgroundColor: colorScheme.secondaryGrey,
        height: { xs: "auto", md: "2rem!important" },
        borderTopLeftRadius: "0.5rem",
        borderTopRightRadius: "0.5rem",
      }}
    >
      {numSelected > 0 ? (
        <Typography
          sx={{ flex: "1 1 100%", fontSize: "1rem" }}
          color={colorScheme.primaryOrange}
          variant="overline"
          component="div"
        >
          {numSelected} Selected
        </Typography>
      ) : (
        <Typography
          sx={{
            flex: "1 1 100%",
            color: colorScheme.primaryOrange,
            fontSize: "1rem",

            letterSpacing: "0.1rem",
          }}
          variant="overline"
          id="tableTitle"
          component="div"
        >
          {`${signupRole} Registration Details`}
        </Typography>
      )}

      {numSelected > 0 ? (
        <>
          <Box
            sx={{
              display: "flex",
              gap: "1rem",
              mr: "0.5rem",
              pt: "0.2rem",
              pb: "0.2rem",
            }}
          >
            <Button
              variant="contained"
              size="small"
              sx={{
                backgroundColor: colorScheme.primaryOrange,
                color: "#ffffff",
                height: "1.5rem",
                fontSize: "0.8rem",
                "&:hover": {
                  backgroundColor: colorScheme.primaryOrange,
                  color: "#ffffff",
                },
              }}
            >
              Approve
            </Button>
            <Button
              variant="contained"
              size="small"
              sx={{
                backgroundColor: colorScheme.primaryOrangeLight,
                color: colorScheme.primaryOrange,
                borderColor: colorScheme.primaryOrange,
                fontSize: "0.8rem",
                height: "1.5rem",
                "&:hover": {
                  backgroundColor: colorScheme.primaryOrangeLight,
                },
              }}
            >
              Reject
            </Button>
          </Box>
        </>
      ) : null}
    </Toolbar>
  );
}

TableToolbar.propTypes = {
  numSelected: PropTypes.number.isRequired,
  signupRole: PropTypes.string.isRequired,
};

export default TableToolbar;
