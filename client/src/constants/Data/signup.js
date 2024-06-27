const roleData = [
  {
    roleTitle: "Organization",
    roleDescription:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  {
    roleTitle: "School",
    roleDescription:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  {
    roleTitle: "User",
    roleDescription:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  {
    roleTitle: "Training Team",
    roleDescription:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
];

const steps = ["Select Role", "Fill Details"];

const initialFormData = {
  signupRole: "",
  firstName: "",
  lastName: "",
  email: "",
  username: "",
  phone: "",
  password: "",
  confirmPassword: "",
  dob: "",
  userOrg: "",
  userSchool: "",
  userRole: "",
  trainingTeamType: "",
  orgName: "",
  dateEstablish: "",
  orgType: "",
  parentOrg: "",
  state: "",
  city: "",
  district: "",
  pinCode: "",
  address: "",
};

export { roleData, steps, initialFormData };
