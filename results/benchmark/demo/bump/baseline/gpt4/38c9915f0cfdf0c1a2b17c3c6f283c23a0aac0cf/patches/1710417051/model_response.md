The error message suggests that the symbol `LengthOf` cannot be found. It seems like the dependency `org.cactoos.iterable.LengthOf` might have been removed or moved to a different package in the updated version of the library. 

Without knowing the exact details of the new version of the library, it's hard to provide a perfect solution. However, assuming that the functionality of `LengthOf` is to get the length of an iterable, you might replace it with native Java code:

```java
import java.util.Collection;

// Replace LengthOf with Collection.size()
int length = ((Collection<?>) iterable).size();
```

Please replace `iterable` with your actual iterable object. If your iterable object is not a Collection, you might need to convert it to a Collection or use a loop to calculate the length. 

Note: This is a general solution and might not work in all cases. Please check the new version of `org.cactoos` library and replace `LengthOf` with the equivalent functionality.