Here is a fixed version of the failing method in `ChachaDecoder.java`:

```java
import java.util.EnumSet;
import java.util.Set;

public class ChachaDecoder {
    // existing code...

    private void fail(short alert) {
        Set<AlertDescription> descriptions = EnumSet.of(AlertDescription.decode(alert));
        throw new TlsFatalAlert(AlertDescription.INTERNAL_ERROR, descriptions);
    }

    // existing code...
}
```

In this fixed version, I replaced the usage of the removed constructor `TlsFatalAlert(short)` with the new constructor `TlsFatalAlert(short, Set<AlertDescription>)`. I also imported the necessary classes for the `EnumSet` and `Set` interfaces.

Note that I had to create a variable `descriptions` of type `Set<AlertDescription>` to pass as an argument to the new constructor. I used the static method `AlertDescription.decode(short)` to convert the `short` value to an `AlertDescription` object, and then added it to the `EnumSet`.