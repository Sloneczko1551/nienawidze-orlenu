public class Cabrio {
    private String name;
    private String brand;
    private boolean isMoving;
    private boolean isRoofOpen;

    public Cabrio(String name, String brand) {
        this.name = name;
        this.brand = brand;
        this.isMoving = false;
        this.isRoofOpen = false;
    }

    public void openRoof() {
        if (isMoving) {
            System.out.println("Cannot open roof while the car is moving.");
        } else {
            isRoofOpen = true;
        }
    }

    public void closeRoof() {
        if (isMoving) {
            System.out.println("Cannot close roof while the car is moving.");
        } else {
            isRoofOpen = false;
        }
    }

    public void start() {
        isMoving = true;
    }

    public void stop() {
        isMoving = false;
    }
}
