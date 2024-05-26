Here's a patch that you can apply to the code in order to fix the error:

```java
import java.util.Objects;

// ...

if (isNull(someVariable)) {
    // ...
}
```

In this patch, I have imported the `Objects` class explicitly instead of using a static import for the `isNull` method. This is because the static import statement is causing a syntax error in your code. Instead, you can import the `Objects` class and use the `isNull` method with the full qualification.