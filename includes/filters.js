function unknown_cup(column) {
  return `starts_with(${column}, ${constants.unknown})`;
}
  
module.exports = {
  unknown_cup
};
