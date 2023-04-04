**Cbario_al** :+1:
Klasa Cabrio przechowuje nazwę i markę samochodu oraz informację, czy samochód porusza się oraz czy dach jest otwarty. Konstruktor klasy Cabrio przyjmuje argumenty name i brand i inicjuje pola isMoving i isRoofOpen na false.

Metoda openRoof otwiera dach, ale tylko jeśli samochód nie porusza się. W przeciwnym wypadku wyświetlany jest komunikat o błędzie. Metoda closeRoof zamyka dach, ale także tylko wtedy, gdy samochód nie porusza się. Metoda start ustawia wartość pola isMoving na true, co oznacza, że samochód porusza się. Metoda stop ustawia wartość pola isMoving na false, co oznacza, że samochód nie porusza się.

Aby przetestować klasę Cabrio, można utworzyć obiekt tej klasy i wywołać metody na tym obiekcie:

```
public class Main {
    public static void main(String[] args) {
        Cabrio cabrio = new Cabrio("MX-5", "Mazda");

        cabrio.openRoof(); // otwiera dach, ponieważ samochód nie porusza się
        cabrio.start(); // uruchamia samochód
        cabrio.openRoof(); // wyświetla komunikat o błędzie, ponieważ samochód się porusza
        cabrio.stop(); // zatrzymuje samochód
        cabrio.closeRoof(); // zamyka dach, ponieważ samochód nie porusza się
    }
}
```

W tym przykładzie najpierw tworzony jest obiekt cabrio klasy Cabrio. Następnie wywoływane są metody openRoof, start, openRoof, stop i closeRoof na tym obiekcie. W wyniku tego otwieranie i zamykanie dachu jest możliwe tylko wtedy, gdy samochód się nie porusza.
