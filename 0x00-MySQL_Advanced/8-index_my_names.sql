-- Create index idx_name_first on the first letter of the name column
CREATE INDEX idx_name_first ON names (LEFT(name(1)));
