-- Create index for first letter of name
CREATE INDEX idx_name_first ON names ((LEFT(name, 1)));