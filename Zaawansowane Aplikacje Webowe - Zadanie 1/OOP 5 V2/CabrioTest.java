package org.example;
import org.testng.annotations.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CabrioTest {
    @Test
    public void testCabrio() {
        Cabrio car = new Cabrio("Gelandewagen", "Mercedes");
        assertEquals("Gelandewagen", car.getName());
        assertEquals("Mercedes", car.getBrand());
        assertFalse(car.isMoving());
        assertFalse(car.isRoofOpen());
    }

    @Test
    public void testOpenRoofWhileDriving() {
        Cabrio car = new Cabrio("Gelandewagen", "Mercedes");
        car.startMoving();
        assertThrows(IllegalStateException.class, () -> {
            car.openRoof();
        });
        assertFalse(car.isRoofOpen());
    }

    @Test
    public void testCloseRoofWhileDriving() {
        Cabrio car = new Cabrio("Gelandewagen", "Mercedes");
        car.startMoving();
        assertThrows(IllegalStateException.class, () -> {
            car.closeRoof();
        });
        assertFalse(car.isRoofOpen());
    }

    @Test
    public void testOpenAndCloseRoof() {
        Cabrio car = new Cabrio("Gelandewagen", "Mercedes");
        assertFalse(car.isRoofOpen());
        car.openRoof();
        assertTrue(car.isRoofOpen());
        car.closeRoof();
        assertFalse(car.isRoofOpen());
    }
}
