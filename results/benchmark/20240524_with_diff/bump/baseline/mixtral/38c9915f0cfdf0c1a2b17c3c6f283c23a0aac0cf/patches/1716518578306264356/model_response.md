Here's a possible patch for the client code:
```java
import org.cactoos.text.BytesOf;

//...

BytesOf splitText = new BytesOf(new SplitText(input, "\n"));
```
In this patch, we import the new `BytesOf` class and use it to create a new `SplitText` object using the new constructor that takes a `CharSequence` as a separator. This way, we can still split the input text into lines using the new library version.