import * as React from "react";
import Box from "@mui/material/Box";
import Table from "@mui/material/Table";
import Paper from "@mui/material/Paper";
import PropTypes from "prop-types";
import TableData from "./TableData";
import TableDescription from "./TableDescription";
import TableToolbar from "./TableToolbar";
import TableContainer from "@mui/material/TableContainer";
import TablePagination from "@mui/material/TablePagination";
import TableColumnHeadings from "./TableColumnHeadings";

import { signupData } from "../../constants/Data/signupApproavl";
import { Container } from "@mui/material";

function descendingComparator(a, b, orderBy) {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}

function getComparator(order, orderBy) {
  return order === "desc"
    ? (a, b) => descendingComparator(a, b, orderBy)
    : (a, b) => -descendingComparator(a, b, orderBy);
}

function stableSort(array, comparator) {
  const stabilizedThis = array.map((el, index) => [el, index]);
  stabilizedThis.sort((a, b) => {
    const order = comparator(a[0], b[0]);
    if (order !== 0) {
      return order;
    }
    return a[1] - b[1];
  });
  return stabilizedThis.map((el) => el[0]);
}

// main table
export default function ApprovalTable({ signupRole }) {
  const [order, setOrder] = React.useState("asc");
  const [orderBy, setOrderBy] = React.useState("calories");
  const [selected, setSelected] = React.useState([]);
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);

  const handleRequestSort = (event, property) => {
    const isAsc = orderBy === property && order === "asc";
    setOrder(isAsc ? "desc" : "asc");
    setOrderBy(property);
  };

  const handleSelectAllClick = (event) => {
    if (event.target.checked) {
      const newSelected = signupData[signupRole].map((n) => n.id);
      setSelected(newSelected);
      return;
    }
    setSelected([]);
  };

  //function to handle individual row select
  const handleClick = (event, id) => {
    const selectedIndex = selected.indexOf(id);
    //saves the id of selected row
    let newSelected = [];
    if (selectedIndex === -1) {
      newSelected = newSelected.concat(selected, id);
    } else if (selectedIndex === 0) {
      newSelected = newSelected.concat(selected.slice(1));
    } else if (selectedIndex === selected.length - 1) {
      newSelected = newSelected.concat(selected.slice(0, -1));
    } else if (selectedIndex > 0) {
      newSelected = newSelected.concat(
        selected.slice(0, selectedIndex),
        selected.slice(selectedIndex + 1)
      );
    }
    setSelected(newSelected);
  };

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  const isSelected = (id) => selected.indexOf(id) !== -1;

  // Avoid a layout jump when reaching the last page with empty rows.
  const emptyRows =
    page > 0
      ? Math.max(0, (1 + page) * rowsPerPage - signupData[signupRole].length)
      : 0;

  const visibleRows = React.useMemo(
    () =>
      stableSort(signupData[signupRole], getComparator(order, orderBy)).slice(
        page * rowsPerPage,
        page * rowsPerPage + rowsPerPage
      ),
    [order, orderBy, page, rowsPerPage, signupRole]
  );

  return (
    <>
      <Box
        sx={{
          width: "100%",
          display: "flex",
          justifyContent: "center",
          alignContent: "center",
        }}
      >
        <Box sx={{ width: "96%" }}>
          {/* table description */}
          <TableDescription signupRole={signupRole} />
          <Paper sx={{ width: "100%", mb: 2 }}>
            {/* table toolbar */}
            <TableToolbar
              numSelected={selected.length}
              signupRole={signupRole}
            />
            <TableContainer>
              <Table
                stickyHeader
                sx={{ minWidth: 750 }}
                aria-labelledby="tableTitle"
              >
                {/* table column headings */}
                <TableColumnHeadings
                  numSelected={selected.length}
                  order={order}
                  orderBy={orderBy}
                  onSelectAllClick={handleSelectAllClick}
                  onRequestSort={handleRequestSort}
                  rowCount={signupData[signupRole].length}
                  signupRole={signupRole}
                />

                {/* table rows */}
                <TableData
                  signupRole={signupRole}
                  visibleRows={visibleRows}
                  isSelected={isSelected}
                  handleClick={handleClick}
                  emptyRows={emptyRows}
                />
              </Table>
            </TableContainer>
            <TablePagination
              rowsPerPageOptions={[5, 10, 25]}
              component="div"
              count={signupData[signupRole].length}
              rowsPerPage={rowsPerPage}
              page={page}
              onPageChange={handleChangePage}
              onRowsPerPageChange={handleChangeRowsPerPage}
            />
          </Paper>
        </Box>
      </Box>
    </>
  );
}

ApprovalTable.propTypes = {
  signupRole: PropTypes.string.isRequired,
};
