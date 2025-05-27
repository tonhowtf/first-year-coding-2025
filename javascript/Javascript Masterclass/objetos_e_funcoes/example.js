// const title = "Clean Code"
// const author = "Robert C. Martin";
// const book = {
//   title: title,
//   author: author,
//   pages: 464,
//   language: "English",
//   available: true
// };
// console.log(book);

// const key1 = "title";
// const key2 = "author";
// const key3 = "pages";
// const key4 = "language";
// const key5 = "available";

// const book = {};
// book[key1] = "Clean Code";
// book[key2] = "Robert C. Martin";
// book[key3] = 464;
// book[key4] = "English";
// book[key5] = true;
// console.log(book);

const book1 = {
  title: "Clean Code",
  author: "Robert C. Martin",
  pages: 464,
  language: "English",
  available: true
};
// for (let key in book) {
//   console.log(book[key])
// }
const book2 = {};
for (let key in book1) {
  book2[key] = book1[key];
}
console.log(book2)