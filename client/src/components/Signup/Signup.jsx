import React, { useState, useEffect } from "react";
import Box from "@mui/material/Box";
import Stepper from "@mui/material/Stepper";
import Step from "@mui/material/Step";
import StepLabel from "@mui/material/StepLabel";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import SelectRole from "./Step1/SelectRole";
import SignupForm from "./Step2/SignupForm";
import { colorScheme } from "../../constants/colorScheme";
import { Container } from "@mui/material";
import { Link, useNavigate } from "react-router-dom";
import { steps, initialFormData } from "../../constants/Data/signup";
import { PropTypes } from "prop-types";

const stepStyle = {
  "& .Mui-active": {
    "& .MuiSvgIcon-root": {
      color: colorScheme.secondaryGrey,
    },
  },
  "& .Mui-completed": {
    "& .MuiSvgIcon-root": {
      color: colorScheme.primaryOrange,
    },
  },
};

function Signup({ urlRole }) {
  const [formData, setFormData] = useState(initialFormData);

  //to move to next step automatically if role already selected
  const navigate = useNavigate();
  useEffect(() => {
    if (urlRole) {
      setFormData((prevFormData) => ({
        ...prevFormData,
        signupRole: urlRole,
      }));
      setActiveStep(1);
    }
  }, [urlRole]);

  const [activeStep, setActiveStep] = useState(0);
  const [skipped, setSkipped] = useState(new Set());

  const isStepSkipped = (step) => {
    return skipped.has(step);
  };

  const handleNext = () => {
    if (activeStep === 0 && formData.signupRole === "") {
      alert("Please Select Role");
    } else {
      let newSkipped = skipped;
      if (isStepSkipped(activeStep)) {
        newSkipped = new Set(newSkipped.values());
        newSkipped.delete(activeStep);
      }
      setActiveStep((prevActiveStep) => prevActiveStep + 1);
      setSkipped(newSkipped);
    }
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleReset = () => {
    setActiveStep(0);
    setFormData(initialFormData);
    navigate("/signup");
  };
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  return (
    <Container sx={{ width: "100vw", pt: "1rem" }}>
      {/* stepper icon and label */}
      <Stepper activeStep={activeStep} alternativeLabel sx={stepStyle}>
        {steps.map((label, index) => {
          return (
            <Step key={label}>
              <StepLabel>
                {index === 0 && formData.signupRole !== ""
                  ? formData.signupRole
                  : label}
              </StepLabel>
            </Step>
          );
        })}
      </Stepper>

      {/* after all steps completed component */}
      {activeStep === steps.length ? (
        <React.Fragment>
          <Typography sx={{ mt: 2, mb: 1 }}>
            All steps completed - you&apos;re finished
          </Typography>
          <Box sx={{ display: "flex", flexDirection: "row", pt: 2 }}>
            <Box sx={{ flex: "1 1 auto" }} />
            <Link to="/login" style={{ textDecoration: "none" }}>
              Login
            </Link>
          </Box>
        </React.Fragment>
      ) : (
        <React.Fragment>
          {/* Each step body content here */}
          {activeStep === 0 ? (
            // step 1
            <SelectRole
              role={formData.signupRole}
              setRole={(role) =>
                setFormData((prevFormData) => ({
                  ...initialFormData,
                  signupRole: role,
                }))
              }
            />
          ) : activeStep === 1 ? (
            // step 2
            <SignupForm formData={formData} setFormData={handleChange} />
          ) : // step 3
          null}

          <Box sx={{ display: "flex", flexDirection: "row", pt: 2 }}>
            {/* back button */}
            <Button
              disabled={activeStep === 0}
              onClick={handleBack}
              sx={{
                height: "1.6rem",
                fontSize: "0.8rem",
                borderColor: colorScheme.primaryOrange,
                mr: 1,
                mb: "1rem",
                mt: "1rem",
                color: colorScheme.primaryOrange,
                "&:hover": {
                  borderColor: colorScheme.primaryOrange,
                },
              }}
              variant="outlined"
            >
              Back
            </Button>

            {/* next button box */}
            <Box sx={{ flex: "1 1 auto" }} />

            {/* next & reset button */}
            {activeStep === steps.length - 1 ? (
              <Button
                variant="outlined"
                size="small"
                sx={{
                  height: "1.6rem",
                  fontSize: "0.8rem",
                  mt: "1rem",
                  backgroundColor: colorScheme.primaryOrangeLight,
                  borderColor: colorScheme.primaryOrange,
                  color: colorScheme.primaryOrange,
                  mr: "1rem",
                  "&:hover": {
                    borderColor: colorScheme.primaryOrange,
                    backgroundColor: colorScheme.primaryOrangeLight,
                  },
                }}
                onClick={handleReset}
              >
                Reset
              </Button>
            ) : null}

            <Button
              variant="contained"
              size="small"
              sx={{
                height: "1.6rem",
                fontSize: "0.8rem",
                mt: "1rem",
                backgroundColor: colorScheme.primaryOrange,
                "&:hover": { backgroundColor: colorScheme.primaryOrange },
              }}
              onClick={handleNext}
            >
              {activeStep === steps.length - 1 ? "Signup" : "Next"}
            </Button>
          </Box>
        </React.Fragment>
      )}
    </Container>
  );
}

Signup.propTypes = {
  urlRole: PropTypes.string,
};
export default Signup;
