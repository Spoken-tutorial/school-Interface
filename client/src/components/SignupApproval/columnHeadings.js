//common column headings
const headCells = [
  {
    id: "firstName",
    numeric: false,
    disablePadding: true,
    label: "First Name",
  },
  {
    id: "lastName",
    numeric: false,
    disablePadding: false,
    label: "Last Name",
  },
  {
    id: "email",
    numeric: false,
    disablePadding: false,
    label: "Email",
  },
  {
    id: "userName",
    numeric: false,
    disablePadding: false,
    label: "User Name",
  },
  {
    id: "phone",
    numeric: false,
    disablePadding: false,
    label: "Phone",
  },
];

//role speicific column headings
const additionDetailsCells = {
  Organization: [
    {
      id: "dob",
      numeric: false,
      disablePadding: false,
      label: "DoB",
    },
    {
      id: "organizationName",
      numeric: false,
      disablePadding: false,
      label: "Organization Name",
    },
    {
      id: "dateOfEstablishment",
      numeric: false,
      disablePadding: false,
      label: "Date of Establishment",
    },
    {
      id: "type",
      numeric: false,
      disablePadding: false,
      label: "Type",
    },
    {
      id: "parentOrganization",
      numeric: false,
      disablePadding: false,
      label: "Parent Organization",
    },
    {
      id: "state",
      numeric: false,
      disablePadding: false,
      label: "State",
    },
    {
      id: "city",
      numeric: false,
      disablePadding: false,
      label: "City",
    },
    {
      id: "district",
      numeric: false,
      disablePadding: false,
      label: "District",
    },
    {
      id: "pincode",
      numeric: false,
      disablePadding: false,
      label: "Pincode",
    },
    {
      id: "address",
      numeric: false,
      disablePadding: false,
      label: "Address",
    },
  ],
  School: [
    {
      id: "dob",
      numeric: false,
      disablePadding: false,
      label: "DoB",
    },
    {
      id: "schoolName",
      numeric: false,
      disablePadding: false,
      label: "School Name",
    },
    {
      id: "dateOfEstablishment",
      numeric: false,
      disablePadding: false,
      label: "Date of Establishment",
    },
    {
      id: "type",
      numeric: false,
      disablePadding: false,
      label: "Type",
    },
    {
      id: "parentOrganization",
      numeric: false,
      disablePadding: false,
      label: "Parent Organization",
    },
    {
      id: "state",
      numeric: false,
      disablePadding: false,
      label: "State",
    },
    {
      id: "city",
      numeric: false,
      disablePadding: false,
      label: "City",
    },
    {
      id: "district",
      numeric: false,
      disablePadding: false,
      label: "District",
    },
    {
      id: "pincode",
      numeric: false,
      disablePadding: false,
      label: "Pincode",
    },
    {
      id: "address",
      numeric: false,
      disablePadding: false,
      label: "Address",
    },
  ],
  User: [
    {
      id: "dob",
      numeric: false,
      disablePadding: false,
      label: "DoB",
    },
    {
      id: "organization",
      numeric: false,
      disablePadding: false,
      label: "Organization",
    },
    {
      id: "school",
      numeric: false,
      disablePadding: false,
      label: "School",
    },
    {
      id: "role",
      numeric: false,
      disablePadding: false,
      label: "Role",
    },
  ],
  "Training Team": [
    {
      id: "type",
      numeric: false,
      disablePadding: false,
      label: "Type",
    },
  ],
};

export { headCells, additionDetailsCells };
