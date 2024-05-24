Here's the proposed patch:

```java
import static org.apache.commons.lang3.StringUtils.isEmpty;
import static org.apache.commons.lang3.StringUtils.isNotBlank;

// ...

if (isAllBlank(someString)) {
    // ...
}

// Change to:
if (isAllBlank(someString)) {
    // ...
} else if (isNotBlank(someString)) {
    // ...
} else {
    // ...
}

// or

if (isEmpty(someString)) {
    // ...
} else {
    // ...
}

// or

if (isBlank(someString)) {
    // ...
} else {
    // ...
}
```

The `isAllBlank` method has been removed from the `StringUtils` class in the updated library. You can use alternative methods like `isEmpty`, `isNotBlank`, or `isBlank` from the same `StringUtils` class to achieve the same functionality.

In case you are sure that the string will never be null, you can use `isEmpty`, `isNotBlank`, or `isBlank` directly. Otherwise, you should check for null before calling these methods.