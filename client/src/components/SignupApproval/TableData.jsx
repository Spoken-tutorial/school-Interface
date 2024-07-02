import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableRow from "@mui/material/TableRow";
import Checkbox from "@mui/material/Checkbox";
import PropTypes from "prop-types";
import { colorScheme } from "../../constants/colorScheme";
import { headCells, additionDetailsCells } from "./columnHeadings";

function TableData({
  signupRole,
  visibleRows,
  isSelected,
  handleClick,
  emptyRows,
}) {
  const columnHeadings = additionDetailsCells[signupRole]
    ? [...headCells, ...additionDetailsCells[signupRole]]
    : headCells;

  return (
    <TableBody>
      {visibleRows.map((row, index) => {
        const isItemSelected = isSelected(row.id);
        const labelId = `enhanced-table-checkbox-${index}`;
        return (
          <TableRow
            hover
            onClick={(event) => handleClick(event, row.id)}
            role="checkbox"
            aria-checked={isItemSelected}
            tabIndex={-1}
            key={row.id}
            selected={isItemSelected}
            sx={{
              cursor: "pointer",
              "&.Mui-selected": {
                backgroundColor: colorScheme.primaryOrangeLight,
                "&:hover": {
                  backgroundColor: "#FFEAD6",
                },
              },
            }}
          >
            <TableCell padding="checkbox">
              <Checkbox
                checked={isItemSelected}
                inputProps={{
                  "aria-labelledby": labelId,
                }}
                sx={{
                  color: colorScheme.secondaryGrey,
                  "&.Mui-checked": {
                    color: colorScheme.primaryOrange,
                  },
                }}
              />
            </TableCell>
            {/* row cell names mapping */}
            {columnHeadings.map((cell) => (
              <TableCell key={cell.id} align={cell.numeric ? "right" : "left"}>
                {row[cell.id]}
              </TableCell>
            ))}
          </TableRow>
        );
      })}
      {emptyRows > 0 && (
        <TableRow
          style={{
            height: 53 * emptyRows,
          }}
        >
          <TableCell colSpan={6} />
        </TableRow>
      )}
    </TableBody>
  );
}
TableData.propTypes = {
  signupRole: PropTypes.string.isRequired,
  handleClick: PropTypes.func.isRequired,
  visibleRows: PropTypes.array.isRequired,
  isSelected: PropTypes.func.isRequired,
  emptyRows: PropTypes.number.isRequired,
};
export default TableData;
