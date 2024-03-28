It seems like the import statement is failing because the `LengthOf` class cannot be found in the `org.cactoos.iterable` package. This could be due to a change in the package structure in a newer version of the library or the class might have been removed.

Unfortunately, without knowing more about the external dependency, it's hard to provide a specific fix. However, you can try to find an alternative class in the `org.cactoos.iterable` package that provides similar functionality. If such a class does not exist, you might need to implement the functionality yourself.

Here is a general example of how you could replace the `LengthOf` functionality:

```java
import org.cactoos.iterable.IterableOf;

Iterable<String> iterable = new IterableOf<>("A", "B", "C");

int length = 0;
for (Object i : iterable) {
    length++;
}
```

In this example, `IterableOf` is used to create an iterable object. The length of the iterable is then calculated by iterating over the elements and incrementing a counter. Please replace `IterableOf` and the iterable object with the actual objects used in your code.