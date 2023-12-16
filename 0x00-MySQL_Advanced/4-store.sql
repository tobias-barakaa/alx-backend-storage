-- Create trigger to decrease quantity after adding a new order
DELIMITER //
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_quantity INT;

    -- Get the current quantity of the item
    SELECT quantity INTO item_quantity
    FROM items
    WHERE name = NEW.item_name;

    -- Update the quantity in the items table
    UPDATE items
    SET quantity = item_quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
