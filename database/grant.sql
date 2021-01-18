CREATE ROLE 'store_staff', 'customer';

-- grant for store_staff in
-- Book
GRANT UPDATE, SELECT ON bookstore.book TO 'store_staff';
-- EBook
GRANT UPDATE, SELECT ON bookstore.ebook TO 'store_staff';
-- Paper Book
GRANT UPDATE, SELECT ON bookstore.paperbook TO 'store_staff';
-- Transaction
GRANT UPDATE, SELECT ON bookstore.transaction TO 'store_staff';
-- End i8

-- Author
GRANT SELECT ON bookstore.author TO 'store_staff';
-- Who wrote this book?
GRANT SELECT ON bookstore.writtenby TO 'store_staff';
-- Payment
GRANT SELECT ON bookstore.payment TO 'store_staff';
-- Transfer
GRANT SELECT ON bookstore.transfer TO 'store_staff';
-- Card Payment
GRANT SELECT ON bookstore.cardpayment TO 'store_staff';
-- Order book
GRANT SELECT ON bookstore.orderbook TO 'store_staff';
-- Stored at
GRANT SELECT ON bookstore.stored TO 'store_staff';
-- Bookstorage
GRANT SELECT ON bookstore.bookstorage TO 'store_staff';

-- grant for customer in
-- Update and Show infor about customer, payment and transaction
GRANT UPDATE, SELECT ON bookstore.customer TO 'customer';
GRANT SELECT, SELECT ON bookstore.payment TO 'customer';
GRANT UPDATE, SELECT ON bookstore.cardpayment TO 'customer';
GRANT UPDATE, SELECT ON bookstore.transfer TO 'customer';
GRANT UPDATE, SELECT ON bookstore.creditcard TO 'customer';
GRANT USELECT ON bookstore.transaction TO 'customer'; -- i14, 15, 16
-- Show necessary infor about Book, Author
GRANT SELECT ON bookstore.book TO 'customer';
GRANT SELECT ON bookstore.ebook TO 'customer';
GRANT SELECT ON bookstore.paperbook TO 'customer';
GRANT SELECT ON bookstore.author TO 'customer';
GRANT SELECT ON bookstore.field TO 'customer';
GRANT SELECT ON bookstore.keyword TO 'customer';
-- Comments about purchased books
GRANT SELECT, UPDATE ON bookstore.response TO 'customer';