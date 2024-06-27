/* eslint-disable react/prop-types */
import React, { useState, useEffect } from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import TextInput from "../common/TextInput";
import KeyIcon from "@mui/icons-material/Key";
import AlternateEmailIcon from "@mui/icons-material/AlternateEmail";
import { colorScheme } from "../../constants/colorScheme";
import { Link, useNavigation } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigation = useNavigation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <>
      <Box
        sx={{
          height: "100vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          mt: "-3rem",
        }}
      >
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            backgroundColor: "#ffffff",
            flexDirection: "column",
            alignItems: "center",
            justifyItems: "center",
            alignContent: "center",
            borderColor: colorScheme.lightText,
            borderWidth: "0.02rem",
            width: { xs: "19rem", sm: "25rem", md: "30rem" },
            height: "25rem",
            borderRadius: "1rem",
            boxShadow: "0px 0px 12px -5px " + colorScheme.lightText,
          }}
        >
          <Typography
            variant="h5"
            gutterBottom
            sx={{
              textAlign: "center",
              fontWeight: "bold",
              mt: "2.5rem",
              fontSize: { xs: "1.2rem", sm: "1.5rem" },
              color: "#000000",
            }}
          >
            Sign in to your account
          </Typography>
          <form>
            <Box
              sx={{
                width: "80%",
                display: "flex",
                justifyContent: "center",
                flexDirection: "column",
              }}
            >
              <Box sx={{ width: "100%" }}>
                <TextInput
                  value={email}
                  requiredToFill={true}
                  setValue={setEmail}
                  label={"Username"}
                  id={"username"}
                  type={"email"}
                  iconRequired={true}
                  icon={<AlternateEmailIcon />}
                />
              </Box>
              <Box sx={{ width: "100%", mt: "0.5rem" }}>
                <TextInput
                  value={password}
                  setValue={setPassword}
                  label={"Password"}
                  requiredToFill={true}
                  id={"password"}
                  type={"password"}
                  iconRequired={true}
                  icon={<KeyIcon />}
                />
              </Box>
              <Typography variant="caption" display="block" sx={{ mt: "1rem" }}>
                Forgot password?
              </Typography>
              <Box
                sx={{
                  backgrdounColor: "red",
                  width: "100%",
                  mt: "0.5rem",
                }}
              >
                <Button
                  size="small"
                  type="submit"
                  variant="contained"
                  name="actionType"
                  value="login"
                  disabled={navigation.state === "submitting" ? true : false}
                  sx={{
                    mt: "1rem",
                    backgroundColor: colorScheme.primaryOrange,
                    "&:hover": {
                      color: "#ffffff",
                      backgroundColor: colorScheme.primaryOrange,
                    },
                  }}
                >
                  {navigation.state === "submitting"
                    ? "Please Wait..."
                    : "Login"}
                </Button>
              </Box>

              <Box
                sx={{
                  mb: "1.5rem",
                  mt: "1rem",
                }}
              >
                <Typography
                  variant="caption"
                  display="block"
                  sx={{
                    mb: "1rem",
                    mt: "0.5rem",
                    color: colorScheme.secondaryGrey,
                  }}
                >
                  <Link
                    style={{
                      textDecoration: "none",
                      color: colorScheme.primaryOrange,
                    }}
                    to="/signup"
                  >
                    Dont' have an account?
                  </Link>{" "}
                  ( Register Now )
                </Typography>
              </Box>
            </Box>
          </form>
        </Box>
      </Box>
    </>
  );
}
